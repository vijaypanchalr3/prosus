import matplotlib as mpl
import matplotlib.font_manager as font_manager

mpl.rcParams['font.family']='serif'
cmfont = font_manager.FontProperties(fname=mpl.get_data_path() + 'cmr10.ttf')
mpl.rcParams['font.serif']=cmfont.get_name()
mpl.rcParams['mathtext.fontset']='cm'
mpl.rcParams['axes.unicode_minus']=False



def plot_things(ax):
    ax.yaxis.tick_right()
    ax.xaxis.tick_top()
    ax.xaxis.get_minor_locator()
    ax.grid(which="both",axis="both",color="orange",alpha=0.4)
    ax.legend()