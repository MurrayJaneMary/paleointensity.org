"""
Code to directly plot arai plots from .th files, based on paleointensity.org code

Author: Mary Murray 
Date: December 2023
"""


import demo_data_classical_Thellier
import graphing
import matplotlib.pyplot as plt
from scipy.integrate import trapz
import numpy as np

def reformat_th_to_data(filename):
    """Inputs a .th Utrecht format file and converts it to paleointensity.org's internal data format. """
    with open(filename, 'r') as infile:
        _data = []
        nline = -1 #I want it to be zero-indexed, but I also need to increment at the start of the loop because of the continue statements
        temperatures = []
        for line in infile:
            nline +=1
            #print(f'line number {nline}: {line}')
            values = line.strip().split(',')
            #print(values[0])
            if nline ==0:
                temperature = 0
                temperatures.append(temperature)
                continue
            if nline == 1:
                samplename = values[0]
                temperature = 0
                temperatures.append(temperature)
                continue

            if values[0] == "9999":
                break


            temperature = str(values[0]).split('.')[0]
            temperature = float(temperature)
            temperatures.append(temperature)
            steptype = str(values[0]).split('.')[1]

            values[1] = float(values[1])
            values[2] = float(values[2])
            values[3] = float(values[3])
            values[4] = float(values[4])

            if steptype == "00": #z step
                dataline = [samplename, samplename, values[1], values[2], values[3], values[4], 0, 0, 0, \
                            values[5], values[6], temperature, 0, 0, 0, 0, temperatures[nline-1]]
            
            if steptype == "11": #I step
                dataline = [samplename, samplename, values[1], values[2], values[3], values[4], 0, 0, 0, \
                            values[5], values[6], temperature, 40, 0, 90, 1, temperatures[nline-1]]
                
            if steptype == "12": #P step
                dataline = [samplename, samplename, values[1], values[2], values[3], values[4], 0, 0, 0, \
                            values[5], values[6], temperature, 40, 0, 90, 2, temperatures[nline-1]]

            _data.append(dataline)
    return(_data)

def straight_line(m, x, c):
    y=m*x+c
    return y

def plot_data(startStep=0, endStep=100, *AraiData):
    #print(AraiData)
    plt.figure(figsize=(8,5))

    for data, legend_label, colour in AraiData:
        ptrm_gained = data[0]
        nrm_rem = data[1]
        ptrmCheck = data[2]
        tailCheck = data[3]
        order_steps = data[4]

        x_values = [0]
        y_values = [1]
        step_labels = [0]  # Initialize with the starting point

        for step in order_steps:
            step_temp = step[0]
            for xstep, xvalue in ptrm_gained:
                if xstep == step_temp:
                    x_values.append(xvalue)
            for ystep, yvalue in nrm_rem:
                if ystep == step_temp:
                    y_values.append(yvalue)
                    step_labels.append(step_temp)

        plt.plot(x_values, y_values, marker='.', label=legend_label, color=colour, alpha=0.3)
        plt.plot(x_values[startStep:endStep], y_values[startStep:endStep], marker='o', label=legend_label, color=colour, alpha=0.7)
        print("/n")
        print(legend_label, "/n")
        print(x_values, y_values)
        print("/n")
        print(x_values[startStep:endStep], y_values[startStep:endStep])
        
        # Add label for each point
        for i, label in enumerate(step_labels):
            plt.text(x_values[i], y_values[i], str(label), ha='right', va='bottom')  
        
        # Add pTRM check line
        for i in range(len(ptrmCheck)):        
            start_point = (ptrmCheck[i][3], ptrmCheck[i][4])
            end_point = (ptrmCheck[i][1],ptrmCheck[i][2])
            #plt.annotate('', xy=start_point, xytext=mid_point, arrowprops=dict(facecolor='black', arrowstyle='-'))
            plt.annotate('', xy=start_point, xytext=end_point, arrowprops=dict(alpha= 0.4, facecolor=colour, arrowstyle='<-', connectionstyle="angle,angleA=-90,angleB=180,rad=0"))
            plt.plot(ptrmCheck[i][1], ptrmCheck[i][2], marker='^', color=colour, alpha=0.4)

       

        
       # Calculate the area under the curve using trapezoidal integration
        area = trapz(y_values, x=x_values)
        
        print(f'Area for {legend_label} is {area}, theorectical area 0.5  so a difference of {0.5 - area}')

        area_difference = calc_area(x_values, y_values)
        print(f'Area difference for {legend_label} is {area_difference}')

    plt.ylim(0, None)
    plt.xlabel('pTRM gained/NRM0')
    plt.ylabel('NRM remaining/NRM0')
    plt.legend()


    plt.show()

def calc_area(x_values, y_values):
    #calculate the difference between the points and an ideal line
    area_total = 0
    m = (y_values[-1]-y_values[0])/x_values[-1]
    #print(f'm is {m}')
    for i in range(len(x_values)-1):
        #print (f'{i} out of {range(len(x_values))}')
        ideal_y1 = m*x_values[i] + y_values[0]
        ideal_y2 = m*x_values[i+1] + y_values[0]
        diff_y1 = y_values[i] - ideal_y1
        diff_y2 = y_values[i+1] - ideal_y2

        #print(y_values[i], ideal_y1)
        #print(y_values[i+1], ideal_y2)
        #print(x_values[i], x_values[i+1], diff_y1, diff_y2)
        
        if (diff_y1*diff_y2) < 0 : # if the lines intersect, one difference will be positive and the other negative
            area = 0.5*(x_values[i+1]-x_values[i])*(diff_y2**2 + diff_y1**2)/(abs(diff_y2) + abs(diff_y1))
            ##Pretty sure this formula is correct but I'd like a better way to double check it
        else:
            area= 0.5*(abs(diff_y1)+abs(diff_y2))*(x_values[i+1]-x_values[i])
        
        ##importantly, these areas could be negative if (x_values[i+1]-x_values[i]) is negative. This is important because
            ## it accounts for the case where the line goes backwards.  
        area_total += area 
        #print(area_total)
    return area_total

def run_together(filepath):
    """Inputs filepath to a .th file and returns formatted datapoints for an Arai plot"""

    _data = reformat_th_to_data(filepath)
    print(filepath)
    print(_data)
    specimen = demo_data_classical_Thellier._demo_data_to_real_format_thermal(_data)
    AraiData = graphing.plot_arai(specimen)
    return AraiData



def main():

    # Generate a sequential colormap
    cmap = plt.get_cmap('viridis')
    num_colors = 4  # Number of datasets to plot
    colors = [cmap(i / num_colors) for i in range(num_colors)]


    AraiData_exp = run_together(f"{folderPath}MMSS13-7A.th")
    plot_data(0,200,(AraiData_exp, "Experimental data", "orange"))


    AraiData_prefModel = run_together(f"{folderPath}modres_customT54_lambda014_theta014.th")

    plot_data(0, 200,
        (AraiData_prefModel, "lambda 0.14, theta 014, customT54", "blue"),
        (AraiData_exp, "MMSS13-7A - measured data", "orange")


    )
       

folderPath = "C:/Users/murray98/Documents/Paleointensity/MD_phenom_mod/ABPhenmod/Phenom_mod_ZIP/"

main() 

##Testing
#test_x = [0,1,3,2,5]
#test_y = [10,10,8,2,0]
#test_area = calc_area(test_x, test_y)
#print(test_area)