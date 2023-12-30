import demo_data_classical_Thellier
import graphing
import matplotlib.pyplot as plt
from scipy.integrate import trapz
import numpy as np

def reformat_th_to_data(filename):
    with open(filename, 'r') as infile:
        _data = []
        nline = -1 #I want it to be zero-indexed, but I also need to increment at the start of the loop because of the continue statements
        temperatures = []
        for line in infile:
            nline +=1
            print(f'line number {nline}: {line}')
            values = line.strip().split(',')
            print(values[0])
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

def plot_data(*AraiData):
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
            step_number = step[0]
            for xstep, xvalue in ptrm_gained:
                if xstep == step_number:
                    x_values.append(xvalue)  
            for ystep, yvalue in nrm_rem:
                if ystep == step_number:
                    y_values.append(yvalue)
                    step_labels.append(step_number)
        plt.plot(x_values, y_values, marker='o', label=legend_label, color=colour)

        #for i, label in enumerate(step_labels):
        #    plt.text(x_values[i], y_values[i], str(label), ha='right', va='bottom')  # Add label for each point
        
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



def main():
    _dataTest1 = reformat_th_to_data("C:/Users/murray98/Documents/Paleointensity/MD_phenom_mod/Phenom_mod_ZIP/MMSS12-7f.th")
    _dataTest2 = reformat_th_to_data("C:/Users/murray98/Documents/Paleointensity/MD_phenom_mod/Phenom_mod_ZIP/modres_customT11_lambda02_antiparallel.th")
    #specimen = demo_data_classical_Thellier.get("MARYTEST")

    specimen1 = demo_data_classical_Thellier._demo_data_to_real_format_thermal(_dataTest1)
    AraiData1 = graphing.plot_arai(specimen1)
    print(AraiData1)
    #plot_data(AraiData1)

    specimen2 = demo_data_classical_Thellier._demo_data_to_real_format_thermal(_dataTest2)
    AraiData2 = graphing.plot_arai(specimen2)
    print(AraiData2)
    #plot_data(AraiData2)

    plot_data((AraiData1, "MMSS12.7f - measured data", "royalblue"), (AraiData2, "modres_customT11_lambda02_antiparallel_B1 - modelled results", "orange"))



main() 

##Testing
#test_x = [0,1,3,2,5]
#test_y = [10,10,8,2,0]
#test_area = calc_area(test_x, test_y)
#print(test_area)