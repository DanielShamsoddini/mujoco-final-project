import random
import numpy

class NEURALNETWORK:
    def __init__(self, size):
        self.levelsOfNeurons = 3
        self.weights= [[random.uniform(-0.01,0.01) for a in range(size)] for a in range(self.levelsOfAbstraction)]

    def returnValue(self, data, level=0):
        motorvals = numpy.zeros(data.ctrl.shape)
        for a in range(data.ctrl.shape[0]):
            for b in range(4):
                motorvals[a]+= float(data.sensor("test"+str(b+1)).data.copy())*self.weights[a+b]
        return self.returnValue(data, )