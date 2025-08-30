(slides-and-recordings-estimation-slam)=
# Full Lecture on Simultaneous Localization and Mapping

```{seo}
:description: Duckietown introduction to the simultaneous localization and mapping (SLAM) problem in robotics.
:keywords: SLAM, simultaneous localization and mapping, duckietown, botics, autonomous vehicles, AVs, self driving cars, self-driving cars
```

## Introduction to SLAM

Simultaneous localization and mapping (SLAM) is the problem where a robot must use the sensor data that it is collecting to build a representation of the environment while concurrently placing itself within that representation. 

In this lecture, we present first the mapping problem, assuming the robot knows where it is (i.e., is _localized_), then the localization problem assuming that the map is provided, and then finally the full joint SLAM problem. 

We discuss three approaches to the SLAM problem, the first based on the Kalman filter, the second based on the particle filter, and the third a maximum a-posteriori optimization-based approach. 

```{slides} ../../../../_assets/instructor-manual/slam.pdf
