from figurelib.figure import FigureCollection
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle
from figures.cst_loader import load_cst_filePOLAR, load_cst_file

collection = FigureCollection("Simple model") # Name of the collection


# @collection.plot_figure()
# def Comparison_Of_Phi():
#     On_bat = np.loadtxt(open('Data\Antenna_Port_Bat.txt'), delimiter='\t', skiprows=1, unpack=True)
#     fig, ax = plt.subplots()   
#     ax.plot(On_PCB[0], On_PCB[1], label='On PCB')
#     ax.plot(On_bat[0], On_bat[1], label='On Battery')
#     plt.xlabel('Frequency [MHz]')
#     plt.ylabel('S1,1 [dB]')
#     plt.title('Comparison of S1,1 parameters based on port placement')
#     plt.legend()
#     plt.grid()
#     return fig

# @collection.plot_figure()
# def Comparison_Of_Theta():
#     On_PCB = np.loadtxt(open('Data\Antenna_port_on_PCB.txt'), delimiter='\t', skiprows=1, unpack=True)
#     On_bat = np.loadtxt(open('Data\Antenna_Port_Bat.txt'), delimiter='\t', skiprows=1, unpack=True)
#     fig, ax = plt.subplots()   
#     ax.plot(On_PCB[0], On_PCB[1], label='On PCB')
#     ax.plot(On_bat[0], On_bat[1], label='On Battery')
#     plt.xlabel('Frequency [MHz]')
#     plt.ylabel('S1,1 [dB]')
#     plt.title('Comparison of S1,1 parameters based on port placement')
#     plt.legend()
#     plt.grid()
#     return fig

# @collection.plot_figure()
# def Comparison_Of_Port_placement():
#     On_PCB = np.loadtxt(open('Data\Antenna_port_on_PCB.txt'), delimiter='\t', skiprows=1, unpack=True)
#     On_bat = np.loadtxt(open('Data\Antenna_Port_Bat.txt'), delimiter='\t', skiprows=1, unpack=True)
#     fig, ax = plt.subplots()   
#     ax.plot(On_PCB[0], On_PCB[1], label='On PCB')
#     ax.plot(On_bat[0], On_bat[1], label='On Battery')
#     plt.xlabel('Frequency [MHz]')
#     plt.ylabel('S1,1 [dB]')
#     plt.title('Comparison of S1,1 parameters based on port placement')
#     plt.legend()
#     plt.grid()
#     return fig

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

phi_list = []
theta_list = []


#Angle_dict["combined gain list"][0][0][0] # [run id (10/20/30 kasser)][phi/theta][valgte grad][plads i array]
                    


@collection.plot_figure(only_build_this = False)
def Comparison_of_models_Without_Case():
    fig, axs = plt.subplots(2,4)

    with open('Data/Generalisering/dictionaries/uden_case.pkl', "rb") as pkl_to_load:
        Angle_dict = pickle.load(pkl_to_load)

    #print(Angle_dict.keys())

    for i in range(4):
        
        for k in range(4):
            if i ==0:
                if k == 2:
                    #axs[0,i].title.set_text(f'Phi {k*45}')
                    axs[0,i].plot(Angle_dict["combined gain list"][k][0][i], label=f'Cuboid 32, Case omitted')
                    axs[0,i].grid(True)
                    axs[0,i].set_xticks([180])
                elif k == 3:
                    #axs[0,i].title.set_text(f'Phi {k*45}')
                    axs[0,i].plot(Angle_dict["combined gain list"][k][0][i], label=f'RTX, Case omitted ')
                    axs[0,i].grid(True)
                else:
                    axs[0,i].title.set_text(f'Phi 0')
                    axs[0,i].plot(Angle_dict["combined gain list"][k][0][i], label=f'Cuboid {(k+1)*10}, Case omitted')
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
            axs[0,i].set_xticks([180])

                
    #plt.title("Phi")
    #plt.xlabel('Degree')
    #plt.ylabel('Gain')
    #plt.title('Phi gain comparison of generalized models') 
    fig.suptitle('Comparison of Phi and Theta, Case Omitted')  
    plt.setp(axs[-1, :], xlabel='Degree')
    plt.setp(axs[:, 0], ylabel='Gain [dBi]')        
    fig.legend(bbox_to_anchor=(-2.95,0.1),bbox_transform = plt.gca().transAxes, loc = 'lower right', fontsize='small' )
    plt.grid(True) 
    #plt.show()
  
    return fig

@collection.plot_figure(only_build_this= False)
def Comparison_of_models_With_Case():
    fig, axs = plt.subplots(2,4)

    with open('Data/Generalisering/dictionaries/med_case.pkl', "rb") as pkl_to_load:
        Angle_dict = pickle.load(pkl_to_load)

    #print(Angle_dict["combined gain list"].shape)

    for i in range(4):
        for k in range(4):
            if i ==0:
                if k == 2:    
                    axs[0,i].title.set_text(f'Phi 0')
                    axs[0,i].plot(Angle_dict["combined gain list"][k][0][i], label=f'Cuboid ver 32')
                    axs[0,i].grid(True)
                elif k == 3:
                    #axs[0,i].title.set_text(f'Phi {k*45}')
                    axs[0,i].plot(Angle_dict["combined gain list"][k][0][i], label=f'RTX')
                    axs[0,i].grid(True)
                else:
                    axs[0,i].title.set_text(f'Phi 0')
                    axs[0,i].plot(Angle_dict["combined gain list"][k][0][i], label=f'Cuboid ver {(k+1)*10}')
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
    plt.grid(True)
    fig.suptitle('Radiation Pattern') 
    fig.legend(bbox_to_anchor=(-3.5,0.25),bbox_transform = plt.gca().transAxes, loc = 'lower right' )
    #plt.show()
    return fig


@collection.plot_figure(only_build_this = False)
def Comparison_of_models_s11():
    fig, axs = plt.subplots(2,4)

    with open('Data/Generalisering/dictionaries/med_case.pkl', "rb") as pkl_to_load:
        Angle_dict = pickle.load(pkl_to_load)

    #print(Angle_dict["combined gain list"].shape)

    for i in range(4):
        for k in range(4):
            if i ==0:
                if k == 2:
                    axs[0,i].title.set_text(f'Phi 0')
                    axs[0,i].plot(Angle_dict["combined gain list"][k][0][i], label=f'Cuboid ver 32')
                    axs[0,i].grid(True)


                elif k == 3:
                    #axs[0,i].title.set_text(f'Phi {k*45}')
                    axs[0,i].plot(Angle_dict["combined gain list"][k][0][i], label=f'RTX')
                    axs[0,i].grid(True)
                else:
                    axs[0,i].title.set_text(f'Phi 0')
                    axs[0,i].plot(Angle_dict["combined gain list"][k][0][i], label=f'Cuboid ver {(k+1)*10}')
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
            
    # print(np.mean((Angle_dict["combined gain list"][3][0][i]) - S11MedCase_5)**2))            

    



    #plt.title("Phi")
    #plt.xlabel('Degree')
    #plt.ylabel('Gain')
    #plt.title('Phi gain comparison of generalized models')
    fig.suptitle('S1,1 Parameters') 
    
    fig.legend(bbox_to_anchor=(-3.5,0.25),bbox_transform = plt.gca().transAxes, loc = 'lower right' )
    plt.grid(True)  
    #plt.show()
 
    return fig


@collection.plot_figure(only_build_this = False)
def Comparison_Of_Port_S11_Med():
    S11MedCase_1 = np.loadtxt(open('Data/Generalisering/s11/S11_MedCase_1.txt'), delimiter='\t', skiprows=1, unpack=True)
    S11MedCase_2 = np.loadtxt(open('Data/Generalisering/s11/S11_MedCase_2.txt'), delimiter='\t', skiprows=1, unpack=True)
    S11MedCase_3 = np.loadtxt(open('Data/Generalisering/s11/S11_MedCase_3.txt'), delimiter='\t', skiprows=1, unpack=True)
    S11MedCase_4 = np.loadtxt(open('Data/Generalisering/s11/S11_MedCase_4.txt'), delimiter='\t', skiprows=1, unpack=True)
    S11MedCase_5 = np.loadtxt(open('Data/Generalisering/s11/S11_MedCase_5.txt'), delimiter='\t', skiprows=1, unpack=True)
    fig, ax = plt.subplots()   
    #ax.plot(S11MedCase_1[0], S11MedCase_1[1], label='Cuboid ver 10')
    #ax.plot(S11MedCase_2[0], S11MedCase_2[1], label='Cuboid ver 20')   
    ax.plot(S11MedCase_3[0], S11MedCase_3[1], label='RTX')
    ax.plot(S11MedCase_4[0], S11MedCase_4[1], label='Voxel 1mm')
    ax.plot(S11MedCase_5[0], S11MedCase_5[1], label='Cuboid 32')    
    plt.xlabel('Frequency [MHz]')
    plt.ylabel('S1,1 [dB]')
    plt.title('S1,1 Parameters')
    fig.legend(bbox_to_anchor=(0.3,0.1),bbox_transform = plt.gca().transAxes, loc = 'lower right' )
    plt.grid(True)
    #plt.show()

    return fig


@collection.plot_figure(only_build_this = False)
def Comparison_Of_Port_S11_Uden():
    S11UdenCase_1 = np.loadtxt(open('Data/Generalisering/s11/S11_UdenCase_1.txt'), delimiter='\t', skiprows=1, unpack=True)
    S11UdenCase_2 = np.loadtxt(open('Data/Generalisering/s11/S11_UdenCase_2.txt'), delimiter='\t', skiprows=1, unpack=True)
    S11UdenCase_3 = np.loadtxt(open('Data/Generalisering/s11/S11_UdenCase_3.txt'), delimiter='\t', skiprows=1, unpack=True)
    S11UdenCase_4 = np.loadtxt(open('Data/Generalisering/s11/S11_UdenCase_4.txt'), delimiter='\t', skiprows=1, unpack=True)
    fig, ax = plt.subplots()     
    ax.plot(S11UdenCase_1[0], S11UdenCase_1[1], label='Cuboid ver 10, Case Omitted')
    ax.plot(S11UdenCase_2[0], S11UdenCase_2[1], label='Cuboid ver 20, Case Omitted')   
    ax.plot(S11UdenCase_3[0], S11UdenCase_3[1], label='Cuboid ver 32, Case Omitted')
    ax.plot(S11UdenCase_4[0], S11UdenCase_4[1], label='RTX, Case Omitted')
    plt.xlabel('Frequency [MHz]')
    plt.ylabel('S1,1 [dB]')
    plt.title('Comparison of S1,1 Parameters, Case Omitted')
    #fig.legend()
    fig.legend(bbox_to_anchor=(0.3,0.1),bbox_transform = plt.gca().transAxes, loc = 'lower right' )
    plt.grid(True)
    #plt.show()
    return fig


# @collection.plot_figure(only_build_this = True)

# def Comparison_Of_32_And_RTX():
#     with open('Data/Generalisering/dictionaries/uden_case.pkl', "rb") as pkl_to_load:
#         Angle_dict = pickle.load(pkl_to_load)

#     axs[0,i].title.set_text(f'Phi 0')
#     axs[0,i].plot(Angle_dict["combined gain list"][k][0][i], label=f'Cuboid ver 32')
#     axs[0,i].grid(True)
#     S11UdenCase_1 = np.loadtxt(open('Data/Generalisering/s11/S11_UdenCase_1.txt'), delimiter='\t', skiprows=1, unpack=True)
#     S11UdenCase_2 = np.loadtxt(open('Data/Generalisering/s11/S11_UdenCase_2.txt'), delimiter='\t', skiprows=1, unpack=True)
#     S11UdenCase_3 = np.loadtxt(open('Data/Generalisering/s11/S11_UdenCase_3.txt'), delimiter='\t', skiprows=1, unpack=True)
#     S11UdenCase_4 = np.loadtxt(open('Data/Generalisering/s11/S11_UdenCase_4.txt'), delimiter='\t', skiprows=1, unpack=True)
#     fig, ax = plt.subplots()     
#     ax.plot(S11UdenCase_1[0], S11UdenCase_1[1], label='Cuboid ver 10, Case Omitted')
#     ax.plot(S11UdenCase_2[0], S11UdenCase_2[1], label='Cuboid ver 20, Case Omitted')   
#     ax.plot(S11UdenCase_3[0], S11UdenCase_3[1], label='Cuboid ver 32, Case Omitted')
#     ax.plot(S11UdenCase_4[0], S11UdenCase_4[1], label='RTX, Case Omitted')
#     plt.xlabel('Frequency [MHz]')
#     plt.ylabel('S1,1 [dB]')
#     plt.title('Comparison of S1,1 Parameters, Case Omitted')
#     fig.legend()
#     fig.legend(bbox_to_anchor=(0.3,0.1),bbox_transform = plt.gca().transAxes, loc = 'lower right' )
#     plt.grid(True)
#     plt.show()
#     return fig


@collection.plot_figure(only_build_this = False)
def Comparison_of_32_RTX_Voxel():
    fig, axs = plt.subplots(2,4)

    with open('Data/Generalisering/dictionaries/med_case.pkl', "rb") as pkl_to_load:
        Angle_dict = pickle.load(pkl_to_load)

    #print(Angle_dict["combined gain list"].shape)
    RTX_phi = []
    voxel_phi = []
    cuboid_phi = []
    for i in range(4):
        for k in range(2,5):
            if i ==0:



                if k == 2:
                    axs[0,i].title.set_text(f'Phi 0')
                    axs[0,i].plot(Angle_dict["combined gain list"][k][0][i], label=f'RTX')
                    axs[0,i].grid(True)
                    axs[0,i].set_xticks([180])
                    # RTX_phi.append(Angle_dict['combined gain list'][2][0][i])
                elif k == 3:
                    axs[0,i].plot(Angle_dict["combined gain list"][k][0][i], label=f'Voxel')
                    axs[0,i].grid(True)
                    # voxel_phi.append(Angle_dict['combined gain list'][3][0][i])
                    
                else:
                    axs[0,i].title.set_text(f'Phi 0')
                    axs[0,i].plot(Angle_dict["combined gain list"][k][0][i], label=f'Cuboid')
                    axs[0,i].grid(True)
                    # cuboid_phi.append(Angle_dict['combined gain list'][4][0][i])

            else:
                axs[0,i].title.set_text(f'Phi {i*45}')
                axs[0,i].plot(Angle_dict["combined gain list"][k][0][i])
                axs[0,i].grid(True)
                axs[0,i].set_xticks([180])
        RTX_phi.append(Angle_dict['combined gain list'][2][0][i])
        voxel_phi.append(Angle_dict['combined gain list'][3][0][i])
        cuboid_phi.append(Angle_dict['combined gain list'][4][0][i])
 ########### start theta for MSE ##############################3
    #RTX_theta= []
    #voxel_theta = []
    #cuboid_theta = []

    for i in range(4):
        for k in range(2,5):
            axs[1,i].title.set_text(f'Theta {i*45}')
            axs[1,i].plot(Angle_dict["combined gain list"][k][1][i])
            axs[1,i].grid(True)
            axs[1,i].set_xticks([180])
############ Append for MSE ##############################
        #RTX_theta.append(Angle_dict['combined gain list'][2][1][i])
        #voxel_theta.append(Angle_dict['combined gain list'][3][1][i])
        #cuboid_theta.append(Angle_dict['combined gain list'][4][1][i])


######################## MSE ##########################################
    #MSE_voxel_theta = [np.mean((RTX_theta[angle]-voxel_theta[angle])**2) for angle in range(4)]
    #MSE_cuboid_theta =[np.mean((RTX_theta[angle]-cuboid_theta[angle])**2) for angle in range(4)]
    #print(f'voxel MSE theta 0, 45, 90, 135')
    #print(MSE_voxel_theta)
    #print(f'Cuboid MSE theta 0, 45, 90, 135')
    #print(MSE_cuboid_theta)

    #MSE_voxel_phi = [np.mean((RTX_phi[angle]-voxel_phi[angle])**2) for angle in range(4)]
    #MSE_cuboid_phi =[np.mean((RTX_phi[angle]-cuboid_phi[angle])**2) for angle in range(4)]
    #print(f'voxel MSE phi 0, 45, 90, 135')
    #print(MSE_voxel_phi)
    #print(f'Cuboid MSE phi 0, 45, 90, 135')
    #print(MSE_cuboid_phi)
    # print(Angle_dict['combined gain list'][2][1][2])
    # print(np.asarray(RTX_theta).shape)
    # print(np.asarray(RTX_theta)[2])


    plt.grid(True)
    fig.suptitle('Radiation Pattern')
    plt.setp(axs[-1, :], xlabel='Degree')
    plt.setp(axs[:, 0], ylabel='Gain [dBi]') 
    fig.legend(bbox_to_anchor=(-3.25,0.25),bbox_transform = plt.gca().transAxes, loc = 'lower right' )
    #plt.show()
    return fig