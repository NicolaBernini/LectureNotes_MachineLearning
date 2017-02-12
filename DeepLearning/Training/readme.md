
# Overview 

The Problem of Training a Deep Neural Networks (DNN) essentially involves the Solution of an Optimization Problem regarding a Cost Function with huge number of parameters 

Different Optimization Strategies exist 
- Deterministic Global Optimization Techniques 
- Gradient Descent Techniques 

# Training Algos 

## Deterministic Global Optimization Techniques 

This Class of Techniques is essentially aimed at performing a systematic exploration of the State Space exploting some particular assumed properties of the Cost Function. 

- Pro 
  - Assumption Properties can be matched with proper Network Design (e.g. careful choice of Neuron Transfer Function, ...)
- Con 
  - No Scalability: the Computational Complexity grows explonentially with the Number of Params 


## Gradient based Techniques 

This Class of Techniques is essentially iteratively following the local gradient towards the closest minimum also using some kind of noise to avoid getting stuck into local minima and aiming for better or global minimum. The gradient is basically the first order derivative which is typically not so computationally expensive 

- Pro 
  - Scalability: can be used on big networks (i.e. more than 1 million params) 
- Con 
  - Non deterministic: depends on the starting point, makes use of noise 
  - Needs meta params tuning: learning step, noise temperature, ... 

Examples 
- Backpropagation Algo 



# Issues 

## Exploding and Vanishing Gradient 

The Gradient of the Loss Function depends on the Neurons Transfer Function (NTF) definition 

The presence of "Non Linear Saturating Transfer Function" (NLSTF) could produce very big or very little gradient values at training time, producing the so called phenomena of Exploding and Vanishing Gradient respectively. 

The probability of this phenomenon grows with the Network Depth hence it is a common issue in the Deep Learning context 

Different Solutions could be used 











