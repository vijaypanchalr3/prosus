import numpy as np
def shady_plot(fobject):
    data = np.array(fobject,dtype=float)
    common_array = [[]]
    index = float(data[0][0])
    count = 0
    for datapoint in data:
        if float(datapoint[0])==index:
            try:
                common_array[count].append(np.array([float(datapoint[0]),float(datapoint[1])],dtype=float))
                count+=1
            except IndexError:
                common_array.append([])
                common_array[count].append([float(datapoint[0]),float(datapoint[1])])
                count+=1
        else:
            count=0
            index = float(datapoint[0])
            
    return common_array





if __name__=="__main__":
    import tools

    file = tools.files("../data/final1.csv")
    data= shady_plot(file.fobject)
    print(np.array(data))
