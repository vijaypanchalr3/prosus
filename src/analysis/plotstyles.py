import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
plt.rcParams['text.usetex'] = True
plt.rcParams.update({"font.size": 12})

def scatter_with_hist(data1, data2, label1="data1", label2="data2", ylabel="Y",savefile=None, suptitle=None, transparent=False, dpi=600)->None:
    facecolor = ["cyan", "orange"]
    edgecolor = ["white", "white"]
    mean1 = np.mean(data1)
    mean2 = np.mean(data2)

    # spread percentile
    percentile1 = np.percentile(data1, [5,95])
    percentile2 = np.percentile(data2, [5,95])
    
    
    # Start with a square Figure.
    fig = plt.figure(figsize=(6, 6))
    gs = fig.add_gridspec(1, 2,  width_ratios=(10, 4),
                      left=0.1, right=0.9, bottom=0.1, top=0.9,
                      wspace=0.0, hspace=0.05)
    
    if suptitle==None:
        pass
    else:
        fig.suptitle(r'\textbf{%s}'%suptitle)

        
    # Create the Axes.
    ax = fig.add_subplot(gs[0, 0])
    axhist = fig.add_subplot(gs[0, 1], sharey=ax)   
    axhist.tick_params(axis="y", labelbottom=False)    
    ylim = [np.min([np.min(data1),np.min(data2)]), np.max([np.max(data1), np.max(data2)])]
    ax.set_xlim(0,10000)
    ax.set_ylim(ylim[0],ylim[1])

    ax.set_ylabel(r'%s'%ylabel)
    z1 =4
    z2 =4
    if len(data1)<len(data2):
        z1=5

    
    # the scatter plot:
    ax.scatter(np.arange(1, len(data1)+1, 1), data1, 
               s=20,
               ec=facecolor[0],
               fc=edgecolor[0], 
               lw=0.5,
               label=label1,
               alpha=0.7,
               zorder=z1)
    ax.scatter(np.arange(1, len(data2)+1, 1), data2,
               s=20, 
               ec=facecolor[1], 
               fc=edgecolor[1],
               lw=0.5,
               label=label2,
               alpha=0.7,
               zorder=z2)
    
    ax.annotate(mean1, xy=(4000, mean1), xytext=(5000, mean1-(np.abs(ylim[1]-ylim[0])/10)),
            arrowprops=dict(facecolor='black',width=.8, headwidth=8, headlength=8), zorder=500)
    
    ax.annotate(mean2, xy=(4000, mean2), xytext=(5000, mean2+(np.abs(ylim[1]-ylim[0])/10)),
            arrowprops=dict(facecolor='black', width=.8, headwidth=8, headlength=8), zorder=500)
    


    ax.axhline(mean1, color="#000000", linestyle="--",zorder=60)
    ax.axhline(mean2, color="#000000", linestyle="--",zorder=60)
    
    ax.add_patch(Rectangle([-650,percentile1[0]], len(data1)+2000, np.abs(percentile1[1]-percentile1[0]),
                            fill=True,
                            edgecolor="#000000",
                            facecolor="#555555",
                            alpha=0.3,
                            zorder=50))
    ax.add_patch(Rectangle([-650,percentile2[0]], len(data2)+2000, np.abs(percentile2[1]-percentile2[0]),
                            fill=True,
                            edgecolor="#000000",
                            facecolor="#444444",
                            alpha=0.3,
                            zorder=50))
    
    ax.add_patch(Rectangle([-650,np.min(data1)], len(data1)+2000, np.abs(np.max(data1)-np.min(data1)),
                            fill=True,
                            facecolor="#111151",
                            alpha=0.08,
                            zorder=49))
    ax.add_patch(Rectangle([-650,np.min(data2)], len(data2)+2000, np.abs(np.max(data2)-np.min(data2)),
                            fill=True,
                            facecolor="#111151",
                            alpha=0.08,
                            zorder=49))

    axhist.axhline(mean1, 
                   color="#000000", 
                   linestyle="--",
                   zorder=60)
    axhist.axhline(mean2, 
                   color="#000000", 
                   linestyle="--",
                   zorder=60)
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xticklabels([])

    
    axhist.hist(data1, bins=np.linspace(np.min(data1), np.max(data1), 50), 
                facecolor=facecolor[0], 
                edgecolor=edgecolor[0], 
                linewidth=0.0,
                orientation='horizontal',
                alpha=1,
                zorder=z1)
    axhist.hist(data2, bins=np.linspace(np.min(data2), np.max(data2), 50), 
                facecolor=facecolor[1], 
                edgecolor=edgecolor[1], 
                linewidth=0.0,
                orientation='horizontal',
                alpha=1,
                zorder=z2)
    
    
    # axhist.spines["right"].set_visible(False)
    axhist.spines["top"].set_visible(False)
    axhist.spines["bottom"].set_visible(False)
    axhist.set_xticks([])
    axhist.yaxis.tick_right()
    ax.legend()
    if savefile == None:
        plt.show()
        pass
    else:
        plt.savefig(savefile, transparent=transparent, dpi=dpi)
        pass
    
    