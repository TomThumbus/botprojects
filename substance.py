from utilities import Neuron

class Box:
    def __init__(self, things):
        self.things = []
        for thing in things:
            self.things.append(thing)

class Brain:
    def __init__(self):
        self.neurons = []
        for i in range(0, 27):
            self.neurons.append(Neuron(i))

brain = Brain()
for n in brain.neurons:
    print(n.data)