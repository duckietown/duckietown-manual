```{seo}
:description: Understand why and how to use gym-duckietown, set it up quickly, drive the simulator, and customise maps, actions, and rewards.
:keywords: Duckietown simulator, gym-duckietown, robotics simulation, domain randomisation, reinforcement learning, Python OpenGL
```

(duckietown-simulation)=
# OpenGL-based Gym Environment (legacy)

```{needget}
* Implementing Basic Robot Behaviors
--- 
* Experience with running and testing on the Duckietown simulator 
```

```{figure} ../../_images/developer/advanced/simulator/simplesim_free.png
:name: fig:simplesim_free

```

```{warning}
This package is obsolete, it has been superseeded by the Duckiematrix Gym environment, [available here](https://github.com/duckietown/gym-duckiematrix).
```

## Introduction to the Gym-Duckietown Simulator

Gym-Duckietown is a simulator for the [Duckietown](https://duckietown.com) universe, 
written in pure Python/OpenGL (Pyglet). It places your agent, a Duckiebot, 
inside an instance of a Duckietown: a loop of roads with turns, 
intersections, obstacles, Duckie pedestrians, and other Duckiebots.

Gym-Duckietown is fast, open, and very customizable. What started as a lane-following simulator has evolved into a fully functioning autonomous driving simulator that you can use to train and test your Machine Learning, Reinforcement Learning, Imitation Learning, or even classical robotics algorithms. Gym-Duckietown offers a wide range of tasks, from simple lane-following to full city navigation with dynamic obstacles. Gym-Duckietown also ships with features, wrappers, and tools that 
can help you bring your algorithms to the real robot, including [domain-randomization](https://blog.openai.com/spam-detection-in-the-physical-world/), accurate camera distortion, and differential-drive physics (and most importantly, realistic waddling).

```{figure} ../../_images/developer/advanced/simulator/finalmain.gif
:name: fig:finalmain-sim

```

The development Gym Duckietown simulator has ended with the previous version of the codebase (`daffy`), therefore it 
is recommended that you refer [to the daffy documentation](https://docs.duckietown.com/daffy/devmanual-software/intermediate/simulation/gym-simulation-in-duckietown.html)
for details about its use and features. 