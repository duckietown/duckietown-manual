(lx-setup-bv)=
# LX: Braitenberg Vehicles

```{seo}
:description: Step by step instructions on how to run the Braitenber Vehicles LX in Duckietown.
:keywords: Duckietown, Duckiebot, LXs, Learning Experiences, Braitenber Vehicles
```

```{needget}
- Learning experience computer setup: [](duckiebot-lxs)
- (reccomended) A successful Duckiematrix installation: [](the-duckiematrix-first-steps)
- (optional) A "Ready to Go" Duckiebot: [](duckiebot-setup-intro)
---
- Running the Braitenberg Vehicles (BV) learning experience.
```

This page describes how to run the Braitenberg Vehicles learning experience.

```{warning}
{{ dt_workspace_matrix_lx_warning.format(dt_workspace_note_prefix) }}
```

```{figure} /_images/lx-devmanual/lx-bv/duckietown-bv-lx-matrix-iso.webp
:alt: Welcome to the Duckiematrix after starting the BV LX
:width: 60%
:name: duckiebot-lx-bv
:align: center

Welcome to the Braitenberg Vehicles LX!
```

```{admonition} Intended Learning Outcomes
:class: tip
In this learning experience, learners will:
- experience the emergence of autonomy from atoms and bits
- design and implement a vision-based sensorimotor connection-based agent to enable simple autonomous behaviors on Duckiebots
- deploy the agent on physical or virtual Duckiebots
- tune the agent to have the Duckiebot avoid a sea of duckies
```

```{note}
This exercise can be run on a [real Duckiebot](https://get.duckietown.com/products/duckiebot-db21?variant=41543707099311) or on a virtual Duckiebot in [the Duckiematrix](the-duckiematrix-first-steps). 
```

For guided setup instructions, lecture content, and more related to this LX, see [our Self-Driving Cars with Duckietown MOOC on EdX](https://duckietown.com/mooc).

(lx-forking-bv)=
## Forking the repository

### 1. Create a fork 

Navigate to [the Braitenberg vehicles repository](https://github.com/duckietown/lx-braitenberg).

Find and press the "Fork" button on the top right:

```{figure} /_images/lx-devmanual/intro/duckietown-lx-forking.png
:alt: how to fork a Duckietown LX repository
:width: 90%
:name: duckiebot-lx-forking-1
:align: center

Fork the LX to be able to make local changes while still being able to receive updates.
```

This will create a new repository at: `<your_github_username>/lx-braitenberg`.

### 2. Clone the fork 

Clone the fork on your computer, replacing your GitHub username in the command below, and navigate to the new folder:

    git clone git@github.com:<your_github_username>/lx-braitenberg
    cd lx-braitenberg
        

### 3. Configure upstream repo 

Configure the Duckietown version of this repository as the upstream repository to synchronize with your fork.

List the current remote repository for your fork,

    git remote -v

Specify a new remote upstream repository,

    git remote add upstream https://github.com/duckietown/lx-braitenberg

Confirm that the new upstream repository was added to the list,

    git remote -v

You can now push your work to your own repository using the standard GitHub workflow, and the beginning of every exercise will prompt you to pull from the upstream repository, updating your exercises to the latest version (if available).

(lx-system-update-bv)=
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

- 🚙 Update your Duckiebot: 

    ```
    dts duckiebot update ROBOTNAME
    ``` 
    
    (where `ROBOTNAME` is the name of your Duckiebot - real or virtual.)

(lx-code-editor-bv)=
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

(lx-navigating-notebooks-bv)=
## Walkthrough of Notebooks

Inside the code editor, use the navigator sidebar on the left-hand side to navigate to the
`notebooks` directory and open the first notebook.

Follow the instructions on the notebook and work through them in sequence.

In many cases the last notebook will instruct you to write some code inside the
learning experience directory. 

Once you have done that you will need to **build** your code before **testing** it.

(lx-matrix-testing-bv)=
### Testing with the Duckiematrix

To test your code in the Duckiematrix you will need a virtual robot attached to an ongoing session. 

(lx-create-vbot-bv)=
#### Creating a virtual Duckiebot

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

Now that your virtual robot is ready, you can start the Duckiematrix. From this exercise directory do:

```
dts code start_matrix
```

```{note}
{{ dt_workspace_start_matrix_split_note.format(dt_workspace_note_prefix) }}
```

You should see the Unity-based Duckiematrix simulator start up. For more details about using
the Duckiematrix see [](the-duckiematrix-manual).

To run the WebGL (browser) version of the Duckiematrix, add the `--browser` flag.

```{note}
For the WebGL (browser) version of the Duckiematrix, if the colors look desaturated, try a different browser.
```

#### Other virtual Duckiebot useful commands

Once you are done for the day, do not forget to stop your virtual robot:

```
dts duckiebot virtual stop [VBOT]
```

If in doubt, you can check the status of your virtual scuderia at any time with:

```
dts duckiebot virtual list
```

(lx-code-build-bv)=
### Building the Code

From inside the learning experience root directory, you can build your code with:

```
dts code build -R ROBOT_NAME
```

where `ROBOT_NAME` can be either a physical or virtual robot. 

(lx-code-test-bv)=
### Testing on a Duckiebot or in the Duckiematrix

To test your code on your real Duckiebot you can do:

```
dts code workbench -R [ROBOT_NAME]
```

To test your code in the Duckiematrix:

```
dts code workbench -m -R [VIRTUAL_ROBOT_NAME]
```

(note the `-m` flag which means that we are running in the `matrix`)

In another terminal, you can launch the `noVNC` viewer, which can be useful to interact with the virtual robot in different ways depending on the specific LX.

```
dts code vnc -R [ROBOT_NAME]
```

where `[ROBOT_NAME]` could be the real or the virtual robot (use whichever you ran the `dts code workbench` and `dts code build` command with).

```{figure} /_images/lx-devmanual/lx-bv/duckiematrix_overhead.png
:alt: Welcome to the Duckiematrix after starting the BV LX
:width: 80%
:name: duckiebot-lx-start-matrix-bv
:align: center

Example Duckiematrix splash screen after starting the Braitenberg Vehicles LX.
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
When running `dts code editor` I get an error: `dts :  No valid DTProject found at '/path/to/lx'`
---
Make sure your are executing the commands from inside a learning experience folder (e.g., `*/lx-control/`)
```

```{trouble}
My virtual robot (named, e.g., `VBOT`) hangs indefinitely when trying to update it.
---
Try to restart it with: `dts duckiebot virtual restart VBOT`
```