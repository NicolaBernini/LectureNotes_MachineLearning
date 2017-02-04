
# Overview 

The Kalman Filter is an Recursive Bayesian Filter 

**What problem does it solve?**

- It is aimed at solving the "Object Design Problem" or "Black Box State Estimation Problem" 
  - it consists of estimating the internal state of an unknown system, just looking at its Input and Output 


**How does the system evolve?**

- As the system is a Black Box, we don't actually know anything about its "inside behaviour" however we can guess or better **assume** a **model** on the basis of some contextual knowledge 
- E.g. Considering the motion of an object, we can take from Physics the appropriate "Law of Motions" 


**Is the evolution deterministic?**

- Oftentimes our model is only precise at some extent: it can explain/predcit the evolution of the system only up to a certain precision
  - The reasons are typically many : e.g. a model typically focuses just on the main dynamic, taking into account only a subset of the variables 
- We should then model the unexplained/unpredicted evolution with a **Noise Term** 
  - We will call it **Evolution Noise** 


**How is the state represented?**

- In the Kalman Framework, Variables are Noisy and the Noise is assumed to be Gaussian 
  - As a result of this, Variables are basically PDF following a Gaussian Distribution 
    - It means that every variable can be represented just in terms of Mean and Variance (this is all the information needed to fully represent a Gaussian PDF)

- **Can the evolution break the Gaussianity?**
  - No as long as the Evolution is **Locally Linear** : a linear combination of Gaussian PDFs is still a Gaussian PDF appunto 
    - This fact is exploited by Standard Kalman Filter (KF) and Extended Kalman Filter (EKF) 
  - The Non-Linearities can break the Gaussianity 



**What could an example of Evolution Model be?**
- As the evolution model describes a Dynamical System, typically Differential Equations are used 
- The Evolution Noise is part of the model 
- As a result of these observations, a class of models typically used is the Stochastic Differential Equations one 



