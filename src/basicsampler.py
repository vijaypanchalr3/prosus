from pyinstro import SR830
from pyinstro import coloroutput



import numpy
import time


class Basic_Sampler:
    """
    
    """
    def __init__(self) -> None:
        self.device = SR830()

        self.device.ping()
        time.sleep(1)
        coloroutput.attentive(self.device.read())
        time.sleep(1)

    def loop(self, number)->None:
        fmin = self.device.fmin()
        fmax = self.device.fmax()
        partitions = self.device.get_partitions()
        freqrange = numpy.linspace(fmin,fmax,partitions)
        for freq in freqrange:
            coloroutput.attentive("frequency set to: "+"{:.4E}".format(freq))
            self.device.set_frequency(freq)
            input()
            for i in range(number):
                data = self.device.get_data_explicitly(3)
                self.device.longwriterow([freq, data])
                time.sleep(0.1)

    
    
    
basicsampler = Basic_Sampler()
basicsampler.loop(2)

        