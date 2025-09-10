```{seo}
:description: Learn about the `dts code` workflow in Duckietown and how to use it to develop, test, and submit your Duckietown Learning Experiences (LX).
:keywords: Duckietown, learning experience, LX, `dts code`, development workflow, Duckiebot, simulator, submit results, Docker, VSCode
```


(devmanual-lx-dts-code-workflow)=
# Step 2: Using the `dts code` workflow

The `dts code` workflow is a set of simple but powerful Duckietown shell commands that you can use to edit, test, 
and run Duckietown Learning Experiences (LX). These tools can
* Spin up a development environment
* Run new robot behaviors in the simulator and on a Duckiebot
* Submit your results to Duckietown challenges
* And much more

We will gain familiarity with this workflow by walking through the **hello-world** learning experience from the [duckietown-lx repository](https://github.com/duckietown/duckietown-lx) as an example. Instructions on how to fork and clone this repository are located in [](env-setup).

## Getting started

Complete the following steps to start your development journey with 
the `dts code` workflow:

### ✅ Step 1

Open a terminal and navigate to the `duckietown-lx/hello-world-lx` directory.

### ✅ Step 2

Glance over [](devmanual-lx-dts-code-command-set) for a preview of your toolkit.

### ✅ Step 3

Continue to the next page, [](dts-code-build), to start your first learning experience!

(devmanual-lx-dts-code-command-set)=
## The `dts code` commands set

```{todo}
update this list on ente
```

### `dts code build`

Builds a learning experience into a Docker image that can then be run.

### `dts code edit`

Spins up a browser-based development environment that can be used to work 
through the Learning Experience (LX) using `VSCode`.

### `dts code workbench`

Creates a virtual environment with Desktop icons that will allow you to run activities easily, simulate a Duckiebot directed through a virtual world by your control algorithms, or execute a demo on your real-world Duckiebot - 
all with debugging and visualization tools to help you along the way.

### `dts code evaluate`

Evaluates your solutions to the learning experience activities on your local machine to quickly inform you of your progress.

### `dts code submit`

Submits your work to the 
[Duckietown Challenges Server](https://challenges.duckietown.org) so that you can monitor your results and view the work of other developers around the world.

<!--
```{todo}
Update the URL to the challenges server once we move to `duckietown.com`.
```
-->

````{tip}
Remember that in addition to the `dts code` workflow, you also have the complete set of Duckietown development tools at your disposal for building and running the projects within each learning experience.  

Check out the [Duckiebot](book-opmanual-duckiebot:ops-tools) and [DTProject](book-devmanual-software:dtproject) 
development pages for more helpful Duckietown shell commands.
````
