
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager


leg_font = font_manager.FontProperties(size=12)
font = {'color':'black','size':12}

import numpy as np
import tools
import csv



class Result:

    def __init__(self)-> None:
        background1=tools.data("../data/healedbackground1.csv")
        background2=tools.data("../data/healedbackground2.csv")
        background3=tools.data("../data/background3.csv")
        background4nickel=tools.data("../data/background4wnickel.csv")
        samplefe2o3=tools.data("../data/sample1.csv")
        samplenickel=tools.data("../data/sample2nickel.csv")


        self.header = background1.header
        print(self.header)
        self.arrays_bg1 = background1.arrays
        self.arrays_bg2 = background2.arrays
        self.arrays_bg3 = background3.arrays
        self.arrays_bg4 = background4nickel.arrays
        self.arrays_s1 = samplefe2o3.arrays
        self.arrays_s2 = samplenickel.arrays
    
    def plot_hist(self,arrays,filename,title)->None:
        fig, axs = plt.subplots(2,2,squeeze=False,sharey=True)
        fig.tight_layout(h_pad=8)
        axs[0,0].hist(arrays[0],bins=100)
        axs[0,0].set_title("X values in volts")
        axs[0,1].hist(arrays[1],bins=100)
        axs[0,1].set_title("Y values in volts")
        axs[1,0].hist(arrays[2],bins=100)
        axs[1,0].set_title("R values in volts")
        axs[1,1].hist(arrays[3],bins=100)
        axs[1,1].set_title("phase in degrees")
        for i in range(2):
            for j in range(2):
                plt.setp(axs[i,j].get_xticklabels(), rotation=60, horizontalalignment='right')
        fig.suptitle(title)
        plt.subplots_adjust(top=0.85)
        plt.subplots_adjust(bottom=.15)
        fig.savefig(filename,transparent=True,format="svg")

    def write_results(self,arrays,filename,title):
        arrays.pop(0)
        print(arrays)
        exit()
        for i in range(4):
            with open(filename,"a",newline="") as file:
                writer = csv.writer(file)
                writer.writerow([title,self.header[i],np.mean(arrays[i]),np.median(arrays[i]),np.std(arrays[i]),np.var(arrays[i]), np.min(arrays[i]),np.max(arrays[i])])



MASTER = Result()
# MASTER.plot_hist(MASTER.arrays_bg1, "bg1.svg", "Background 1")
# MASTER.plot_hist(MASTER.arrays_bg2, "bg2.svg", "Background 2")
# MASTER.plot_hist(MASTER.arrays_bg3, "bg3.svg", "Background 3")
# MASTER.plot_hist(MASTER.arrays_bg4, "bg3.svg", "Background 4")
# MASTER.plot_hist(MASTER.arrays_s1, "s1.svg", "sample 1")
# MASTER.plot_hist(MASTER.arrays_s2, "s2.svg", "sample 2")
MASTER.write_results(MASTER.arrays_bg1,"result.csv","Background 1")
MASTER.write_results(MASTER.arrays_bg2,"result.csv","Background 2")
MASTER.write_results(MASTER.arrays_bg3,"result.csv","Background 3")
MASTER.write_results(MASTER.arrays_bg4,"result.csv","Background 4")
MASTER.write_results(MASTER.arrays_s1,"result.csv","Sample 1")
MASTER.write_results(MASTER.arrays_s2,"result.csv","Sample 2")