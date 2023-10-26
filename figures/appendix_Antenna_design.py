from figurelib.figure import FigureCollection
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle
from figures.cst_loader import load_cst_filePOLAR, load_cst_file



collection = FigureCollection("Antenna_design")

@collection.plot_figure()
def MIFA_s11():
    data = np.loadtxt(open('Data/MIFA_s11_data.txt'), delimiter='\t', skiprows=1, unpack=True)
    fig, ax = plt.subplots()    
    ax.plot(data[0], data[1])    
    plt.xlabel('Frequency [MHz]')
    plt.ylabel('S1,1 [dB]')
    plt.title('S1,1 of MIFA antenna')
    plt.grid()
    return fig


@collection.plot_figure(only_build_this=False)
def circular_wire_antenna_s11():   
    with open('Data/appendix_circular_wire_antenna.pkl', 'rb') as pkl_path: #Dump the pickle file at the given file path
        file_data = pickle.load(pkl_path)
    fig, ax = plt.subplots()    
    frequency = np.arange(500,3001,2.5)

    #ax.plot(data[0], dat
    # a[1])  
    for i in range(0,200):
        if (np.mod(i+1,16) == 0):
            plt.plot(frequency,file_data['S1,1'][i],label=
            f"h = {abs(file_data['Parameter combination'][i,0])}, wr = {file_data['Parameter combination'][i,1]}") # , cr = {file_data['Parameter combination'][i,2]}
    plt.legend()
    plt.xlabel('Frequency [MHz]')
    plt.ylabel('S1,1 [dB]')
    plt.title('S1,1 of Circular Wire Antenna')
    plt.grid()
    #plt.show()
    return fig 

@collection.plot_figure(only_build_this=False)
def IFA_for_appendix():   
    with open('Data/appendix_circular_wire_antenna.pkl', 'rb') as pkl_path: #Dump the pickle file at the given file path
        file_data = pickle.load(pkl_path)
    fig, ax = plt.subplots()    
    frequency = np.arange(500,3001,2.5)

    #ax.plot(data[0], dat
    # a[1])  
    for i in range(0,200):
        if (np.mod(i+1,16) == 0):
            plt.plot(frequency,file_data['S1,1'][i],label=
            f"h = {abs(file_data['Parameter combination'][i,0])}, wr = {file_data['Parameter combination'][i,1]}") # , cr = {file_data['Parameter combination'][i,2]}
    plt.legend()
    plt.xlabel('Frequency [MHz]')
    plt.ylabel('S1,1 [dB]')
    plt.title('S1,1 of Circular Wire Antenna')
    plt.grid()
    return fig 

@collection.plot_figure(only_build_this=False)
def MIFA_for_appendix():   
    with open('Data/MIFA_res.pkl', 'rb') as pkl_path: #Dump the pickle file at the given file path
        file_data = pickle.load(pkl_path)
        
    fig, ax = plt.subplots()    
    frequency = np.arange(500,5001,4.5)
    for i in range(len(file_data['Parameter combination'])):
        plt.plot(frequency,file_data['S1,1'][i],label=f"L = {file_data['Parameter combination'][i]}")
    
    plt.legend(ncol = 2)
    plt.xlabel('Frequency [MHz]')
    plt.ylabel('S1,1 [dB]')
    plt.title('S1,1 of MIFA Antenna')
    plt.grid()
    return fig


@collection.plot_figure(only_build_this=False)
def IFA_for_appendix():   
    with open('Data/appendix_davidIFA.pkl', 'rb') as pkl2_path: #Dump the pickle file at the given file path
        file_data = pickle.load(pkl2_path)
    fig, ax = plt.subplots()    
    frequency = np.arange(500,3001,2.5)

    for i in range(0,30):
        if (np.mod(i,6) == 0):
            plt.plot(frequency,file_data['S1,1'][i],label=
          # two variables:
            f"H = {file_data['Parameter combination'][i,0]}, L = {25-(file_data['Parameter combination'][i,1])}")
          # three variables:
          #f"diff = {file_data['Parameter combination'][i,0]}| thickness = {file_data['Parameter combination'][i,1]} | radius = {file_data['Parameter combination'][i,2]}")

    plt.legend()
    plt.xlabel('Frequency [MHz]')
    plt.ylabel('S1,1 [dB]')
    plt.title('S1,1 of IFA')
    plt.grid()
    #plt.show()
    return fig 
