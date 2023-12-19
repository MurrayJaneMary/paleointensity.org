import demo_data_classical_Thellier
import graphing
import matplotlib.pyplot as plt

def reformat_th_to_data(filename):
    with open(filename, 'r') as infile:
        _data = []
        nline = -1 #I want it to be zero-indexed, but I also need to increment at the start of the loop because of the continue statements
        temperatures = []
        for line in infile:
            nline +=1
            print(f'line number {nline}: {line}')
            values = line.strip().split(',')
            print("these are words")
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
            temperatures.append(temperature)
            steptype = str(values[0]).split('.')[1]

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

_dataTest1 = reformat_th_to_data("C:/Users/murray98/Documents/Paleointensity/MD_phenom_mod/Phenom_mod_ZIP/modres_customT18_lambda05_antiparallel_B1.th")

#specimen = demo_data_classical_Thellier.get("MARYTEST")

specimen = demo_data_classical_Thellier._demo_data_to_real_format_thermal(_dataTest1)


AraiData = graphing.plot_arai(specimen)

print(AraiData)

ptrm_gained = AraiData[0]
nrm_rem = AraiData[1]
ptrmCheck = AraiData[2]
tailCheck = AraiData[3]
order_steps = AraiData[4]


def plot_data(AraiData):
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
    plt.plot(x_values, y_values, marker='o')

    for i, label in enumerate(step_labels):
        plt.text(x_values[i], y_values[i], str(label), ha='right', va='bottom')  # Add label for each point
    
    # Add pTRM check line
    for i in range(len(ptrmCheck)):        
        start_point = (ptrmCheck[i][3], ptrmCheck[i][4])
        dx = -1*ptrmCheck[i][1]
        dy = ptrmCheck[i][2] - start_point[1]
        end_point = (ptrmCheck[i][1],ptrmCheck[i][2])
        #plt.annotate('', xy=start_point, xytext=mid_point, arrowprops=dict(facecolor='black', arrowstyle='-'))
        plt.annotate('', xy=start_point, xytext=end_point, arrowprops=dict(facecolor='black', arrowstyle='<-', connectionstyle="angle,angleA=-90,angleB=180,rad=0"))
        plt.plot(ptrmCheck[i][1],ptrmCheck[i][2], marker='^', color='black')
    
    plt.xlabel('pTRM gained')
    plt.ylabel('NRM remaining')



    plt.show()


plot_data(AraiData)
