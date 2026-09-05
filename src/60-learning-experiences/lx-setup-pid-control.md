```{seo}
:description: Step by step instructions on how to run the PID control learning experience (LX) in Duckietown.
:keywords: Duckietown, Duckiebot, LXs, Learning Experiences, control systems, controls, proportional integrative derivative control, PID, PID control, control of a differential drive robot
```

(lx-setup-control-pid)=
# LX: PID Control

```{needget}
- Learning experience computer setup: [](duckiebot-lxs)

- (recommended) A successful Duckiematrix installation: [](the-duckiematrix-first-steps)

- (optional) A "Ready to Go" Duckiebot: [](duckiebot-setup-intro)

- Mathematical model built in Modeling and Kinematics LX: [](lx-setup-mod-kin)
---
- Running the PID Control learning experience.
```

This page describes how to run the PID Control learning experience.

{{ dt_workspace_matrix_lx_warning.format(dt_workspace_note_prefix) }}

```{figure} ../_images/lx-devmanual/lx-control-pid/control-lx-duckiematrix-riding.png
:alt: Riding a virtual Duckiebot in the PID control LX
:width: 70%
:name: duckiebot-lx-control-riding
:align: center

Welcome to the PID control LX! Are you able to autonomously perform basic driving maneuvres in a simple world? Press <kbd>R</kbd> if you get lost to get back to the road!
```

```{admonition} Intended Learning Outcomes
:class: tip
After this learning experience, learners will:
- Understand what a PID controller is, and how each component (P, I, D) affects the closed loop performance of the controlled robot.

- Be able to describe the difference between discrete time and continuous time implementations of derivatives and integrals.

- Write a PID controller for regulating the heading of a Duckiebot, in Python.

- Write a PID controller for regulating the (lateral) position of a Duckiebot, in Python.

- Perform unit tests (i.e., sanity checks) on specific implementation functions.

- Deploy and tune the designed PID controller on virtual and/or physical Duckiebots.
```

## About these learning activities

In this learning experience, you will use the model that we built in the [kinematics and odometry](lx-setup-mod-kin) learning experience. Now we will build a simple controller to make the Duckiebot follow a specified set of actions based on our knowledge of how it moves.

For guided setup instructions, lecture content, and more related to this LX, see [our Self-Driving Cars with Duckietown MOOC on EdX](https://duckietown.com/mooc).

{{ dt_lx_exercise_runtime_note }}

(lx-forking-control-pid)=
## Forking the repository

### 1. Create a fork

Navigate to [the (PID) Control repository](https://github.com/duckietown/lx-control).

Find and press the "Fork" button on the top right:

```{figure} /_images/lx-devmanual/intro/duckietown-lx-forking.png
:alt: how to fork a Duckietown LX repository
:width: 90%
:name: duckiebot-lx-forking-control-pid
:align: center

Fork the LX to be able to make local changes while still being able to receive updates.
```

This will create a new repository at: `<your_github_username>/lx-control`.

### 2. Clone the fork

Clone the fork on your computer, replacing your GitHub username in the command below, and navigate to the new folder:

```shell
git clone git@github.com:<your_github_username>/lx-control
cd lx-control
```

### 3. Configure the upstream repository

Configure the Duckietown version of this repository as the upstream repository to synchronize with your fork.

List the current remote repository for your fork:

```shell
git remote -v
```

Specify a new remote upstream repository:

```shell
git remote add upstream https://github.com/duckietown/lx-control
```

Confirm that the new upstream repository was added to the list:

```shell
git remote -v
```

You can now push your work to your own repository using the standard GitHub workflow, and the beginning of every exercise will prompt you to pull from the upstream repository, updating your exercises to the latest version (if available).

(lx-system-update-control-pid)=
## Keeping your System Up To Date

- 💻 These instructions are for `ente` learning experiences. Ensure your Duckietown Shell is set to an `ente` profile (and not a `daffy` one). You can check your current profile with:

    ```shell
    dts profile list
    ```

    To switch to an ente profile, follow the [Duckietown Manual DTS installation instructions](setup-dts).

- 💻 Pull from the upstream remote to synchronize your fork with the upstream repository:

    ```shell
    git pull upstream ente
    ```

- 💻 Make sure your Duckietown Shell is updated to the latest version:

    ```shell
    pipx upgrade duckietown-shell
    ```

- 💻 Update the shell commands:

    ```shell
    dts update
    ```

- 💻 Update your laptop/desktop:

    ```shell
    dts desktop update
    ```

- 🚙 Update your Duckiebot:

    ```shell
    dts duckiebot update DUCKIEBOT_NAME
    ```

    (where `DUCKIEBOT_NAME` is the name of your physical or virtual Duckiebot.)

(lx-code-editor-lx-control-pid)=
## Launching the Code Editor

{{ dt_lx_dts_code_root_important }}

Making sure you are inside the path of the specific learning experience you want to work on, open the code editor by running:

```shell
dts code editor
```

Wait for a URL to appear on the terminal, then click on it or copy-paste it in the address bar
of your browser to access the code editor. The first thing you will see in the code editor is a version of these instructions. At this point you can start following the LX-specific indications shown in your code editor.

(lx-navigating-notebooks-control-pid)=
## Walkthrough of Notebooks

Inside the code editor, use the navigator sidebar on the left-hand side to navigate to the
`notebooks` directory and open the first notebook.

Follow the instructions on the notebook and work through them in sequence.

In many cases the last notebook will instruct you to write some code inside the
learning experience directory.

Once you have done that you will need to **build** your code before **testing** it.

(lx-matrix-testing-control-pid)=
### Testing with the Duckiematrix

To test your code in the Duckiematrix, attach either a physical or virtual robot to a Duckiematrix Entity. The steps below use a virtual robot; for instructions on attaching a physical robot, see [](introduction-duckiematrix-connect-db-to-remote-engine).

(lx-create-vbot-control-pid)=
#### 1. Creating and starting virtual Duckiebot

You can create one with the command:

```shell
dts duckiebot virtual create --type duckiebot --configuration DB21J ROBOT_NAME
```

where `ROBOT_NAME` is the hostname. It can be anything you like, subject to the [same naming constraints of physical Duckiebots](setup-db-sd-card-flashing-complete). Make sure to remember your robot (host)name for later.

Then you can start your virtual robot with the command:

```shell
dts duckiebot virtual start ROBOT_NAME
```

You should see it with a status `Booting` and finally `Ready` if you look at `dts fleet discover`: 

```text
     | Hardware |   Type    | Model |  Status  | Hostname 
---  | -------- | --------- | ----- | -------- | ---------
ROBOT_NAME |  virtual | duckiebot | DB21J |  Ready   | ROBOT_NAME.local
```

Once you are done for the day, do not forget to stop your virtual robot:

```shell
dts duckiebot virtual stop ROBOT_NAME
```

If in doubt, you can check the status of your virtual scuderia at any time with:

```shell
dts duckiebot virtual list
```

(lx-code-matrix-start-control-pid)=
#### 2. Starting the Duckiematrix with the virtual Duckiebot

Now that your virtual robot is ready, you can start the Duckiematrix. From this exercise directory do:

```shell
dts code start_matrix
```

{{ dt_workspace_start_matrix_split_note.format(dt_workspace_note_prefix) }}

You should see the Unity-based Duckiematrix simulator start up. For more details about using
the Duckiematrix see [](the-duckiematrix-manual).

```{figure} ../_images/lx-devmanual/lx-control-pid/control-lx-duckiematrix-start.png
:alt: Initial screen in the Duckiematrix for the control LX and startup instructions
:width: 70%
:name: duckiebot-lx-control-matrix-start
:align: center

You start as a duckie. Click <kbd>Enter</kbd> to get started. Move with <kbd>W</kbd><kbd>A</kbd><kbd>S</kbd><kbd>D</kbd> and rotate the point of view by moving the mouse, as if you were playing a computer game. Approach the Duckiebot and ride it by pressing <kbd>E</kbd>. 
```

To run the WebGL (browser) version of the Duckiematrix, add the `--browser` flag.

{{ dt_duckiematrix_webgl_browser_note }}

(lx-code-build-control-pid)=
### Building the Code

From inside the learning experience root directory, you can build your code with:

```shell
dts code build -R ROBOT_NAME
```

where `ROBOT_NAME` can be either a physical or virtual robot.

(lx-code-test-control-pid)=
### Testing on a Duckiebot or in the Duckiematrix

🚙 To test your code on your physical Duckiebot you can do:

```shell
dts code workbench -R DUCKIEBOT_NAME
```

💻 To test your code in the Duckiematrix:

```shell
dts code workbench -m -R ROBOT_NAME
```

(note the `-m` flag which means that we are running in the `matrix`.)

In another terminal, you can launch the `noVNC` viewer, which can be useful to interact with the virtual robot in different ways depending on the specific LX:

```shell
dts code vnc -R ROBOT_NAME
```

where `ROBOT_NAME` could be the physical or the virtual robot (use whichever you ran the `dts code workbench` and `dts code build` command with).

## Troubleshooting

{{ dt_lx_code_editor_no_project_trouble }}

{{ dt_lx_virtual_robot_update_trouble }}

{{ dt_lx_vnc_startup_trouble }}

```{trouble}
When I click on `PID Heading` in the noVNC desktop, I do not see the interaction window with `heading ref`, `v_0`, etc.  
---
Enlarge the noVNC window on your computer to see it. It could pop up out of view of the initial window size.
```

```{trouble}
When I click on `PID Heading` in the noVNC desktop, I do not see image in the pre-configured RVIZ window popping up.   
---
Terminate the process in the terminal where you ran `dts code workbench [-m] -R ROBOT_NAME` and run it again after starting the Duckiematrix with `dts start_matrix`.
```
