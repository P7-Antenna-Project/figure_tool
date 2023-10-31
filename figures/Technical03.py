from figurelib.figure import FigureCollection
import matplotlib.pyplot as plt
from figures.cst_loader import load_cst_filePOLAR, load_cst_file
import numpy as np
import pickle

from matplotlib.ticker import FuncFormatter

# Some example data to display

collection = FigureCollection("03Technical")




@collection.plot_figure(only_build_this=False)
def mutualCouplingDegrading_sParams():   
    with open('Data\data_s11_unpolar.pkl', 'rb') as pkl_path: #Dump the pickle file at the given file path
        file_data11 = pickle.load(pkl_path)
    with open('Data\data_s21_unpolar.pkl', 'rb') as pkl_path: #Dump the pickle file at the given file path
        file_data21 = pickle.load(pkl_path)
    fig, ax = plt.subplots()
    frequency = np.arange(500, 3001, 2.5)    

    shift_value = 1050 # for shifting frequency of reference data. 
    colors = ['c', 'r', 'c', 'b', 'r', 'k']
    indices_to_plot = [0,10,15]
    
    # plotting S11 params: 
    for i in range(0,200):
        if i in indices_to_plot:
            color = colors[i % len(colors)]
            plt.plot(frequency,file_data11['S1,1'][i], color=color,linewidth=1.5,label=
            #one variable:
                #no logical reason to do the if-statement, but it makes 51 = 50 which looks nice.
            f"Dist = {1+file_data11['Parameter combination'][i]} mm" if i == 0 else f"Dist = {file_data11['Parameter combination'][i]} mm"
            )   

    # plotting S21 params:
    for i in range(0,200):
        if i in indices_to_plot:
            color = colors[i % len(colors)]
            plt.plot(frequency,file_data21['S2,1'][i], color=color,linewidth=1.5,linestyle='--')
           
    # plotting reference data:       
    ref_values = []
    frequency_ref = []
    with open('Data/REFunpolars.txt', 'rb') as file:
        file.readline()  # Skip the first line
        file.readline()  # Skip the second line
        file.readline()  # Skip the second line
        for line in file:
            if line != '\n':  # Skip the empty line
                parts = line.split()
                if len(parts) >= 2:  # Check that there are at least two parts
                    ref_values.append(float(parts[1]))
                    frequency_ref.append(float(parts[0]))
    # using shiftvalue and scaling to get the reference data to match the other data:
    plt.plot([f * 1000 + shift_value for f in frequency_ref],ref_values, color='black', linestyle='-.', linewidth=2, label='Reference (1 dipole)')

    plt.legend()
    plt.xlabel('Frequency [MHz]')
    plt.ylabel('S1,1 [dB]')
    plt.title('S1,1 and S2,1 of two dipoles with varying distance')
    plt.xlim([1200,2500])
    plt.ylim([-30,0])
    plt.grid()
    print(len(ref_values))
    return fig 


# Some example data to display
@collection.plot_figure(only_build_this=False)
def mutualCouplingDegrading_sParamsDiffPolari():   
    with open('Data\data_s11_DiffPolar.pkl', 'rb') as pkl_path: #Dump the pickle file at the given file path
        file_data11 = pickle.load(pkl_path)
    with open('Data\data_s21_DiffPolar.pkl', 'rb') as pkl_path: #Dump the pickle file at the given file path
        file_data21 = pickle.load(pkl_path)
    fig, ax = plt.subplots()
    frequency = np.arange(500, 3001, 2.5)    

    shift_value = 1050 # for shifting frequency of reference data. 
    colors = ['c', 'r', 'c', 'b', 'r', 'k']
    indices_to_plot = [0,10,15]
    
    # plotting S11 params: 
    for i in range(0,200):
        if i in indices_to_plot:
            color = colors[i % len(colors)]
            plt.plot(frequency,file_data11['S1,1'][i], color=color,linewidth=1.5,label=
            #one variable:
                #no logical reason to do the if-statement, but it makes 51 = 50 which looks nice.
            f"Dist = {1+file_data11['Parameter combination'][i]} mm" if i == 0 else f"Dist = {file_data11['Parameter combination'][i]} mm"
            )   

    # plotting S21 params:
    for i in range(0,200):
        if i in indices_to_plot:
            color = colors[i % len(colors)]
            plt.plot(frequency,file_data21['S2,1'][i], color=color,linewidth=1.5,linestyle='--')
           
    # plotting reference data:       
    ref_values = []
    frequency_ref = []
    with open('Data/REFunpolars.txt', 'rb') as file:
        file.readline()  # Skip the first line
        file.readline()  # Skip the second line
        file.readline()  # Skip the second line
        for line in file:
            if line != '\n':  # Skip the empty line
                parts = line.split()
                if len(parts) >= 2:  # Check that there are at least two parts
                    ref_values.append(float(parts[1]))
                    frequency_ref.append(float(parts[0]))
    # using shiftvalue and scaling to get the reference data to match the other data:
    plt.plot([f * 1000 + shift_value for f in frequency_ref],ref_values, color='black', linestyle='-.', linewidth=2, label='Reference (1 dipole)')

    plt.legend()
    plt.xlabel('Frequency [MHz]')
    plt.ylabel('S1,1 [dB]')
    plt.title('S1,1 and S2,1 of two dipoles with varying distance and \n orthogonal polarisation')
    plt.xlim([1200,2500])
    plt.ylim([-100,0])
    plt.grid()
    print(len(ref_values))
    return fig 

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np

    r = np.arange(0, 2, 0.01)
    theta = 2 * np.pi * r

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(theta, r)
    ax.set_rmax(2)
    ax.set_rticks([0.5, 1, 1.5, 2])  # Less radial ticks
    ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
    ax.grid(True)

    ax.set_title("A line plot on a polar axis", va='bottom')
    #plt.show()