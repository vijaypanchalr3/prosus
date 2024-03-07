from pyinstro import SR830


import numpy
import sys
import time
import keyboard


class sampler:
    """
    function:   very simpler data logger for SR830
                write file, as what given from terminal or auto{number}.csv in present directory under data directory.
    limitation: too much hard coded
    """
    def __init__(self, Argument="Frequency") -> None:
        self.device = SR830()
        time.sleep(2)
        # self.device.ping()
        time.sleep(0.5)
        # print(self.device.read())
        time.sleep(2)
        self.device.longwriterow([Argument, "XinV", "YinV", "RinV", "outputphase"])

    def discrete_range(self,minimum,maximum,step):
        input()
        for voltage in numpy.arange(minimum,maximum,step):
            self.device.set_voltage(voltage)
            voltage=round(voltage,3)
            print(voltage)
            time.sleep(.5)
            for j in range(250):
                for i in range(1):
                    data = self.device.get_data_explicitly_fast()
                    self.device.longwriterow([voltage]+data)
                    # print(freq,data)
                    time.sleep(0.08)

    
    def manual(self, xmin, xmax, steps, times):
        nestedbreak = False
        distance = xmin
        print("came outside")
        while distance!=xmax:
            count=0
            print("hell")
            while count < times:
                time.sleep(.1)
                if input()=="":
                    # data1= float(self.device.get_data_explicitly(1))
                    # time.sleep(.1)
                    # data2= float(self.device.get_data_explicitly(2))
                    # time.sleep(.1)
                    # data3= float(self.device.get_data_explicitly(3))
                    # time.sleep(.1)
                    # data4= float(self.device.get_data_explicitly(4))
                    # time.sleep(.1)
                    data = self.device.get_data_explicitly_fast()
                    data = data[:-1].split(",")
                    print("distance ", distance, data)
                    self.device.longwriterow([distance]+data)
                    count+=1
                else:
                    print("continue ? ")
                    if input()=="y":
                        pass
                    else:
                        nestedbreak=True
                        break
            distance-=steps
            if nestedbreak==True:
                break

        
    def timer(self):
        for i in range(10000):
            time.sleep(.08)
            data = self.device.get_data_explicitly_fast()
            print(data)
            self.device.longwriterow(data)
    
    def partition_loop(self,minimum, maximum,partitions,timedelay=0.2):
        # time.sleep(2)
        frange = numpy.linspace(minimum, maximum,partitions)
        count = 1
        for freq in frange:
            self.device.set_frequency(freq)
            time.sleep(timedelay)
            for i in range(100):
                data = float(self.device.get_data_explicitly(3))
                self.device.longwriterow([freq,data])
                print(data)
                input()
                time.sleep(timedelay)
                if count==50:
                    input("check setup and press enter")
                    count = 1
                else:
                    count+=1

    

if __name__=="__main__":
    x = sampler()
    x.timer()
    sys.exit()