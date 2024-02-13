import csv
import re
from numpy import array,mean,abs,split,vstack,argsort,column_stack

__all__=[
    "files"
    ]

class data:
    """
    PARAMETER: filename as Relative path to __file__
    RETURN: nil
    FUNCTION: read files named filename, write other files with data
    """
    def __init__(self,filename:str,datatype=float) -> None:
        self.datatype = datatype
        self.filename = filename

        with open(filename, 'r') as newfile:
            
            self.fobject = list(csv.reader(newfile))
            
            # omit first member
            try:
                datatype(self.fobject[0][0])
                self.header = None
            except ValueError:
                self.header = self.fobject.pop(0)
                
            self.length = sum(1 for row in self.fobject)
            self.data = array(self.fobject, dtype=self.datatype)
            self.arrays = split(self.data,len(self.data[0]), axis=1)
            
    def create_empty(self,nameaddition:str="extra"):
        _finalfile = re.split("\/",self.filename)
        finalfile = re.split("\.", _finalfile[len(_finalfile)-1])
        self.finalfile = "/".join(str(_finalfile[i]) for i in range(len(_finalfile)-1))+"/"+finalfile[0]+nameaddition+finalfile[1]
    
    def write_another(self,data:list)-> None:
        with open(self.finalfile, 'wxs', newline="") as cleandata:
            writer = csv.writer(cleandata)
            writer.writerow(data)
    
    def get_mean(self):
        data = array(self.fobject)
        try:
            first_array,second_array = split(data,2,axis=1)
        except IndexError:
            print("from get_mean()::empty array from data")
            
        extra_array,_first_array,_second_array = [],[],[]
        count = 0
        _first_array.append(first_array[count][0])
        for i in range(0,len(data)):
            if first_array[i][0]==_first_array[count]:
                extra_array.append(second_array[i][0])
            else:
                _second_array.append(mean(array(extra_array,dtype=float)))
                count+=1
                _first_array.append(first_array[i][0])
                extra_array=[]

            if i==len(first_array)-1:
                _second_array.append(mean(array(extra_array,dtype=float)))

        return vstack((array(_first_array,dtype=float),array(_second_array,dtype=float))).T
        
    def sort_on_deviation(self, points=5):
        data = array(self.fobject, dtype=float)
        filtered_data=[]
        temp_erray = []
        index = float(data[0][0])
        count = 0
        for datapoint in data:
            count+=1
            if datapoint[0]==index:
                temp_erray.append(float(datapoint[1]))
            else:
                nlist = array(temp_erray,dtype=float)
                m = mean(nlist)
                sorted_deviation = argsort(abs(nlist - m))
                filtered_nlist = nlist[sorted_deviation[:points]]
                indexonelist = array([index]*points)
                final_list= column_stack((indexonelist,filtered_nlist))
                for member in final_list:
                    filtered_data.append(member)
                index = float(datapoint[0])
                temp_erray = []

            if count == len(data)-1:
                nlist = array(temp_erray,dtype=float)
                m = mean(nlist)
                sorted_deviation = argsort(abs(nlist - m))
                filtered_nlist = nlist[sorted_deviation[:points]]
                indexonelist = array([index]*points)
                final_list= column_stack((indexonelist,filtered_nlist))
                for member in final_list:
                    filtered_data.append(member)
        return array(filtered_data)
    
    def shady_plot(self, color="Blues"):
        """
        
        """
        data = array(self.fobject,dtype=float)
        
        # [here] can be better memort handling !
        common_array = [[]]
        index = float(data[0][0])
        count = 0
        for datapoint in data:
            if float(datapoint[0])==index:
                try:
                    common_array[count].append([float(datapoint[0]),float(datapoint[1])])
                    count+=1
                except IndexError:
                    common_array.append([])
                    common_array[count].append([float(datapoint[0]),float(datapoint[1])])
                    count+=1
            else:
                count=0
                index = float(datapoint[0])
        
        
        

        delete = []
        common_array.pop()
        for i in range(len(common_array)-1):    
            if len(common_array[len(common_array)-1])<len(common_array[i]):
                common_array[i].pop()
        
        common_array = array(common_array)
        
        from matplotlib import cm

        colormap = cm.get_cmap(color, len(common_array))

        return common_array,colormap

    def point_mean(self,data):
        freq = []
        vo = []
        freq.append(float(data[0][0]))
        vo.append(float(data[0][1]))
        count = 1
        for i in range(1,len(data)):
            lenth = len(freq)
            if float(data[i][0])==freq[lenth-1]:
                vo[lenth-1]+=float(data[i][1])
                count+=1
            else:
                vo[lenth-1]=vo[lenth-1]/count
                count=1
                freq.append(float(data[i][0]))
                vo.append(float(data[i][1]))
        freq.pop()
        vo.pop()
        return array(freq,dtype=float),array(vo,dtype=float)



 

if __name__=="__main__":
    print("No Error")