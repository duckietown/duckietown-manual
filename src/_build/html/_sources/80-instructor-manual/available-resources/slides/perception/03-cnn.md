```{seo}
:description: Deep Convolutional Neural Networks in Duckietown.
:keywords: convolutional neural networks, CNNs, neural networks, AI, machine learning, duckietown, ML, deep learning, padding, stride, pooling, residual
```

(slides-and-recordings-cnn)=
# Deep Convolutional Neural Networks

Since images are high-dimensional (there are lots of pixels!), it is impractical to have a fully connected [neural network](slides-and-recordings-intro-neural-networks).
Instead, we will learn [image filters](slides-and-recordings-image-filtering) and apply them through convolution.
 If we chain several of these blocks together the result is a deep convolutional neural network, which we introduce here.
 We also discuss some details needed in the construction of these networks, such as padding, stride, pooling, and finally we introduce the residual which can more efficiently pass gradients enabling such models to be much deeper (more layers).

```{vimeo} 549675144
:alt: Deep Convolutional Neural Networks
```


