(slides-and-recordings-estimation-kalman)=
# Kalman Filter

```{seo}
:description: Duckietown implementation of the famous Kalman Filter.
:keywords: Kalman Filter, Duckietown, estimation, probability, continuous time, stochastic, recursive, prior, posterior, apriori
```

The Kalman filter approximates the Bayes filter by assuming that the process and measurement models are linear and corrupted by additive Gaussian noise. Under these assumptions, the Kalman filter is optimal in the sense of minimizing the covariance of the estimation error.

In the case that the linearity assumption is violated, we can linearize the equations at each time step, which results in the extended Kalman filter (EKF).

Even though these assumptions seem severe, this filter is probably the most widely used in practice.

Note that there is also an activity that explains this approach in more detail in the [state estimation exercise](mooc-exercises).

```{vimeo} 889271993
:alt: Kalman Filter
```

