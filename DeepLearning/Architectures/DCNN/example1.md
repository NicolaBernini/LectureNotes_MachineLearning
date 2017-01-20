
# Overview 

An example of CNN Architecture is presented in 

<figure>
  <img src="http://www.embedded-vision.com/sites/default/files/technical-articles/CadenceCNN/Figure4.jpg">
  <figcaption>Fig1. - CNN Example</figcaption>
</figure>


# Analysis 

Making sense of the dimensions is important 

- Input 
  - Image is `32 x 32` 

- Layer 1 
  - Content = Convolutional Kernel `5 x 5` 
  - Input = Image `32 x 32`
  - Output = Image `28 x 28`
    - Convolutional Kernels can be applied only from `(2,2)` to `(26,26)`

