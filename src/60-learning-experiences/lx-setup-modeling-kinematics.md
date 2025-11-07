(lx-setup-mod-kin)=
# LX: Kinematics and Odometry

```{seo}
:description: Step by step instructions on how to run the kinematics and odometry learning experience (LX) in Duckietown.
:keywords: Duckietown, Duckiebot, LXs, Learning Experiences, mathematical modelling, differential drive robot, modelling of a differential drive robot, differential drive, kinematic model, kinematics, kinematic model of a differential drive robot, wheel encoders, odometry, dead reckoning, estimator
```

```{needget}
- Learning experience computer setup: [](duckiebot-lxs)
- (optional) familiarity with ROS basics: [](lx-setup-ros-basics)
---
- Running the kinematics and odometry learning experience.
```

This page describes how to run the BV learning experience. 

```{admonition} Intended Learning Outcomes
:class: tip
In this learning experience, learners will:
- appreciate the importance of representations in robotics, in particular what is a robot _state_
- be able to formalize and explain the concept of _pose_ in SE(2) and SE(3)
- practice defining and implementing poses in given reference frames
- learn how to convert poses in a reference frame to another one
- read data from wheel encoders of physical or virtual Duckiebots, and familiarize with the message type
- code and implement a simple ROS node to extract wheel encoder data and manipulate it
- design and implement a dead reckoning estimator to reconstruct the pose of a differential drive robot from wheel encoder measurements (odometry)
- be able to articulate the strengths and shortcomings of this dead rekoning estimator
- perform odometry calibration procedures for physical Duckiebots
- use more advanced ROS tools (`rosservice`, `rosparameter`)    
```

```{note}
This exercise can be run on a [real Duckiebot](https://get.duckietown.com/products/duckiebot-db21?variant=41543707099311) or on a virtual Duckiebot in [the Duckiematrix](the-duckiematrix-first-steps). 
```

(lx-forking-mod-kin)=
## Forking the repo

### 1. Create a fork 

Navigate to [the Modeling and Kinematics LX repository](https://github.com/duckietown/lx-kinematics-odometryol).

Find and press the "Fork" button on the top right:

```{figure} /_images/lx-devmanual/intro/duckietown-lx-forking.png
:alt: how to fork a Duckietown LX repository
:width: 90%
:name: duckiebot-lx-forking-2
:align: center

Fork the LX to be able to make local changes while still being able to receive updates.
```

This will create a new repository at: `<your_github_username>/lx-kinematics-odometry`.

### 2. Clone the fork 

Clone the fork on your computer, replacing your GitHub username in the command below, and navigate to the new folder:

    git clone git@github.com:<your_github_username>/lx-kinematics-odometry
    cd lx-kinematics-odometry
        

### 3. Configure upstream repo 

Configure the Duckietown version of this repository as the upstream repository to synchronize with your fork.

List the current remote repository for your fork,

    git remote -v

Specify a new remote upstream repository,

    git remote add upstream https://github.com/duckietown/lx-kinematics-odometry

Confirm that the new upstream repository was added to the list,

    git remote -v

You can now push your work to your own repository using the standard GitHub workflow, and the beginning of every exercise will prompt you to pull from the upstream repository, updating your exercises to the latest version (if available).

(lx-system-update-mod-kin)=
## Keeping your System Up To Date

- 💻 These instructions are for `ente` learning experiences. Ensure your Duckietown Shell is set to an `ente` profile (and not, e.g., a `daffy` one). You can check your current profile with:

    dts profile list

  To switch to an ente profile, follow the [Duckietown Manual DTS installation instructions](setup-dts).

- 💻 Pull from the upstream remote to synch your fork with the upstream repo:

    git pull upstream ente

- 💻 Make sure your Duckietown Shell is updated to the latest version: `pipx upgrade duckietown-shell`

- 💻 Update the shell commands: `dts update`

- 💻 Update your laptop/desktop: `dts desktop update`

- 🚙 Update your Duckiebot: `dts duckiebot update ROBOTNAME` (where `ROBOTNAME` is the name of your Duckiebot - real or virtual.)

    **Note**: if your virtual robot (named, e.g., `VBOT`) hangs indefinitely when you try to update it, you can try to restart it with:

        dts duckiebot virtual restart VBOT

(lx-code-editor-lx-mod-kin)=
## Launching the Code Editor

```{important}
All `dts code` commands should be executed inside the root directory of the learning experience.
```

Making sure you are inside the path of the specific learning experience you want to work on, open the code editor by running:

```
dts code editor
```

Wait for a URL to appear on the terminal, then click on it or copy-paste it in the address bar
of your browser to access the code editor. The first thing you will see in the code editor are a version of these instructions. At this point you can start following the LX-specific indications shown in your code editor.

(lx-navigating-notebooks-mod-kin)=
## Walkthrough of Notebooks

Inside the code editor, use the navigator sidebar on the left-hand side to navigate to the
`notebooks` directory and open the first notebook.

Follow the instructions on the notebook and work through them in sequence.

In many cases the last notebook will instruct you to write some code inside the
learning experience directory. 

Once you have done that you will need to **build** your code before **testing** it.

(lx-matrix-testing-mod-kin)=
### Testing with the Duckiematrix

To test your code in the Duckiematrix you will need a virtual robot attached to an ongoing session. 

(lx-create-vbot-mod-kin)=
#### 1. Creating and starting virtual Duckiebot

To test your code in the Duckiematrix you will need a virtual robot. You can create one with the command:

```
dts duckiebot virtual create --type duckiebot --configuration DB21J [VBOT]
```

where `[VBOT]` is the hostname. It can be anything you like, subject to the [same naming constraints of physical Duckiebots](setup-db-sd-card-flashing-complete). Make sure to remember your robot (host)name for later.

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

(lx-code-matrix-start-mod-kin)=
#### 2. Starting the Duckiematrix with the virtual Duckiebot

Now that your virtual robot is ready, you can start the Duckiematrix. From this exercise directory do:

```
dts code start_matrix
```

You should see the Unity-based Duckiematrix simulator start up. For more details about using
the Duckiematrix see [](the-duckiematrix-manual).

(lx-code-build-mod-kin)=
### Building the Code

From inside the learning experience root directory, you can build your code with:

```
dts code build -R ROBOT_NAME
```

where `ROBOT_NAME` can be either a physical or virtual robot. 

(lx-code-test-mod-kin)=
### Testing on a Duckiebot or in the Duckiematrix

🚙 To test your code on your real Duckiebot you can do:

```
dts code workbench -R [ROBOT_NAME]
```

💻 To test your code in the Duckiematrix:

```
dts code workbench -m -R [VIRTUAL_ROBOT_NAME]
```

(note the `-m` flag which means that we are running in the `matrix`)

In another terminal, you can launch the `noVNC` viewer, which can be useful to interact with the virtual robot in different ways depending on the specific LX.

```
dts code vnc -R [ROBOT_NAME]
```

where `[ROBOT_NAME]` could be the real or the virtual robot (use whichever you ran the `dts code workbench` and `dts code build` command with).


```{figure} ../_images/lx-devmanual/lx-mod-kin/images/odometry/odometry-real-2.png
:alt: precise reconstruction of physical Duckiebot odometry 
:width: 70%
:name: duckiebot-lx-kin-odometry-good-real
:align: center

Example of good odometry from a dead rekoning estimator using wheel encoder data on a physical Duckiebot. The robot starts and ends at the same position, and the estimate does not drift significantly.
```

```{figure} ../_images/lx-devmanual/lx-mod-kin/images/odometry/less-good-odometry.png
:alt: imprecise reconstruction of physical Duckiebot odometry 
:width: 70%
:name: duckiebot-lx-kin-odometry-less-good-real
:align: center

Example of less good odometry from a dead rekoning estimator using wheel encoder data on a physical Duckiebot. The robot starts and ends at the same position, but the estimate drifts significantly.
```

## Troubleshooting

If you run into any issues while building the image, you can search the troubleshooting symptoms below or
reference the [](how-to-get-help) section of this manual.

```{trouble}

`dts :  The path '...' does not appear to be a Duckietown project.
     :  The metadata file '.dtproject' is missing.`

---
You need to be in the root directory of the LX in order to run the `dts code` commands.
```

```{trouble}
When running `dts code editor` I get an error: `dts :  No valid DTProject found at '/workspaces/dt-env-developer/lx'`
---
Make sure your are executing the commands from inside a learning experience folder (e.g., `*/lx-control/`)
```

```{trouble}
My virtual robot (named, e.g., `VBOT`) hangs indefinitely when trying to update it.
---
Try to restart it with: `dts duckiebot virtual restart VBOT`
```