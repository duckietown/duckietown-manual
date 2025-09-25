(duckiebot-lxs)=
# General Procedure for Running Learning Experiences

```{seo}
:description: The LXs (Learning Experiences) available for a Duckiebot.
:keywords: Duckietown, Duckiebot, LXs, Learning Experiences
```

This page describes the general workflow for learning experiences. There might
be slight differences in some cases, you should follow the specific instructions
provided for the specific learning experiences.

```{note}
If you are interested to learn about creating your own learning experiences, see [](creating-new-lxs).
```

## SSL Certificate

```{note}
You only need to run this once the first time you run an LX on a new laptop
```

We use SSL certificates and TLS encryption to guarantee the highest standard of safety and privacy. Set up a local SSL certificate needed to run the LX editor inside your browser:

```shell
dts setup mkcert
```


## Forking the LX Repository

To store your own code, while also keeping the ability to pull updates
from our version of this repo, we recommend that you create your own fork.

Start by pressing "Fork" in the top right corner of the LX repository page on GitHub.
You will be able to create a new
fork: `<your_username>/lx-<lx-name>`

Then clone your new repository, replacing your GitHub username in the command below,

    git clone git@github.com:<your_username>/lx-<lx-name>

Now, change directory to `lx-<lx-name>`

    cd lx-<lx-name>

Now we will configure the Duckietown version of this repository as the upstream repository to sync with your fork.

List the current remote repository for your fork,

    git remote -v

Specify a new remote upstream repository,

    git remote add upstream https://github.com/duckietown/lx-<lx-name>

Confirm that the new upstream repository was added to the list,

    git remote -v

You can now push your work to your own repository using the standard GitHub workflow, and the beginning of every
exercise will prompt you to pull from the upstream repository - updating your exercises to the latest Duckietown
version,


## Keeping your System Up-To-Date

It is a good idea to pull from the upstream remote in case your instructor or the
exercise creator changed something:

    git pull upstream ente

It is also a good idea to:

- 💻 Always make sure your Duckietown Shell is updated to the latest version: `pipx upgrade duckietown-shell`

- 💻 Update the shell commands: `dts update`

- 💻 Update your laptop/desktop: `dts desktop update`

- 🚙 Update your Duckiebot: `dts duckiebot update ROBOTNAME` (where `ROBOTNAME` is the name of your Duckiebot chosen during the initialization procedure.)


## Work on the Exercise

### Launch the Code Editor

Open the code editor by running the following command,

```
dts code editor
```

Wait for a URL to appear on the terminal, then click on it or copy-paste it in the address bar
of your browser to access the code editor. The first thing you will see in the code editor is
this same document, you can continue there.

<!--
(duckiedrone-lxs-list)=
## Supported Duckiedrone LXs


-->


```{important}
All `dts code` commands should be executed inside the root directory of the learning experience.
```



### Walkthrough of Notebooks

Inside the code editor, use the navigator sidebar on the left-hand side to navigate to the
`notebooks` directory and open the first notebook.

Follow the instructions on the notebook and work through the notebooks in sequence.
In many cases the last notebook will instruct you to write some code inside the
learning experience directory. Once you have done that you will need to build and test your code.
We describe how to do that next.

### Building your Code

From inside the learning experience root directory, you can build your code with

```
dts code build -R ROBOT_NAME
```

This will build a docker image with your code compiled inside - you should your ROS node get built during the process.

```{hint}
Strengthen your iterative development habits by beginning every work session with a fresh build of your LX.
This will help ensure that you do not continue development on top of any previous errors.
```


### Testing with the Duckiematrix

In order to test your code in the Duckiematrix you will need a virtual robot. You can create one with the command:

```
dts duckiebot virtual create [VBOT]
```

where `[VBOT]` can be anything you like (but remember it for later).

Then you can start your virtual robot with the command:

```
dts duckiebot virtual start [VBOT]
```

You should see it with a status `Booting` and finally `Ready` if you look at `dts fleet discover`:

```
     | Hardware |   Type    | Model |  Status  | Hostname
---  | -------- | --------- | ----- | -------- | ---------
[VBOT] |  virtual | duckiebot | DB21J |  Ready   | [VBOT].local
```

Now that your virtual robot is ready you can start the Duckiematrix. From this exercise directory do:

```
dts code start_matrix
```

You should see the Unity-based Duckiematrix simulator start up. For more details about using
the Duckiematrix see [](the-duckiematrix-manual).


### Testing on a Duckiebot or in the Duckiematrix

To test your code on your real Duckiebot you can do:

```
dts code workbench -R [ROBOT_NAME]
```

To test your code in the duckiematrix you can do:

```
dts code workbench -m -R [VIRTUAL_ROBOT_NAME]
```

(note the `-m` flag which means that we are running in the `matrix`)

In another terminal, you can launch the `noVNC` viewer for this exercise which can be useful to send commands to the robot and view the odometry that you calculating in the RViZ window.

```
dts code vnc -R [ROBOT_NAME]
```

where `[ROBOT_NAME]` could be the real or the virtual robot (use whichever you ran the `dts code workbench` and `dts code build` command with).


## Troubleshooting

If you run into any issues while building the image, you can search the troubleshooting symptoms below or
reference the [](how-to-get-help) section of this manual.

```{trouble}

`dts :  The path '...' does not appear to be a Duckietown project.
     :  The metadata file '.dtproject' is missing.`

---
You need to be in the root directory of the LX in order to run the `dts code` commands.
```
