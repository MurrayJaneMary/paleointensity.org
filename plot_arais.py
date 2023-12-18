import demo_data_classical_Thellier
import graphing
import matplotlib.pyplot as plt

specimen = demo_data_classical_Thellier.get("MARYTEST")

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
