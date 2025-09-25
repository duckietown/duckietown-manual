```{seo}
:description: Slides and recording used to introduce state estimation, or filtering, in Duckietown.
:keywords: Bayes Filter, Kalman Filter, Particle Filter, Histogram Filter, Duckietown, SLAM, Ransac, filtering, estimation, state, robotics, robot, autonomy, autonomous vehicle, AV, self driving car, self-driving car
```


(slides-and-recordings-estimation-overview)=
# State Estimation

This section lists slides and recordings used to present topics related to state estimation.

These are methods for the robot to quantify its position and orientation (pose) in the world, and possibly also the state of the world around it in the case of simultaneous localization and mapping (SLAM).

In other words, estimation algorithms provide solutions for transforming sensor _data_ into actionable _information_, useful to the robot to achieve its task.

We present materials related to how to represent the robot, as well as several different filters, which generate a state estimate based on the data that the robot is collecting (as well as some pre-built models and assumptions).

Finally, we present some methods related to robust optimization and SLAM. These materials are supported by the [learning experience](learning-experiences) related to state estimation.


```{tableofcontents}
```
