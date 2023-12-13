from figurelib.figure import FigureCollection
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle
from figures.cst_loader import load_cst_filePOLAR, load_cst_file

collection = FigureCollection("Simple model") # Name of the collection

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
Adv_WC_WW = np.loadtxt(open('Data/Generalisering/Adv_WC_WW.txt'), delimiter='\t', skiprows=1, unpack=True)
Adv_NOC_WW = np.loadtxt(open('Data/Generalisering/Adv_NOC_WW.txt'), delimiter='\t', skiprows=1, unpack=True)
S10_NOC_WW = np.loadtxt(open('Data/Generalisering/Simple10_NOC_WW.txt'), delimiter='\t', skiprows=1, unpack=True)
S10_WC_WW = np.loadtxt(open('Data/Generalisering/Simple10_WC_WW.txt'), delimiter='\t', skiprows=1, unpack=True)
Adv_WC_NOW = np.loadtxt(open('Data/Generalisering/Adv_WC_NOW.txt'), delimiter='\t', skiprows=1, unpack=True)
Adv_NOC_NOW = np.loadtxt(open('Data/Generalisering/Adv_NOC_NOW.txt'), delimiter='\t', skiprows=1, unpack=True)
S10_NOC_NOW = np.loadtxt(open('Data/Generalisering/Simple10_NOC_NOW.txt'), delimiter='\t', skiprows=1, unpack=True)
S10_WC_NOW = np.loadtxt(open('Data/Generalisering/Simple10_WC_NOW.txt'), delimiter='\t', skiprows=1, unpack=True)
S20_NOC_NOW = np.loadtxt(open('Data/Generalisering/Simple20_NOC_NOW.txt'), delimiter='\t', skiprows=1, unpack=True)
S20_WC_NOW = np.loadtxt(open('Data/Generalisering/Simple20_WC_NOW.txt'), delimiter='\t', skiprows=1, unpack=True)

@collection.plot_figure()
def Comparison_Of_models_wire():
    fig, ax, = plt.subplots()   
    ax.plot(Adv_WC_WW[0], Adv_WC_WW[1], label='Advanced model With CASE')
    ax.plot(Adv_NOC_WW[0], Adv_NOC_WW[1], label='Advanced model WIRE')
    ax.plot(S10_NOC_WW[0], S10_NOC_WW[1], label='Simple model 10 NO CASE WIRE')
    ax.plot(S10_WC_WW[0], S10_WC_WW[1], label='Simple model 10 CASE WIRE')
    plt.title("With Wire")
    plt.xlabel('Frequency [MHz]')
    plt.ylabel('S1,1 [dB]')
    plt.title('Comparison of S1,1 parameters based on model')
    plt.legend()
    plt.grid()
    return fig

@collection.plot_figure(only_build_this=True)
def Comparison_Of_models_case():
    fig, ax, = plt.subplots()   
    ax.plot(Adv_WC_NOW[0], Adv_WC_NOW[1], label='Advanced model WITH CASE')
    ax.plot(Adv_NOC_NOW[0], Adv_NOC_NOW[1], label='Advanced model NO CASE')
    #ax.plot(S10_NOC_NOW[0], S10_NOC_NOW[1], label='Simple model 10 NO CASE')
    ax.plot(S10_WC_NOW[0], S10_WC_NOW[1], label='Simple model 10 WITH CASE')
    #ax.plot(S20_NOC_NOW[0], S20_NOC_NOW[1], label='Simple model 20 NO CASE')
    ax.plot(S20_WC_NOW[0], S20_WC_NOW[1], label='Simple model 20 WITH CASE')
    plt.title("Without Wire")
    plt.xlabel('Frequency [MHz]')
    plt.ylabel('S1,1 [dB]')
    plt.title('Comparison of S1,1 parameters based on model')
    plt.legend()
    plt.grid()
    plt.show()
    return fig

