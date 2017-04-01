
import numpy as np
# ELEMENT Training Set Definer 
def do_TrainingSetDefiner(): 
    x = np.matrix('0.1;0.25;0.5;0.75;1')
    y = np.matrix('0;0;0;0;0')
    return x,y

# ELEMENT Transfer Function Definer 
def sigmoid(x):
    return np.matrix(1.0 / (1.0 + np.exp(-x)))

# ELEMENT Neuron Runner 
def do_NeuronRunner(x,w,b,tf): 
    return tf(x*w+b)

params = dict()
params['n1'] = dict()
params['n1']['w'] = 1
params['n1']['b'] = 0
params['n1']['tf'] = sigmoid

def do_NetworkRunner(x, params): 
    return do_NeuronRunner(x, params['n1']['w'], params['n1']['b'], params['n1']['tf'])

# ELEMENT Cost Computer 
def do_cost_computer(X, y, weight):
    nn_output = run(X,weight)
    m = X.shape[0] #num training examples, 2
    return np.sum(np.square(nn_output - y)) / m

print "Test Neuron = " + str(do_NeuronRunner(1,1,1,sigmoid))

ts_x, ts_y = do_TrainingSetDefiner()
print "Test Network = " + str(do_NetworkRunner(ts_x, params))

