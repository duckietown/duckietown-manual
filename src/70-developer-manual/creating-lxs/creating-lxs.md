(creating-new-lxs)=
# Creating New Learning Experiences

```{seo}
:description: Creating LXs (Learning Experiences) for a Duckiebot.
:keywords: Duckietown, Duckiebot, LXs, Learning Experiences
```

This page describes the general procedure for creating a learning experience (LX). LXs comprise two main parts:

1. The **LX recipe**, which is typically created by the instructor and hidden from the students
2. The **LX repository itself**, which houses the notebooks and whatever code structure should be visible to the student

An additional third repository is recommended, which has the same structure as the LX repository but contains 
the **solutions** and is kept private. 

```{tip}
While developing a new LX, it is good practice to start working on the solution first. Once the solution is
in place, parts of the solution with relative pedagogical value can be stripped out and replaced with 
placeholders effectively producing a boilerplate code that can populate the learner's workspace. 
This procedure guarantees that the resulting boilerplate is (by construction) enough for the learner to
achieve a valid solution.
```


A recommended way to get started is to create repos from the template repos for both the [recipe](https://github.com/duckietown/template-lx-recipe)
and the [LX](https://github.com/duckietown/template-lx)

The LX recipe contains components of the exercise that the student should
not need to change and are effectively hidden from view. There are a few
files here that will require some attention in the creation of the learning
experience.

## The LX Recipe Repository

As mentioned, the LX recipe repository contains all the configurations and details about how the LX should be run
that are not important for the student to see. In this section we will list the different components that you may
want to edit for the definition of your LX. 

### Dependencies

Specify any `apt` or `python` dependencies needed in the 
`dependencies-apt.txt` and 
`dependencies-py3.txt,` respectively in the recipe repository. 

### Base Image

You need to specify a `BASE_IMAGE` in the `Dockerfile` in the recipe repository. This
choice defines what is already in the docker image and can be used in the 
running of the exercise.

Reasonable choices could be:

 - [`dt-commons`](https://github.com/duckietown/dt-commons): likely a good choice
if the LX is pure python and doesn't require ROS.
 - [`dt-ros-commons`](https://github.com/duckietown/dt-ros-commons): likely
a good choice if you would like to use ROS in a standalone fashion (i.e., 
your exercise includes all the nodes that are needed)
 - [`dt-core`](https://github.com/duckietown/dt-core): a good choice if you 
would like to use one or more of the nodes defined in the packages 
in the `dt-core` repository. 

Coming soon:
 - ROS2 base image
 - Machine learning base image


### Title, Description, and Maintainer

Additionally, in the three Dockerfiles, that is  `Dockerfile`, `Dockerfile.vnc` and `Dockerfile.vscode`
you will need to update:

 - The `EXERCISE_NAME`: Replace `<LX_NAME_HERE>` with a title for your LX (**Note**: this should not contain spaces)
 - The `DESCRIPTION`: Replace `<DESCRIPTION_HERE>` with a brief description of your LX
 - The `MAINTAINER`: Replace `<YOUR_FULL_NAME>` and `<YOUR_EMAIL_ADDRESS>` with appropriate values



### Duckiematrix Configuration

By default, each LX is compatible with the [Duckiematrix](the-duckiematrix-manual).
See the [general procedure for running LXs](duckiebot-lxs)
for more details on how to deploy this capability through the `dts code` API. 
You can define the exact configuration of the Duckiematrix environment in the 
`assets/duckiematrix` directory in the recipe repository. For more details see
[](advanced-duckiematrix-development).



### noVNC Customization

It is also possible to customize the noVNC desktop. These configurations files are found the `assets/vnc`
folder of the recipe repository. Within these configurations you can:

 - Create new desktop icons and define what happens when they are clicked
 - Define the default RVIZ configuration that is loaded if RVIZ is opened

For inspiration you could take look at [the existing LXs](db-lx-intro).

### Launchers

You will need to define exactly what happens when the student executes the `dts workbench` command. The default
is that this will run a "launcher" called `default.sh`, defined in the `launchers` directory of the recipe repository. 
The launcher in the template simply runs a python file (`__solution/main.py`). In the case of ROS-based LX, you would 
likely want to call a ROS launch file with `roslaunch`.

### Code Hidden from Students

You can equally write any code that you don't want the students to see and include it in the `packages` directory
in the recipe repository. For example, this could be the file that calls the functions that are going to be 
written by the student as part of the LX which is in turn run by the launcher. You could also define ROS packages 
that will be used but are not important for the student to understand (such as debugging or visualization tools). 


## The LX Repository

The LX repository that you create is the one that the students will fork to complete the learning experience. 

### The `.dtproject` File

A file that you **must** edit in order for your LX to work is the `.dtproject` file in the LX repo. In this file
(if you started from the template), you will see:

```bash

# name of the exercise
NAME=<LX_NAME_HERE>

# recipe repository and location
# - fully qualified name of the recipe repository, e.g., 'duckietown/duckietown-lx-recipes'
RECIPE_REPOSITORY=<RECIPE_REPOSITORY_HERE>

# - branch of RECIPE_REPOSITORY containing the recipe
RECIPE_BRANCH=<RECIPE_BRANCH_HERE>

# - location of the recipe inside the RECIPE_REPOSITORY/RECIPE_BRANCH above
RECIPE_LOCATION=<RECIPE_LOCATION_HERE>
```

You should: 

 - Change the `<LX_NAME_HERE>` to the name of your LX
 - Change the `<RECIPE_REPOSITORY_HERE`> to the name of the recipe repository that you have created
 - Change the `<RECIPE_BRANCH_HERE`> to the name of the branch that you want to use in your recipe repository
 - Change the `<RECIPE_LOCATION_HERE`> to the path within the recipe repo where the recipe is store. If you used the 
template then this can simply be left blank


### Notebooks

In the `notebooks` directory you can place [jupyter notebooks](https://jupyter.org/). These will be executed in 
VSCode when the student executes: 

```shell
dts code editor
```

### Boilerplate Code

The code for the LX will go into the `packages` directory in the LX repo. It can be a good idea to provide some boilerplate
code so that the students just have to fill in specific parts. It is also recommended that the LX always "work" in the sense
that if the student runs the launcher through `dts code workbench` nothing breaks. The solution might not be properly 
implemented, but there are no compilation errors. 


```{attention}
When working in the development workspace, you can append the `--recipe` flag to any `dts code` commands 
and specify your local development version of the recipe.
```
