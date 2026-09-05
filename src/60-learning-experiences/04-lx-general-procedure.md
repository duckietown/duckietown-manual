```{seo}
:description: Step-by-step instructions for setting up your working environment to work with Duckietown learning experiences (LXs).
:keywords: Duckietown, Duckiebot, LXs, Learning Experiences, Computer setup
```

(duckiebot-lxs)=
# General Procedure for Running Learning Experiences

```{needget}
- A computer with `dts` installed and correctly set up: [](setup-dts)

- (recommended) A successful Duckiematrix installation: [](the-duckiematrix-first-steps)

- (optional) A "Ready to Go" Duckiebot: [](duckiebot-setup-intro)
---
- A computer ready to run any Duckietown learning experience
```

This page describes the setup and general workflow for Duckietown learning experiences. Specific instructions for each available LX are detailed in the following pages of this manual. The following LXs are currently supported:

{{ dt_workspace_matrix_lx_warning.format(dt_workspace_note_prefix) }}

(ente-supported-lxs)=
## Currently supported `ente` LXs

```{tableofcontents}
```

```{note}
- to create your own LXs, see: [](creating-new-lxs).

- to share your LXs, reach out to [info@duckietown.com](mailto:info@duckietown.com) 
```

(lx-forking)=
## Forking the LX Repositories

The recommended way to use [the repository for each LX](lx-overview) is to make a fork and then clone that fork. Forking can be done through the GitHub web interface and allows the creation of a personal, local copy that is nevertheless synchronized with upstream Duckietown code.

To create and configure a fork:

1. **Create a fork**: Navigate to the repository of interest, for example: [the Braitenberg vehicles repository](https://github.com/duckietown/lx-braitenberg). All LXs URLs have the same format: `https://github.com/duckietown/lx-<lx-name>`

    Find and press the "Fork" button on the top right:

    ```{figure} ../_images/lx-devmanual/intro/duckietown-lx-forking.png
    :alt: how to fork a Duckietown LX repository
    :width: 90%
    :name: duckiebot-lx-forking-4
    :align: center

    Fork the LX to be able to make local changes while still being able to receive updates.
    ```

    This will create a new repository at: `<your_github_username>/lx-<lx-name>`.

2. **Clone the fork**: clone the fork on your computer, replacing your GitHub username in the command below, and navigate to the new folder:

    ```shell
    git clone git@github.com:<your_github_username>/lx-<lx-name>
    cd lx-<lx-name>
    ```

3. **Configure upstream repo**: configure the Duckietown version of this repository as the upstream repository to synchronize with your fork.

    List the current remote repository for your fork:

    ```shell
    git remote -v
    ```

    Specify a new remote upstream repository:

    ```shell
    git remote add upstream https://github.com/duckietown/lx-<lx-name>
    ```

    Confirm that the new upstream repository was added to the list:

    ```shell
    git remote -v
    ```

    You can now push your work to your own repository using the standard GitHub workflow, and the beginning of every exercise will prompt you to pull from the upstream repository, updating your exercises to the latest version.

However, you are also free to simply clone this repository and get started.

(lx-system-update)=
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

(lx-ssl-setup)=
## SSL Certificate setup

```{note}
You only need to run this once the first time you run an LX on a new laptop
```

We use SSL certificates and TLS encryption to guarantee the highest standard of safety and privacy. Set up a local SSL certificate needed to run the LX editor inside your browser:

```shell
sudo apt install libnss3-tools
dts setup mkcert
```

```{note}
{{ "{} install `mkcert` on the host system by following [the workspace setup instructions](setup-devcontainer) instead of running these commands inside the Dev Container.".format(dt_workspace_note_prefix) }}
```

(lx-code-editor)=
## Launching the Code Editor

{{ dt_lx_dts_code_root_important }}

Making sure you are inside the path of the specific learning experience you want to work on, open the code editor by running:

```shell
dts code editor [--bind 0.0.0.0]
```

Where the `--bind` flag can be used if using a Duckietown Workspace and the browser is not automatically opening this document.

Wait for a URL to appear on the terminal, then click on it or copy-paste it in the address bar of your browser to access the code editor. The first thing you will see in the code editor is a version of these instructions specific to the LX you are running. You can generally start following the LX-specific indications shown in your code editor and stop reading here.

(lx-navigating-notebooks)=
## Walkthrough of Notebooks

Inside the code editor, use the navigator sidebar on the left-hand side to navigate to the `notebooks` directory and open the first notebook.

Follow the instructions on the notebook and work through them in sequence.

In many cases the last notebook will instruct you to write some code inside the learning experience directory.

Once you have done that you will need to **build** your code before **testing** it.

(lx-matrix-testing)=
### Testing with the Duckiematrix

To test your code in the Duckiematrix, attach either a physical or virtual robot to a Duckiematrix Entity. The steps below use a virtual robot; for instructions on attaching a physical robot, see [](introduction-duckiematrix-connect-db-to-remote-engine).

(lx-create-vbot)=
#### 1. Creating and starting virtual Duckiebot

If you have not done so already (e.g., for a different LX), you can create a virtual Duckiebot with the command:

```shell
dts duckiebot virtual create --type duckiebot --configuration DB21J ROBOT_NAME
```

where `ROBOT_NAME` is the hostname. It can be anything you like, subject to the [same naming constraints of physical Duckiebots](setup-db-sd-card-flashing-complete).

Then you can start your virtual robot with the command:

```shell
dts duckiebot virtual start ROBOT_NAME
```

You should see it with a status `Booting` and finally `Ready` if you look at `dts fleet discover`:

```text
       | Hardware |   Type    | Model |  Status  |   Hostname 
------ | -------- | --------- | ----- | -------- | ------------
ROBOT_NAME |  virtual | duckiebot | DB21J |  Ready   | ROBOT_NAME.local
```

(lx-code-matrix-start-planning)=
#### 2. Starting the Duckiematrix with the virtual Duckiebot

`````{tab-set}

````{tab-item} Ubuntu

Now that your virtual robot is ready, you can start the Duckiematrix. From  the LX directory:

```shell
dts code start_matrix
```

````

````{tab-item} Duckietown Workspace

{{ dt_workspace_start_matrix_split_note.format(dt_workspace_note_prefix) }}

````

`````

You should see the Unity-based Duckiematrix simulator start up. For more details about using the Duckiematrix see [](the-duckiematrix-manual).

```{figure} /_images/lx-devmanual/lx-bv/duckiematrix_overhead.png
:alt: Welcome to the Duckiematrix after starting the BV LX
:width: 80%
:name: duckiebot-lx-start-matrix
:align: center

Example Duckiematrix splash screen after starting the Braitenberg Vehicles LX.
```

Remember that to activate the Duckiematrix window, click anywhere on it and press [ENTER]. You can then at any time press `ESC` to disengage the mouse.

From here you can move the duckie towards the Duckiebot with the <kbd>W</kbd>, <kbd>A</kbd>, <kbd>S</kbd>, and <kbd>D</kbd> keys, or you can move the camera angle to view the Duckiebot with the mouse. If you are close enough to your Duckiebot, you can jump on with the 'E' key. You can then drive the Duckiebot around with the <kbd>W</kbd>, <kbd>A</kbd>, <kbd>S</kbd>, and <kbd>D</kbd> keys. All available keyboard commands are summarized in the "Settings" tab at the bottom left of the Duckiematrix window.

If you get very lost from the road and you want to come back, you can do so with the <kbd>R</kbd> key.

To run the WebGL (browser) version of the Duckiematrix, add the `--browser` flag.

{{ dt_duckiematrix_webgl_browser_note }}

(lx-stop-list-vbot)=
#### Other virtual Duckiebot useful commands

Once you are done for the day, do not forget to stop your virtual robot:

```shell
dts duckiebot virtual stop ROBOT_NAME
```

If in doubt, you can check the status of your virtual scuderia at any time with:

```shell
dts duckiebot virtual list
```

(lx-code-build)=
### Building the Code

From inside the learning experience root directory, you can build your code with:

```shell
dts code build -R ROBOT_NAME
```

where `ROBOT_NAME` can be either a physical or virtual robot.

(lx-code-test)=
### Deploying the code on a (physical or virtual) Duckietown robot

To test your code on your physical Duckiebot you can do:

```shell
dts code workbench -R DUCKIEBOT_NAME
```

To test your code in the Duckiematrix:

```shell
dts code workbench -m -R ROBOT_NAME
```

{{ dt_lx_matrix_target_note }}

(lx-code-novnc)=
### LX specific interaction GUI: `noVNC`

In another terminal, you can launch the `noVNC` viewer, which can be useful to interact with the virtual robot in different ways depending on the specific LX:

```shell
dts code vnc -R ROBOT_NAME
```

where `ROBOT_NAME` could be the physical or the virtual robot (use whichever you ran the `dts code workbench` and `dts code build` command with).

## Troubleshooting

If you run into any issues while building the image, you can search the troubleshooting symptoms below or
reference the [](how-to-get-help) section of this manual.

{{ dt_lx_code_project_metadata_trouble }}

{{ dt_lx_code_editor_no_project_trouble }}

{{ dt_lx_virtual_robot_update_trouble }}
