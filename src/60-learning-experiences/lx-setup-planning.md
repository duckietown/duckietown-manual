```{seo}
:description: Learn about RRT (randomly exploring random trees) planning and follow step by step instructions to design and deploy a planner in this Duckietown learning experience (LX).
:keywords: Duckietown, Duckiebot, virtual Duckiebot, digital twin, physical Duckiebot, autonomous vehicles, LXs, Learning Experiences, planning, robotics project, hands on learning, RRT, rapidly exploring random trees
```

```{needget}
- Learning experience computer setup: [](duckiebot-lxs)
- (reccomended) A successful Duckiematrix installation: [](the-duckiematrix-first-steps)
- (optional) A "Ready to Go" Duckiebot: [](duckiebot-setup-intro)
---
- Running the Planning learning experience.
```

(lx-setup-planning-rrt)=
# LX: Planning - RRT

In this learning experience, you will build a robot planner designed to have a Duckiebot drive safely in a cluttered environment. We will represent the environment by a set of obstacles (in our simplified case they will be circular and rectangular). The first task will be to figure out how to tell if a robot configuration (pose) collides with an obstacle. From there you can build a planner based on the randomly exploring random trees (RRT) algorithm to find a path from a start configuration to a goal configuration without colliding with anything. 


```{figure} ../_images/lx-devmanual/lx-planning/planning-lx-dtmatrix-splashscreen-topview.jpg
:alt: Duckietown planning LX duckiematrix top view
:width: 60%
:name: duckiebot-lx-planning-dtmatrix-top
:align: center

Welcome to the Planning - RRT LX!
```

```{admonition} Intended Learning Outcomes
:class: tip
After this learning experience, you will:
- understand and model configuration space (C-space) for a Duckiebot
- build and implement a collision checker in C-space
- Review the Rapidly-exploring Random Tree (RRT) planning algorithm
- Create a differential drive steering function as motion primitive for the RRT algorithm
- Implement the RRT algoirthm and test it in the Duckiematrix 
```

```{warning}
{{ dt_workspace_matrix_lx_warning.format(dt_workspace_note_prefix) }}
```

## About these learning activities

For guided setup instructions, lecture content, and more related to this LX, see [our Self-Driving Cars with Duckietown MOOC on EdX](https://duckietown.com/mooc).

(lx-forking-planning)=
## Forking the repository

The recommended way to use [the repository for this LX](https://github.com/duckietown/lx-planning) is to make a fork and then clone that fork. 

This can be done through the GitHub web interface. However, you are also free to simply clone this repository and get started. 

### 1. Create a fork

Navigate to [the lx-planning repository](https://github.com/duckietown/lx-planning).

Find and press the "Fork" button on the top right:

```{figure} /_images/lx-devmanual/intro/duckietown-lx-forking.png
:alt: how to fork a Duckietown LX repository
:width: 90%
:name: duckiebot-lx-forking-planning
:align: center

Fork the LX to be able to make local changes while still being able to receive updates.
```

This will create a new repository at: `<your_github_username>/lx-planning`.

### 2. Clone the fork

Clone the fork on your computer, replacing your GitHub username in the command below, and navigate to the new folder:

    git clone git@github.com:<your_github_username>/lx-planning
    cd lx-planning
        
### 3. Configure the upstream repository

Configure the Duckietown version of this repository as the upstream repository to synchronize with your fork.

List the current remote repository for your fork,

    git remote -v

Specify a new remote upstream repository,

    git remote add upstream https://github.com/duckietown/lx-planning

Confirm that the new upstream repository was added to the list,

    git remote -v

You can now push your work to your own repository using the standard GitHub workflow, and the beginning of every exercise will prompt you to pull from the upstream repository, updating your exercises to the latest version (if available).

(lx-system-update-planning)=
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

(lx-code-editor-lx-planning)=
## Launching the LX through the Code Editor

```{important}
All `dts code` commands should be executed inside the root directory of the learning experience (`cd ./path-to-lxs-in-your-workstation/lx-planning`).
```

### SSL certificate

```{note}
If you have not done so already, set up your local SSL certificate needed to run the learning experience editor with:

    sudo apt install libnss3-tools
    dts setup mkcert
```

```{warning}
If you are running Duckietown inside a [Duckietown Workspace](setup-devcontainer), make sure to [install the certificate for your host machine as well](setup-devcontainer-dts-code-editor). 
```

Open the code editor with:

```
dts code editor [--bind 0.0.0.0]
```

Where the `--bind` flag can be used if using a Duckietown Workspace and the browser is not automatically opening this document. Wait for a URL to appear on the terminal, then click on it or copy-paste it in the address bar of your browser to access the code editor. The first thing you will see in the code editor is this same document, you can continue there.

The first thing you will see in the code editor are a version of these instructions. At this point you can start following the LX-specific indications shown in your code editor.

(lx-navigating-notebooks-planning)=
## Walkthrough of Notebooks

Inside the code editor, use the navigator sidebar on the left-hand side to navigate to the `notebooks` directory and open the first notebook.

Follow the instructions on the notebook and work through them in sequence.

In many cases the last notebook will instruct you to write some code inside the learning experience directory. 

Once you have done that you will need to **build** your code before **testing** it.

(lx-matrix-testing-planning)=
### Testing with the Duckiematrix

To test your code in the Duckiematrix you will need a virtual robot attached to an ongoing session.

(lx-create-vbot-planning)=
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
       | Hardware |   Type    | Model |  Status  |    Hostname 
-----  | -------- | --------- | ----- | -------- | -------------
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

(lx-code-matrix-start-planning)=
#### 2. Starting the Duckiematrix with the virtual Duckiebot

Now that your virtual robot is ready, you can start the Duckiematrix. From this LX directory:

```
dts code start_matrix [--no-renderer]
```

```{note}
{{ "{} keep the `--no-renderer` flag and launch the Duckiematrix renderer from a local terminal outside the dev container with `dts matrix run`.".format(dt_workspace_note_prefix) }}
```

You will see the Unity-based Duckiematrix simulator start up. The startup screen will look like:

```{figure} ../_images/lx-devmanual/lx-planning/planning-lx-dtmatrix-splashscreen-2.jpg
:alt: Duckiematrix splash screen for the Planning - RRT learning experience. 
:width: 90%
:name: duckiebot-lx-planning-rrt-start
:align: center

In this LX you will be greeted by a particular Duckietown with signs and potholes/missing tiles. 
```

Remember that to activate the Duckiematrix window, click anywhere on it and press [ENTER]. You can then at any time press `ESC` to disengage the mouse. 

From here you can move the duckie towards the Duckiebot with the <kbd>W</kbd>, <kbd>A</kbd>, <kbd>S</kbd>, and <kbd>D</kbd> keys, or you can move the camera angle to view the Duckiebot with the mouse. If you are close enough to your Duckiebot, you can jump on with the 'E' key. You can then drive the Duckiebot around with the <kbd>W</kbd>, <kbd>A</kbd>, <kbd>S</kbd>, and <kbd>D</kbd> keys. All available keyboard commands are summarized in the "Settings" tab at the bottom left of the Duckiematrix window. 

If you get very lost from the road and you want to come back, you can do so with the <kbd>R</kbd> key. 

<!--
To run the WebGL (browser) version of the Duckiematrix, add the `--browser` flag.

```{note}
For the WebGL (browser) version of the Duckiematrix, if the colors look desaturated, try a different browser.
```
-->

(lx-code-build-planning)=
### Building the Code

From inside the learning experience root directory, you can build your code with:

```
dts code build -R ROBOT_NAME
```

where `ROBOT_NAME` can be either a physical or virtual robot.

(lx-code-test-planning)=
### Deploying the code on a (physical or virtual) Duckietown robot

🚙 To test your code on your real Duckiebot you can do:

```
dts code workbench -R ROBOT_NAME
```

💻 To test your code on a virtual robot in the Duckiematrix:

```
dts code workbench -m -R VIRTUAL_ROBOT_NAME
```

```{note}
The `-m` flag indicates we are targeting a virtual robot in the `matrix`.
```

### Open the noVNC GUI

In another terminal, you can launch the `noVNC` viewer for this LX and open RViz. 

```
dts code vnc -R ROBOT_NAME
```

where `ROBOT_NAME` could be the real or the virtual robot (use whichever you ran the `dts code workbench` and `dts code build` command with).

## Troubleshooting

```{trouble}
When running `dts code editor` I get an error: `dts :  No valid DTProject found at '/path/to/lx'`
---
Make sure your are executing the commands from inside a learning experience folder (e.g., `*/lx-planning/`)
```

```{trouble}
My virtual robot (named, e.g., `VBOT`) hangs indefinitely when trying to update it.
---
Try to restart it with: `dts duckiebot virtual restart VBOT`
```