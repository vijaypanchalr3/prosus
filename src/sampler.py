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
        
        self.device.set_frequency(minimum)
        time.sleep(.8)
        self.device.autogain()
        input()
        for freq in range(minimum,maximum,step):
            self.device.set_frequency(freq)
            print(freq)
            time.sleep(1)
            for j in range(1):
                for i in range(5):
                    print(self.device.get_data_explicitly(1))
                    data1= float(self.device.get_data_explicitly(1))
                    time.sleep(.1)
                    data2= float(self.device.get_data_explicitly(2))
                    time.sleep(.1)
                    data3= float(self.device.get_data_explicitly(3))
                    time.sleep(.1)
                    data4= float(self.device.get_data_explicitly(4))
                    time.sleep(.1)
                    self.device.longwriterow([freq,data1, data2, data3, data4])
                    # print(freq,data)
                    time.sleep(0.1)

    
    def manual(self, xmin, xmax, steps, times):
        nestedbreak = False
        distance = xmin
        print("came outside")
        while distance!=xmax:
            count=0
            print("hell")
            while count < times:
                time.sleep(.1)
                command = keyboard.wait()
                if command=="n" or command=="\n":
                    # data1= float(self.device.get_data_explicitly(1))
                    # time.sleep(.1)
                    # data2= float(self.device.get_data_explicitly(2))
                    # time.sleep(.1)
                    # data3= float(self.device.get_data_explicitly(3))
                    # time.sleep(.1)
                    # data4= float(self.device.get_data_explicitly(4))
                    # time.sleep(.1)
                    print("distance ", distance)
                    self.device.longwriterow([distance, 1, 2, 3, 4])
                    count+=1
                    distance-=steps
                elif command=="p":
                    distance-=steps
                elif command=="q":
                    nestedbreak=True
                    break
                else:
                    pass
            if nestedbreak==True:
                break

    
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
    x.manual(25,-1,0.5,3)
    sys.exit()