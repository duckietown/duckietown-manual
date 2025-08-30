```{seo}
:description: Duckietown uses an OpenAI Gym simulator written in pure Python to be as slim as possible, and support ML traning applications. A new Unity-based environment, the Duckiematrix, is in beta.
:keywords: Duckietown, simulation, simulator, OpenAI Gym, evaluations
```
(simulation)=
# Duckietown Simulator

We use simulations for both development and evaluation. 

(gym-duckietown)=
## Gym Duckietown

We have developed a simulation environment in OpenGL. 

```{figure} ../../_images/instructor-manual/simplesim_free.png
:name: gym-duckietown1
:scale: 50%
:align: center

A screenshot of our simple OpenGL based simulation environment
```

This simulator is used as a development environment in many of the [learning experiences](learning-experiences). 
To test exercises in simulation, one simply adds the `--sim` flag to the `dts code workbench` command:

```
dts code workbench --sim
```

For more details about the `dts code` API that is used with the exercises please refer to the [Learning Experiences Manual](temp-lx-devmanual-lx-dev-intro).


The simulator may also be used directly. For example, this is done in the [object detection exercise](https://github.com/duckietown/duckietown-lx/tree/mooc2022/object-detection) to automate the process of collecting labeled data to train the model. 

For full details on how to use the simulator, refer to [](temp-sw-devmanual-duckietown-simulation). 


```{figure} ../../_images/instructor-manual/finalmain.gif
:name: gym-duckietown2

```

```{warning}
If the simulator is used in standalone mode it is slightly different than the version of the simulator that is used for exercise evalution.
```

The reason for this is partly historical and partly practical. The Gym Duckietown simulation predates the [automated evaluation infrastructure](https://challenges.duckietown.org/v4/). It was originally used as a tool for training reinforcement learning agents. This is the reason that it adheres to the [OpenAI Gym](https://github.com/openai/gym) API. As such, the focus originally was on making the simulation extremely fast and lightweight, and this is the reason it was written in pure Python. 

When we developed the Challenges infrastructure we determined that the simulation was not realistic enough since there were some missing pieces such as motion blur and momentum. For those very motivated to dig into the details, the extra pieces coded are in the [challenge-aido_LF-simulator-gym](https://github.com/duckietown/challenge-aido_LF-simulator-gym) repository. 


(matrix-duckietown)=
## The Duckiematrix

We are in the process of developing a higher-fidelity simulation environment that we refer to as the Duckiematrix. This simulation is built using [Unity](https://unity.com/).

```{figure} ../../_images/instructor-manual/duckiematrix.jpg
:name: duckiematrix
:scale: 50%
:align: center
:alt: Duckietown Duckiematrix teaser

The "Duckiematrix" simulation environment
```

To learn more, check out [](book-devmanual-duckiematrix:book). 

