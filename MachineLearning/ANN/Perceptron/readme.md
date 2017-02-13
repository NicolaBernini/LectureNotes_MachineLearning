
# Overview 

The basic perceptron model is described in Fig1 

<figure>
  <img src="http://www.embedded-vision.com/sites/default/files/technical-articles/CadenceCNN/Figure3b.jpg">
  <figcaption>Fig1. - Basic Perpcetron Model. A Weighted Sum of Input is performed and then it is passed to the Neuron Activation Function to compute its Output State</figcaption>
</figure>


## Structure 

- Input: set of N weighted input 
- Output: two states hence 1 bit 
- Activation Function: defines the final state of the output according to the weighted sum of the input 

## Training  

- Input: 
  - Set of N Training Samples <img src="http://quicklatex.com/cache3/70/ql_2fd891814493081005cc3af80393e070_l3.png"> in a specific State Space <img src="http://quicklatex.com/cache3/75/ql_7b2ccc555d1f0f7650c7af99d8d5c275_l3.png"> 
    - <img src="http://quicklatex.com/cache3/98/ql_4c62bf401e6532a66206d7da60a56f98_l3.png">
  - Set of N Labels <img src="http://quicklatex.com/cache3/d0/ql_ed3b03f45f37fe431f5f25ef5ebfaad0_l3.png">

- Output: 
  - Hyperplane in the Training Samples Space which separates the samples according to labels 


