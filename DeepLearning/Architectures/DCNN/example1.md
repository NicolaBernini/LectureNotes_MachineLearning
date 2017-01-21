
# Overview 

An example of CNN Architecture is presented in 

<figure>
  <img src="http://www.embedded-vision.com/sites/default/files/technical-articles/CadenceCNN/Figure4.jpg">
  <figcaption>Fig1. - CNN Example</figcaption>
</figure>


# Analysis 

Making sense of the dimensions is important 

- Input 
  - Image is `32 x 32` pixel probably RGB (3 channels) hence a final tensor of `32 x 32 x 3` 

- Layer 1 
  - Content = Probably `36` Convolutional Kernel of `5 x 5` size 
  - Input = Image `32 x 32 x 3`
    - For each of the 3 channels, the `32 x 32` image is processed by the Convolutional Kernel 
    - Single Kernel Outpue = Image `28 x 28` 
      - Convolutional Kernels can be applied only from `(2,2)` to `(26,26)`
  - Outout = Image `28 x 28 x 108`
    - Considering 36 Kernels * 3 Channels = 108 Convolutional Images of `28 x 28` size 

