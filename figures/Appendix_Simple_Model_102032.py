from figurelib.figure import FigureCollection
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle
from figures.cst_loader import load_cst_filePOLAR, load_cst_file

collection = FigureCollection("Simple model") # Name of the collection


@collection.plot_figure()
def Comparison_Of_Phi():
    On_bat = np.loadtxt(open('Data\Antenna_Port_Bat.txt'), delimiter='\t', skiprows=1, unpack=True)
    fig, ax = plt.subplots()   
    ax.plot(On_PCB[0], On_PCB[1], label='On PCB')
    ax.plot(On_bat[0], On_bat[1], label='On Battery')
    plt.xlabel('Frequency [MHz]')
    plt.ylabel('S1,1 [dB]')
    plt.title('Comparison of S1,1 parameters based on port placement')
    plt.legend()
    plt.grid()
    return fig

@collection.plot_figure()
def Comparison_Of_Theta():
    On_PCB = np.loadtxt(open('Data\Antenna_port_on_PCB.txt'), delimiter='\t', skiprows=1, unpack=True)
    On_bat = np.loadtxt(open('Data\Antenna_Port_Bat.txt'), delimiter='\t', skiprows=1, unpack=True)
    fig, ax = plt.subplots()   
    ax.plot(On_PCB[0], On_PCB[1], label='On PCB')
    ax.plot(On_bat[0], On_bat[1], label='On Battery')
    plt.xlabel('Frequency [MHz]')
    plt.ylabel('S1,1 [dB]')
    plt.title('Comparison of S1,1 parameters based on port placement')
    plt.legend()
    plt.grid()
    return fig

@collection.plot_figure()
def Comparison_Of_Port_placement():
    On_PCB = np.loadtxt(open('Data\Antenna_port_on_PCB.txt'), delimiter='\t', skiprows=1, unpack=True)
    On_bat = np.loadtxt(open('Data\Antenna_Port_Bat.txt'), delimiter='\t', skiprows=1, unpack=True)
    fig, ax = plt.subplots()   
    ax.plot(On_PCB[0], On_PCB[1], label='On PCB')
    ax.plot(On_bat[0], On_bat[1], label='On Battery')
    plt.xlabel('Frequency [MHz]')
    plt.ylabel('S1,1 [dB]')
    plt.title('Comparison of S1,1 parameters based on port placement')
    plt.legend()
    plt.grid()
    return fig

Adv_WC_WW   = np.loadtxt(open('Data/Generalisering/RTX/Adv_WC_WW.txt'),        delimiter='\t', skiprows=1, unpack=True)
Adv_NOC_WW  = np.loadtxt(open('Data/Generalisering/RTX/Adv_NOC_WW.txt'),       delimiter='\t', skiprows=1, unpack=True)
S10_NOC_WW  = np.loadtxt(open('Data/Generalisering/old/Simple10_NOC_WW.txt'),  delimiter='\t', skiprows=1, unpack=True)
S10_WC_WW   = np.loadtxt(open('Data/Generalisering/old/Simple10_WC_WW.txt'),   delimiter='\t', skiprows=1, unpack=True)
Adv_WC_NOW  = np.loadtxt(open('Data/Generalisering/RTX/Adv_WC_NOW.txt'),       delimiter='\t', skiprows=1, unpack=True)
Adv_NOC_NOW = np.loadtxt(open('Data/Generalisering/RTX/Adv_NOC_NOW.txt'),      delimiter='\t', skiprows=1, unpack=True)
S10_NOC_NOW = np.loadtxt(open('Data/Generalisering/old/Simple10_NOC_NOW.txt'), delimiter='\t', skiprows=1, unpack=True)
S10_WC_NOW  = np.loadtxt(open('Data/Generalisering/old/Simple10_WC_NOW.txt'),  delimiter='\t', skiprows=1, unpack=True)
S20_NOC_NOW = np.loadtxt(open('Data/Generalisering/old/Simple20_NOC_NOW.txt'), delimiter='\t', skiprows=1, unpack=True)
S20_WC_NOW  = np.loadtxt(open('Data/Generalisering/old/Simple20_WC_NOW.txt'),  delimiter='\t', skiprows=1, unpack=True)





#Angle_dict["combined gain list"][0][0][0] # [run id (10/20/30 kasser)][phi/theta][valgte grad][plads i array]
                    


@collection.plot_figure(only_build_this = False)
def Comparison_of_models_Without_Case():
    fig, axs = plt.subplots(2,4)

    with open(r"C:\Users\ndrazzar\Documents\GitHub\figure_tool\Data\Generalisering\dictionaries\uden_case.pkl", "rb") as pkl_to_load:
        Angle_dict = pickle.load(pkl_to_load)

    print(Angle_dict.keys())

    for i in range(4):
        
        for k in range(4):
            if i ==0:
                if k == 3:
                    #axs[0,i].title.set_text(f'Phi {k*45}')
                    axs[0,i].plot(Angle_dict["combined gain list"][k][0][i], label=f'RTX model without case ')
                    axs[0,i].grid(True)
                else:
                    axs[0,i].title.set_text(f'Phi 0')
                    axs[0,i].plot(Angle_dict["combined gain list"][k][0][i], label=f'Simple model {(k+1)*10} without case')
                    axs[0,i].grid(True)
            else:
                axs[0,i].title.set_text(f'Phi {i*45}')
                axs[0,i].plot(Angle_dict["combined gain list"][k][0][i])
                axs[0,i].grid(True)
    for i in range(4):
        for k in range(4):
            axs[1,i].title.set_text(f'Theta {i*45}')
            axs[1,i].plot(Angle_dict["combined gain list"][k][1][i])
            axs[1,i].grid(True)

                
    #plt.title("Phi")
    #plt.xlabel('Degree')
    #plt.ylabel('Gain')
    #plt.title('Phi gain comparison of generalized models')
    fig.legend()
    #plt.show()
    plt.grid()   
    return fig

@collection.plot_figure(only_build_this= False)
def Comparison_of_models_With_Case():
    fig, axs = plt.subplots(2,4)

    with open(r"C:\Users\ndrazzar\Documents\GitHub\figure_tool\Data\Generalisering\dictionaries\med_case.pkl", "rb") as pkl_to_load:
        Angle_dict = pickle.load(pkl_to_load)

    print(Angle_dict["combined gain list"].shape)

    for i in range(4):
        for k in range(4):
            if i ==0:
                if k == 3:
                    #axs[0,i].title.set_text(f'Phi {k*45}')
                    axs[0,i].plot(Angle_dict["combined gain list"][k][0][i], label=f'RTX model with case')
                    axs[0,i].grid(True)
                    
                else:
                    axs[0,i].title.set_text(f'Phi 0')
                    axs[0,i].plot(Angle_dict["combined gain list"][k][0][i], label=f'Simple model {(k+1)*10} with case')
                    axs[0,i].grid(True)
                    
            else:
                axs[0,i].title.set_text(f'Phi {i*45}')
                axs[0,i].plot(Angle_dict["combined gain list"][k][0][i])
                axs[0,i].grid(True)
                
                
    for i in range(4):
        for k in range(4):
            axs[1,i].title.set_text(f'Theta {i*45}')
            axs[1,i].plot(Angle_dict["combined gain list"][k][1][i])
            axs[1,i].grid(True)
            
        

                
    #plt.title("Phi")
    #plt.xlabel('Degree')
    #plt.ylabel('Gain')
    #plt.title('Phi gain comparison of generalized models')
    fig.legend()
    #plt.show()
    return fig


@collection.plot_figure(only_build_this = False)
def Comparison_of_models_s11():
    fig, axs = plt.subplots(2,4)

    with open(r"C:\Users\ndrazzar\Documents\GitHub\figure_tool\Data\Generalisering\dictionaries\med_case.pkl", "rb") as pkl_to_load:
        Angle_dict = pickle.load(pkl_to_load)

    print(Angle_dict["combined gain list"].shape)

    for i in range(4):
        for k in range(4):
            if i ==0:
                if k == 3:
                    #axs[0,i].title.set_text(f'Phi {k*45}')
                    axs[0,i].plot(Angle_dict["combined gain list"][k][0][i], label=f'RTX model with case')
                    axs[0,i].grid(True)
                else:
                    axs[0,i].title.set_text(f'Phi 0')
                    axs[0,i].plot(Angle_dict["combined gain list"][k][0][i], label=f'Simple model {(k+1)*10} with case')
                    axs[0,i].grid(True)
            else:
                axs[0,i].title.set_text(f'Phi {i*45}')
                axs[0,i].plot(Angle_dict["combined gain list"][k][0][i])
                axs[0,i].grid(True)
    for i in range(4):
        for k in range(4):
            axs[1,i].title.set_text(f'Theta {i*45}')
            axs[1,i].plot(Angle_dict["combined gain list"][k][1][i])
            axs[1,i].grid(True)
            

                
    #plt.title("Phi")
    #plt.xlabel('Degree')
    #plt.ylabel('Gain')
    #plt.title('Phi gain comparison of generalized models')
    fig.legend()
    plt.grid()  
    #plt.show()  
    return fig


@collection.plot_figure()
def Comparison_Of_Port_S11_Med():
    S11MedCase_1 = np.loadtxt(open('Data/Generalisering/s11/S11_MedCase_1.txt'), delimiter='\t', skiprows=1, unpack=True)
    S11MedCase_2 = np.loadtxt(open('Data/Generalisering/s11/S11_MedCase_2.txt'), delimiter='\t', skiprows=1, unpack=True)
    S11MedCase_3 = np.loadtxt(open('Data/Generalisering/s11/S11_MedCase_3.txt'), delimiter='\t', skiprows=1, unpack=True)
    S11MedCase_4 = np.loadtxt(open('Data/Generalisering/s11/S11_MedCase_4.txt'), delimiter='\t', skiprows=1, unpack=True)
    fig, ax = plt.subplots()   
    ax.plot(S11MedCase_1[0], S11MedCase_1[1], label='Simple Model 10 With Case')
    ax.plot(S11MedCase_2[0], S11MedCase_2[1], label='Simple Model 20 With Case')   
    ax.plot(S11MedCase_3[0], S11MedCase_3[1], label='Simple Model 30 With Case')
    ax.plot(S11MedCase_4[0], S11MedCase_4[1], label='Simple Model RTX With Case')   
    plt.xlabel('Frequency [MHz]')
    plt.ylabel('S1,1 [dB]')
    plt.title('Comparison of S1,1 parameters in Generalization')
    plt.legend()
    plt.grid()
    return fig


@collection.plot_figure(only_build_this = True)
def Comparison_Of_Port_S11_Uden():
    S11UdenCase_1 = np.loadtxt(open('Data/Generalisering/s11/S11_UdenCase_1.txt'), delimiter='\t', skiprows=1, unpack=True)
    S11UdenCase_2 = np.loadtxt(open('Data/Generalisering/s11/S11_UdenCase_2.txt'), delimiter='\t', skiprows=1, unpack=True)
    S11UdenCase_3 = np.loadtxt(open('Data/Generalisering/s11/S11_UdenCase_3.txt'), delimiter='\t', skiprows=1, unpack=True)
    S11UdenCase_4 = np.loadtxt(open('Data/Generalisering/s11/S11_UdenCase_4.txt'), delimiter='\t', skiprows=1, unpack=True)
    fig, ax = plt.subplots()     
    ax.plot(S11UdenCase_1[0], S11UdenCase_1[1], label='Without Case 10')
    ax.plot(S11UdenCase_2[0], S11UdenCase_2[1], label='Without Case 20')   
    ax.plot(S11UdenCase_3[0], S11UdenCase_3[1], label='Without Case 30')
    ax.plot(S11UdenCase_4[0], S11UdenCase_4[1], label='Without Case RTX')
    plt.xlabel('Frequency [MHz]')
    plt.ylabel('S1,1 [dB]')
    plt.title('Comparison of S1,1 parameters without case')
    plt.legend()
    plt.grid()
    plt.show()
    return fig