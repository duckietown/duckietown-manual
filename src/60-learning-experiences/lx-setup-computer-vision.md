(lx-setup-computer-vision)=
# LX: Computer Vision

```{seo}
:description: Step by step instructions on how to run the computer vision - visual servoing learning experience (LX) in Duckietown.
:keywords: Duckietown, Duckiebot, LXs, Learning Experiences, computer vision, visual servoing, differential drive robot
```

```{needget}
- Learning experience computer setup: [](duckiebot-lxs)
- (reccomended) A successful Duckiematrix installation: [](the-duckiematrix-first-steps)
- (optional) A "Ready to Go" Duckiebot: [](duckiebot-setup-intro)
---
- Running the Computer Vision learning experience.
```

This page describes how to run the "Computer Vision - Visual Servoing" learning experience.

```{admonition} Intended Learning Outcomes
:class: tip
After this learning experience, you will:
- learn about and perform instrinsics and extrinsics camera calibration procedures
- 
```

```{warning}
If you are running Duckietown inside a devcontainer and not on a native Ubuntu setup, some steps vary slightly. Read this before proceeding: [](caveat-devcontainer-lx)
```

## About these learning activities

For guided setup instructions, lecture content, and more related to this LX, see [our Self-Driving Cars with Duckietown MOOC on EdX](https://duckietown.com/mooc).

```{note}
This exercise can be run on a [real Duckiebot](https://get.duckietown.com/products/duckiebot-db21?variant=41543707099311) or on a virtual Duckiebot in [the Duckiematrix](the-duckiematrix-first-steps). 
```

(lx-forking-computer-vision)=
## Forking the repository

### 1. Create a fork

Navigate to [the LX-Computer-Vision repository](https://github.com/duckietown/lx-computer-vision).

Find and press the "Fork" button on the top right:

```{figure} /_images/lx-devmanual/intro/duckietown-lx-forking.png
:alt: how to fork a Duckietown LX repository
:width: 90%
:name: duckiebot-lx-forking-computer-vision
:align: center

Fork the LX to be able to make local changes while still being able to receive updates.
```

This will create a new repository at: `<your_github_username>/lx-computer-vision`.

### 2. Clone the fork

Clone the fork on your computer, replacing your GitHub username in the command below, and navigate to the new folder:

    git clone git@github.com:<your_github_username>/lx-computer-vision
    cd lx-computer-vision
        
### 3. Configure the upstream repository

Configure the Duckietown version of this repository as the upstream repository to synchronize with your fork.

List the current remote repository for your fork,

    git remote -v

Specify a new remote upstream repository,

    git remote add upstream https://github.com/duckietown/lx-computer-vision

Confirm that the new upstream repository was added to the list,

    git remote -v

You can now push your work to your own repository using the standard GitHub workflow, and the beginning of every exercise will prompt you to pull from the upstream repository, updating your exercises to the latest version (if available).

(lx-system-update-computer-vision)=
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

(lx-code-editor-lx-computer-vision)=
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

(lx-navigating-notebooks-computer-vision)=
## Walkthrough of Notebooks

Inside the code editor, use the navigator sidebar on the left-hand side to navigate to the
`notebooks` directory and open the first notebook.

Follow the instructions on the notebook and work through them in sequence.

In many cases the last notebook will instruct you to write some code inside the
learning experience directory. 

Once you have done that you will need to **build** your code before **testing** it.

(lx-matrix-testing-computer-vision)=
### Testing with the Duckiematrix

To test your code in the Duckiematrix you will need a virtual robot attached to an ongoing session. 

(lx-create-vbot-computer-vision)=
#### 1. Creating and starting virtual Duckiebot

You can create one with the command:

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

Once you are done for the day, do not forget to stop your virtual robot:

```
dts duckiebot virtual stop [VBOT]
```

If in doubt, you can check the status of your virtual scuderia at any time with:

```
dts duckiebot virtual list
```

(lx-code-matrix-start-computer-vision)=
#### 2. Starting the Duckiematrix with the virtual Duckiebot

Now that your virtual robot is ready, you can start the Duckiematrix. From this exercise directory do:

```
dts code start_matrix
```

You should see the Unity-based Duckiematrix simulator start up. For more details about using
the Duckiematrix see [](the-duckiematrix-manual).

```{figure} ../_images/lx-devmanual/lx-computer-vision/extrinsics/scenario0/frame0_distorted.jpg
:alt: Distorted image from Duckiebot POV in the Duckiematrix, due to uncalibrated camera extrinsics.
:width: 70%
:name: duckiebot-lx-cv-image-distorted
:align: center

The Duckiebot fisheye camera lens distorts images, requiring a camera calibration process. 
```

```{figure} ../_images/lx-devmanual/lx-computer-vision/extrinsics/scenario0/frame0_rectified.jpg
:alt: Rectified image from Duckiebot POV in the Duckiematrix, thanks to calibrated camera extrinsics.
:width: 70%
:name: duckiebot-lx-cv-image-rectified
:align: center

Duckiebot images with a calibrated camera.
```

(lx-code-build-computer-vision)=
### Building the Code

From inside the learning experience root directory, you can build your code with:

```
dts code build -R ROBOT_NAME
```

where `ROBOT_NAME` can be either a physical or virtual robot. 

(lx-code-test-computer-vision)=
### Testing on a Duckiebot or in the Duckiematrix

🚙 To test your code on your real Duckiebot you can do:

```
dts code workbench -R [ROBOT_NAME]
```

💻 To test your code on a virtual robot in the Duckiematrix:

```git
dts code workbench -m -R [VIRTUAL_ROBOT_NAME]
```

(note the `-m` flag which means that we are running in the `matrix`.)

In another terminal, you can launch the `noVNC` viewer, which can be useful to interact with the virtual robot in different ways depending on the specific LX.

```
dts code vnc -R [ROBOT_NAME]
```

where `[ROBOT_NAME]` could be the real or the virtual robot (use whichever you ran the `dts code workbench` and `dts code build` command with).

```{figure} ../_images/lx-devmanual/lx-computer-vision/images/visual_control/lane-markings-angles.png
:alt: 
:width: 70%
:name: duckiebot-lx-cv-lane-markings
:align: center

Visual Servoing relies exclusively on images to control the Duckiebot. 
```


## Troubleshooting

```{trouble}
When running `dts code editor` I get an error: `dts :  No valid DTProject found at '/workspaces/dt-env-developer/lx'`
---
Make sure your are executing the commands from inside a learning experience folder (e.g., `*/lx-computer-vision/`)
```

```{trouble}
My virtual robot (named, e.g., `VBOT`) hangs indefinitely when trying to update it.
---
Try to restart it with: `dts duckiebot virtual restart VBOT`
```

```{trouble}
When I run `dts code vnc` nothing happens in the browser. 
---
It can take some time for noVNC to start (10-45 seconds, depending on computer specifications), wait. 
```