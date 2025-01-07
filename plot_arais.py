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
    
    #Aesthitic choices
    #figure size is set in inches 
    plt.figure(figsize=(3, 3))  
    legend_fs = 8 
    legendTxtColor = "#595959" #dark grey


    plotTitle = "AraiComparison"
    for data, legend_label, title, colour in AraiData:
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

        plt.plot(x_values, y_values, marker='o', label=legend_label,
                 color=colour, alpha=0.7)
        # plt.plot(x_values[startStep:endStep], y_values[startStep:endStep],
        #          marker='o', label=legend_label, color=colour, alpha=0.7)
        
                # Add label for each point
        #for i, label in enumerate(step_labels):
        #    plt.text(x_values[i], y_values[i], str(label), ha='right', va='bottom')  

        plt.ylim(0, 2)
        plt.xlim(0, 2)
        # Print statements for debugging
        print("\n")
        print("title", title, "\n")
        print("legend_label", legend_label, "\n")
        print(x_values, y_values)
        print("\n")
        print(x_values[startStep:endStep], y_values[startStep:endStep])

        # # Create a table with the data values
        # table_data = list(zip(x_values[startStep:endStep],
        #                       y_values[startStep:endStep]))
        # col_labels = ['x values', 'y values']
        # row_labels = [f'Step {i}' for i in range(startStep, endStep)]
        
        # # Add the table to the plot
        # table = plt.table(cellText=table_data,
        #                   colLabels=col_labels,
        #                   colWidths=[0.2,0.2] ,
        #                   loc='left', cellLoc='center',
        #                   bbox=[-0.5, 0, 0.8, 1])
        
        # # Adjust layout to make room for the table
        # plt.subplots_adjust(left=0.2, bottom=0.4)
        plotTitle += '_'
        plotTitle += title

    plt.legend(fontsize =legend_fs, prop={"style": "italic"}, labelcolor = legendTxtColor)
    plt.title(title)
    #plt.xlabel('pTRM Gained / NRM0')
    #plt.ylabel('NRM Remaining / NRM0')
    plt.savefig(f'{folderPath}{plotTitle}.png')    
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

def modelNaming(customT, lamda, theta, B):
    # Format lamda to appear as 020
    lamda_formatted = f"{lamda:.2f}".replace('.', '')
    theta_formatted = f"{theta:03}"
    B_formatted = f"{B:.3f}".replace('.', '')
    
    if B ==1:
        modelFile = f'modres_customT{customT}_lambda{lamda_formatted}_theta{theta_formatted}.th'
        modelLegend = f"Model: T{customT} λ={lamda:.2f} θ={theta_formatted}\N{DEGREE SIGN}"
        modelTitle = f'modres_customT{customT}_lambda{lamda_formatted}_theta{theta_formatted}'
    
    else: 
        modelFile = f'modres_customT{customT}_lambda{lamda_formatted}_theta{theta_formatted}_B{B_formatted}.th'
        modelLegend = f"Model:\n T{customT} λ={lamda:.2f} θ={theta_formatted}\N{DEGREE SIGN} B={B:.3f}"
        modelTitle = f'modres_customT{customT}_lambda{lamda_formatted}_theta{theta_formatted}_B{B_formatted}'

    return modelFile, modelLegend, modelTitle




def main():

    ##aesthetic choices
    colorModel = "#e60073"
    colorExp = "#3900e6"

    # Generate a sequential colormap
    cmap = plt.get_cmap('viridis')
    num_colors = 4  # Number of datasets to plot
    colors = [cmap(i / num_colors) for i in range(num_colors)]


    ##Model and data to plot
    expTitle="MMSS12-2A"
    customT = 80
    lamda = 0.28
    theta = 27
    B=0.796

    modelFile, modelLegend, modelTitle = modelNaming(customT, lamda, theta, B)

    AraiData_exp = run_together(f"{folderPath}{expTitle}.th")
    plot_data(0,200, (AraiData_exp, f"Observed data: {expTitle}", expTitle, colorExp))

    AraiData_prefModel = run_together(f"{folderPath}{modelFile}")
    plot_data(0, 200,
        (AraiData_prefModel, modelLegend, modelTitle, colorModel),
        (AraiData_exp, f"Observed data: {expTitle}", expTitle, colorExp)
        )
    
    # lamda=0.1
    # modelFile010, modelLegend010, modelTitle010 = modelNaming(customT, lamda, theta, B)
    # AraiData_Model_lambda010 = run_together(f"{folderPath}{modelFile010}")

    # lamda=0.2
    # modelFile020, modelLegend020, modelTitle020 = modelNaming(customT, lamda, theta, B)
    # AraiData_Model_lambda020 = run_together(f"{folderPath}{modelFile020}")

    # lamda=0.3
    # modelFile030, modelLegend030, modelTitle030 = modelNaming(customT, lamda, theta, B)
    # AraiData_Model_lambda030 = run_together(f"{folderPath}{modelFile030}")

    # lamda=0.4
    # modelFile040, modelLegend040, modelTitle040 = modelNaming(customT, lamda, theta, B)
    # AraiData_Model_lambda040 = run_together(f"{folderPath}{modelFile040}")

    # plot_data(0, 200,
    #     (AraiData_Model_lambda010, modelLegend010, modelTitle010, colors[0]),
    #     (AraiData_Model_lambda020, modelLegend020, modelTitle020, colors[1]),
    #     (AraiData_Model_lambda030, modelLegend030, modelTitle030, colors[2]),
    #     (AraiData_Model_lambda040, modelLegend040, modelTitle040, colors[3]),
    #     (AraiData_exp, f"Observed data: {expTitle}", expTitle, "orange")
    #     )

    



       

folderPath = "C:/Users/murray98/Documents/Paleointensity/MD_phenom_mod/ABPhenmod/Phenom_mod_ZIP/"

main() 

