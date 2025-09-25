
(slides-and-recordings-architectures)=
# Architectures in Robotics

```{seo}
:description: Duckietown introduction to robot architectures - logical, physical, control, stateful.
:keywords: state, sensorimotor control, Braitenberg Vehicles, BVs, logical architecture, architecture, physical architecture, computational architecture, feedback
```

One of the first and most fundamental choices in the design of the software for a robotic system is the choice of how to structure the architecture. In this series of videos, we present some options.

## Sensorimotor Architecture

In some sense, a sensorimotor architecture is the simplest possible robot architecture that one could imagine - one where sensors are directly connected to the motors. To illustrate this idea we introduce "Braitenberg vehicles", which also has an associated [learning experience](learning-experiences).

```{vimeo} 546397378
:alt: Sensorimotor Architecture
```


## Stateful Architectures

In a stateful architecture, we now have more complex abstractions, such as perception, planning, and control. These pieces operate together in a feedback loop that can be used to control the robot.

```{vimeo} 554223650
:alt: Stateful Architectures
```

The following slides cover sensorimotor and stateful architectures.

```{slides} ../../../../_assets/instructor-manual/autonomy-architectures.pdf
```


## Logical and Physical Architectures

In this video, we explain the distinction between logical architectures, which specify the functionality of components and their interfaces, and physical architectures, which explain the details of how the components are implemented.

```{vimeo} 587453397
:alt: Logical and Physical Architectures
```

```{slides} ../../../../_assets/instructor-manual/logical-architectures.pdf
```
