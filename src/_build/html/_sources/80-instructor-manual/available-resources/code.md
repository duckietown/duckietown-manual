```{seo}
:description: Duckietown code structure is based on a hierarchy of Docker images. Learn more in this page.
:keywords: Duckietown, code structure, code, Docker, Python, ROS, dts, Duckietown Shell, code hierarchy
```

(dt-code-structure)=
# The Code Structure

In this section, we give a brief overview of how the code is structured at a high level, and where you can find various things.

We make extensive use of [Docker](sec:developer_basics_docker) in our infrastructure. This enables us to keep things compartmentalized. It means that we can take the same "agent", e.g., one that is built as part of a [learning experience](learning-experiences), and run it many different ways: as locally but in simulation, on an actual Duckiebot, or on a cloud server for evaluation.

```{image} ../../_images/instructor-manual/duckietown-power-user.jpg
:scale: 40%
:align: center
:name: Duckietown power user managing Duckiebots with Ubuntu
:alt: Duckietown power user managing Duckiebots with Ubuntu
```


```{seealso}
For more details, you may want to refer to the [code hierarchy](code-hierarchy) page.
```


(code-dt-core)=
## `dt-core`

The [`dt-core`][dt-core] repository contains the code that runs the core autonomy stack for the Duckiebot.
This includes all the needed components for the [lane-following demo](duckiebot-demo-lf) as well as some of their core components for more complicated robot behaviors.

Some of the [learning-experiences](learning-experiences) leverage code from this repository, though it is somewhat "hidden" from the student doing the learning experience because it is part of the base docker image on which they are working.

(code-dt-ros-commons)=
## `dt-ros-commons`

The [`dt-ros-commons`][dt-ros-commons] repository is *upstream* of [`dt-core`][dt-core], in the sense that the Dockerfile that builds the `dt-core` image builds from the image that is created by [`dt-ros-commons`][dt-ros-commmons].

This repository contains [ROS](dtproject-ros)-related configurations and details.

For example, we created a parent class for all ROS nodes called [`dtros`](sec:advanced-dtros), and you will also find all of the message definitions for topics that ROS nodes use to communicate in this repository.

It is relatively unlikely that you should need to look into or understand in detail the code in this repository.

(code-dt-commons)=
## `dt-commons`

The [dt-commons][dt-commons] repository sits *upstream* of [dt-ros-commons][dt-ros-commons] and contains Duckietown-specific configurations and libraries.

It is very unlikely that you will need to look at the code in this repository.

(code-dt-machine-learning-base-environment)=
## `dt-machine-learning-base-environment`

The [dt-machine-learning-base-environment][dt-machine-learning-base-environment] is *downstream* of [dt-ros-commons][dt-ros-commons] but includes extra libraries and utilities for using the GPU and machine learning on the Jetson nano. For example, this is used in the [object detection learning experience](learning-experiences).

(code-duckietown-shell)=
## `duckietown-shell`

We have created the [`duckietown-shell`][duckietown-shell] to abstract away a lot of the details, particularly with respect to the way that Docker images are created and configured.

This is the code that runs the [`dts`](setup-dts) that is used extensively to do exercises, build code and documentation, run code and many other things.

It is very unlikely that you would need to understand the code in this repository. If you are interested to understand better what happens for a specific command that you run with `dts`, it is probably better to start with the implementation of that command in the [`duckietown-shell-commands`][duckietown-shell-commands] repository.

(code-duckietown-shell-commands)=
## `duckietown-shell-commands`

The [`duckietown-shell-commands`][duckietown-shell-commands] repository contains the implementations of the commands that are run by the Duckietown shell (with `dts` in the command line).

For the specific implementations of how these commands are executed, you can refer to the subfolders in the repository. You also probably should not need to understand the details of how these commands work, but if you get an error you do not understand, it might be a good place to start debugging (in addition to also reporting the bug).

(code-gym-duckietown)=
## `gym-duckietown`

The [`gym-duckietown`][gym-duckietown-repo] repository contains the code that implements the [`gym-duckietown` simulator](duckietown-gym-simulation).

This simulator is written in OpenGL and Python to be as slim as possible, with a view of being useful for machine learning, as it adheres to the [OpenAI Gym API](https://github.com/openai/gym).

It is also used to evaluate exercise submissions.

(code-duckietown-lx)=
## Learning Experiences

The learning experiences are now separated into their own repositories. See [](duckiebot-lxs) for details.

(code-duckietown-lx-recipes)=
## Learning Experience Recipes

Each learning experience also has its own recipe. See [](creating-new-lxs) for a description of the LX recipe.

(code-duckietown-lx-solutions)=
## Learning Experience Solutions

Each learning experience also has its own solution repository that is kept private.

[dt-core]: https://github.com/duckietown/dt-core
[dt-ros-commons]: https://github.com/duckietown/dt-ros-commons/
[dt-commons]: https://github.com/duckietown/dt-commons/
[dt-machine-learning-base-environment]: https://github.com/duckietown/dt-machine-learning-base-environment
[duckietown-shell]: https://github.com/duckietown/duckietown-shell
[duckietown-shell-commands]: https://github.com/duckietown/duckietown-shell-commands
[gym-duckietown-repo]: https://github.com/duckietown/gym-duckietown
[duckietown-lx-solutions]: https://github.com/duckietown/duckietown-lx-solutions
