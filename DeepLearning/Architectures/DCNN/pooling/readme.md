
# Overview 

Max Pooling is a Downsampling Technique commonly sued in CNN 

The Max Pooling Algo works as follows 
- Input: Convolution Image 
  - The result of the Convolutional Kernel Application to the Image Kernel on the previous layer 
- Divides the image in non-overlapping subregions 
  - The Max-Pooling Operator goal is to downsample hence to pass from a `(N x M)` image to a `(N'x M')` with `N' < N` and `M' < M`
- Foreach subregion 
  - Chooses the Max Value 

<img src="http://cs231n.github.io/assets/cnn/maxpool.jpeg"/>
