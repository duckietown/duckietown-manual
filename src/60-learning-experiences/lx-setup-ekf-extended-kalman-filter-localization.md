(lx-setup-ekf-localization)=
# LX: Localization - Extended Kalman Filter (EKF)

```{seo}
:description: Step by step instructions on how to run the Extended Kalman Filtering Localization learning experience (LX) in Duckietown.
:keywords: Duckietown, Duckiebot, LXs, Learning Experiences, localization, state estimation, kalman filter, extended kalman filter, particle filter, histogram filter, hands on learning, sensor fusion
```

```{needget}
- Learning experience computer setup: [](duckiebot-lxs)
- (reccomended) A successful Duckiematrix installation: [](the-duckiematrix-first-steps)
- (optional) A "Ready to Go" Duckiebot: [](duckiebot-setup-intro)
---
- Running the Localization - Extended Kalman Filter learning experience.
```

This learning experience is about how we should use the data streaming through the sensors, together with the knowledge of our surroundings, to estimate our state. The so-called optimal approach to this is the Bayes filter, however, this approach is computationally intractable in all but the simplest settings. We will explore several approximations to the Bayes filter. Namely, the Kalman filter, the particle filter, and the histogram filter. Each has its own assumptions and conditions under which it is most applicable. Finally, you will program an extended Kalman filter, or EKF, to localize your Duckiebot using the data from the wheel encoders and the AprilTag fiducial markers that you observe at known locations.

```{figure} ../_images/lx-devmanual/lx-ekf-localization/Histogram.png
:alt: Duckietown histogram filter representation for Duckiebot pose estimation
:width: 60%
:name: duckiebot-lx-ekf-localization-histogram
:align: center

Welcome to the EKF - Localization LX!
```

```{admonition} Intended Learning Outcomes
:class: tip
After this learning experience, you will:
- learn about Kalman filters: from the theory to implementation details
- learn about Particle filters: from the theory to implementation details
- learn about Histogram filters: from the theory to implementation details
- be able to evaluate advantages and disadvantages of each approach given different scenarios
- be able to design, tune and test an extended Kalman Filter for achieving map-based localization, fusing wheel encoder and AprilTag-based pose measurement. 
```

```{warning}
{{ dt_workspace_matrix_lx_warning.format(dt_workspace_note_prefix) }}
```

## About these learning activities

For guided setup instructions, lecture content, and more related to this LX, see [our Self-Driving Cars with Duckietown MOOC on EdX](https://duckietown.com/mooc).

```{note}
This exercise can be run on a virtual Duckiebot in [the Duckiematrix](the-duckiematrix-first-steps), and on a [real Duckiebot](https://get.duckietown.com/products/duckiebot-db21?variant=41543707099311) with off-board agent workflow. On-board agent workflow is work in progress. 
```

(lx-forking-ekf-localization)=
## Forking the repository

### 1. Create a fork

Navigate to [the lx-ekf-localization repository](https://github.com/duckietown/lx-ekf-localization).

Find and press the "Fork" button on the top right:

```{figure} /_images/lx-devmanual/intro/duckietown-lx-forking.png
:alt: how to fork a Duckietown LX repository
:width: 90%
:name: duckiebot-lx-forking-ekf-localization
:align: center

Fork the LX to be able to make local changes while still being able to receive updates.
```

This will create a new repository at: `<your_github_username>/lx-ekf-localization`.

### 2. Clone the fork

Clone the fork on your computer, replacing your GitHub username in the command below, and navigate to the new folder:

    git clone git@github.com:<your_github_username>/lx-ekf-localization
    cd lx-ekf-localization
        
### 3. Configure the upstream repository

Configure the Duckietown version of this repository as the upstream repository to synchronize with your fork.

List the current remote repository for your fork,

    git remote -v

Specify a new remote upstream repository,

    git remote add upstream https://github.com/duckietown/lx-ekf-localization

Confirm that the new upstream repository was added to the list,

    git remote -v

You can now push your work to your own repository using the standard GitHub workflow, and the beginning of every exercise will prompt you to pull from the upstream repository, updating your exercises to the latest version (if available).

(lx-system-update-ekf-localization)=
## Keeping your System Up To Date

- 💻 These instructions are for `ente` learning experiences. Ensure your Duckietown Shell is set to an `ente` profile (and not a `daffy` one). You can check your current profile with: 
    
    ```
    dts profile list
    ```

    To switch to an ente profile, follow the [Duckietown Manual DTS installation instructions](setup-dts).

- 💻 Pull from the upstream remote to synch your fork with the upstream repo: 

    ```
    git pull upstream ente
    ```

- 💻 Make sure your Duckietown Shell is updated to the latest version: 

    ```
    pipx upgrade duckietown-shell
    ```

- 💻 Update the shell commands: 

    ```
    dts update
    ```

- 💻 Update your laptop/desktop: 

    ```
    dts desktop update
    ```

- 🚙 Update your Duckiebot (even if it is a virtual one): 

    ```
    dts duckiebot update ROBOTNAME
    ``` 
    
    (where `ROBOTNAME` is the name of your Duckiebot - real or virtual.)

(lx-code-editor-lx-ekf-localization)=
## Launching the Code Editor

```{important}
All `dts code` commands should be executed inside the root directory of the learning experience.
```

Making sure you are inside the path of this learning experience (`cd ./path-to-lxs-in-your-workstation/lx-ekf-localization`), then open the code editor:

```
dts code editor
```

Wait for a URL to appear on the terminal, then click on it or copy-paste it in the address bar of your browser to access the code editor. 

The first thing you will see in the code editor are a version of these instructions. At this point you can start following the LX-specific indications shown in your code editor.

(lx-navigating-notebooks-ekf-localization)=
## Walkthrough of Notebooks

Inside the code editor, use the navigator sidebar on the left-hand side to navigate to the
`notebooks` directory and open the first notebook.

Follow the instructions on the notebook and work through them in sequence.

In many cases the last notebook will instruct you to write some code inside the
learning experience directory. 

Once you have done that you will need to **build** your code before **testing** it.

(lx-matrix-testing-ekf-localization)=
### Testing with the Duckiematrix

To test your code in the Duckiematrix you will need a virtual robot attached to an ongoing session.

(lx-create-vbot-ekf-localization)=
#### 1. Creating and starting virtual Duckiebot

If you have not done so already (e.g., for a different LX), you can create a virtual Duckiebot with the command:

```
dts duckiebot virtual create --type duckiebot --configuration DB21J [VBOT]
```

where `[VBOT]` is the hostname. It can be anything you like, subject to the [same naming constraints of physical Duckiebots](setup-db-sd-card-flashing-complete).

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

If in doubt if any of your virtual Duckiebots in running or not, you can check the status of your virtual scuderia at any time with:

```
dts duckiebot virtual list
```

(lx-code-matrix-start-ekf-localization)=
#### 2. Starting the Duckiematrix with the virtual Duckiebot

Now that your virtual robot is ready, you can start the Duckiematrix. From this LX directory:

```
dts code start_matrix [--no-renderer]
```

```{note}
{{ "{} keep the `--no-renderer` flag and launch the Duckiematrix renderer from a local terminal outside the dev container with `dts matrix run`.".format(dt_workspace_note_prefix) }}
```

You will see the Unity-based Duckiematrix simulator start up. The startup screen will look like:

```{figure} ../_images/lx-devmanual/lx-ekf-localization/duckiematrix-start.png
:alt: Duckiematrix splash screen for the EKF Localization learning experience. 
:width: 70%
:name: duckiebot-lx-ekf-localization-segmentation
:align: center

In this LX you will be greeted by a slightly more complex Duckietown than in previous ones. 
```

From here you can click anywhere on the window and click <kbd>ENTER</kbd> to make it become active, and then move the duckie towards the Duckiebot with the <kbd>w</kbd>, <kbd>a</kbd>, <kbd>s</kbd>, and <kbd>d</kbd> keys, and you can move the 
camera angle to view the Duckiebot with the mouse. 

If you are close enough to your Duckiebot, you can board it with the <kbd>E</kbd> key, which should look like

```{figure} ../_images/lx-devmanual/lx-ekf-localization/duckiematrix-riding.png
:alt: Duckiematrix splash screen for the EKF Localization learning experience. 
:width: 70%
:name: duckiebot-lx-ekf-localization-segmentation
:align: center

After boarding your Duckiebot you will be able to move it around manually with <kbd>WASD</kbd>.
```

You can then you can drive the Duckiebot around with the 'w', 'a', 's', and 'd' keys. You will notice that this map includes traffic signs with fiducial markers ([AprilTags](https://april.eecs.umich.edu/software/apriltag)) that we are going to use in this LX to help localize your robot.

If you get very lost from the road and you want to come back, you can do so with the <kbd>R</kbd> key. 

```{note}
You should reset your Duckiebot's position with <kbd>R</kbd> before each test since the initial state estimate coincides with the reset position.
```

To run the WebGL (browser) version of the Duckiematrix, add the `--browser` flag.

```{note}
For the WebGL (browser) version of the Duckiematrix, if the colors look desaturated, try a different browser.
```

(lx-code-build-ekf-localization)=
### Building the Code

From inside the learning experience root directory, you can build your code with:

```
dts code build -R ROBOT_NAME
```

where `ROBOT_NAME` can be either a physical or virtual robot.

(lx-code-test-ekf-localization)=
### Testing on a Duckiebot or in the Duckiematrix

🚙 To test your code on your real Duckiebot you can do:

```
dts code workbench -R ROBOT_NAME
```

💻 To test your code on a virtual robot in the Duckiematrix:

```
dts code workbench -m -R VIRTUAL_ROBOT_NAME
```

(note the `-m` flag which means that we are running in the `matrix`.)

In another terminal, you can launch the `noVNC` viewer for this exercise and open RViz. 

```
dts code vnc -R ROBOT_NAME
```

where `ROBOT_NAME` could be the real or the virtual robot (use whichever you ran the `dts code workbench` and `dts code build` command with).

This will show you your published pose estimate (blue arrow with a covariance ellipse in purple) as well the ground truth pose of the robot (red arrow which should be inside the ellipse if your implementation is correct). 

You will also see markers that correspond to the AprilTag traffic signs in the map. As each one is detected by your camera you will see it change color from green to blue. At initialization, it should like this:

```{figure} ../_images/lx-devmanual/lx-ekf-localization/rviz.png
:alt: rviz initialization of Duckietown localization LX
:width: 70%
:name: duckiebot-lx-ekf-localization-rviz
:align: center


```

You can also look at an image that shows the tags that are being detected. It is published on the topic `/ROBOT_NAME/detections/image/compressed` (for example you can view with `rqt_image_viewer`).

This output should look like this:

```{figure} ../_images/lx-devmanual/lx-ekf-localization/apriltag-detections.png
:alt: Duckietown EKF localization LX AprilTag detections
:width: 70%
:name: duckiebot-lx-ekf-localization-april-tag-detections
:align: center

AprilTag detections. 
```

You may also use the keyboard controller to pilot your robot and test that the localization performance
of your Duckiebot as it moves.

## Troubleshooting

```{trouble}
When running `dts code editor` I get an error: `dts :  No valid DTProject found at '/path/to/lx'`
---
Make sure your are executing the commands from inside a learning experience folder (e.g., `*/lx-ekf-localization/`)
```

```{trouble}
My virtual robot (named, e.g., `VBOT`) hangs indefinitely when trying to update it.
---
Try to restart it with: `dts duckiebot virtual restart VBOT`
```