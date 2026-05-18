```{seo}
:description: Step by step instructions and troubleshooting tips for running a fully fledged Duckietown environment in a development container, enabling smooth operations on macOS (including M-chips) and Windows.
:keywords: duckietown setup, Dev Container, Duckietown Workspaces, duckietown macOS, duckietown windows
```

```{warning}
Duckietown Workspaces are currently under development and released in Beta mode. Most functionalities are currently working and have been extensively tested on macOS and on Windows. 
Please report all bugs in the Duckietown Slack community channel [#beta-devcontainer](https://duckietown.slack.com/archives/C09KJ1QC46R) or by email at [info@duckietown.com](mailto:info@duckietown.com). 
```

(setup-devcontainer)=
# Using Duckietown Workspaces (Beta)

This page describes how to run Duckietown code inside a [Development (Dev) Container](https://containers.dev/), providing a functional environment inside of [Visual Studio Code](https://code.visualstudio.com/).

```{note}
This is the only workflow for running Duckietown code on an Apple Silicon (M-series) Mac and on Windows.
```

## Host System Container Installation

In order to run Duckietown in a Dev Container, you need to install the following software on your host system, depending on your operating system:

:::::{tab-set}

::::{tab-item} macOS

On macOS, we will be installing [Orbstack](https://orbstack.dev/), a lightweight container runtime that supports Apple Silicon (M-series) Macs.

```{attention}
If you have Docker Desktop installed, [uninstall it](https://docs.docker.com/desktop/uninstall/) and reboot.
```

To install Orbstack:

1. [Download the Orbstack `.dmg` file](https://orbstack.dev/download).

2. Navigate to your `Downloads` folder.

3. Double-click the `.dmg` file.

4. Move the application to your `Applications` folder.

```{tip}
If your Mac refuses to open an application because it is not trusted, hold down the `option` key and right-click it, then select `Open`. Your Mac will inform you that the application is not trusted but will allow you to open it.
```

```{attention}
There is a known bug for which `dts fleet discover` will not find physical robots on the same network. Nonetheless, all other functions (e.g., pinging, updating, controlling, etc.) are unaffected by this bug.  
```

::::

::::{tab-item} Windows

```{admonition} Duckietown Workspace: Windows 11 installation tutorial
<div style="padding:56.25% 0 0 0;position:relative;">
<iframe 
  src="https://www.youtube.com/embed/0vqfccIVb5Q"
  style="position:absolute;top:0;left:0;width:100%;height:100%;"
  frameborder="0"
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
  allowfullscreen>
</iframe>
</div>

This video is a third-party contribution kindly created by Irina Zheleznova, Senior Lecturer at [Academy of Civil Aviation, Almaty, Kazakhstan](https://caa.edu.kz/), and her students [Zhanibek Kenshilik](https://cutt.ly/zhanibek-kenshilik-linkedin) and [Andrey Shilovsky](https://cutt.ly/andrey-shilovsky-linkedin).
```

On Windows, we will be installing WSL with Ubuntu and Docker Desktop.

```{attention}
The following instructions use Windows Terminal, which comes preinstalled with Windows 11 version 22H2 and later. If you do not have it installed, you can download it from the [Microsoft Store](https://aka.ms/terminal).
```

To install WSL and Ubuntu on Windows:

1. Install WSL by opening up the Windows Terminal and running

    ```
    wsl --install
    ```

2. Reboot your computer after the installation is complete.

3. Install Ubuntu by running

    ```
    wsl --install ubuntu
    ```

4. Follow on-screen instructions to set up an account in Ubuntu on WSL.

Installing Docker Desktop:

1. Install Docker Desktop from https://www.docker.com/ 

2. Start Ubuntu by running `wsl` in the Windows Terminal.

```{important}
From now on, cloning and running the devcontainer should be done from the `wsl` terminal, except when otherwise specified.
```

::::
:::::

## Installing Visual Studio Code

To install Visual Studio Code:

1. [Download the appropriate VS Code `.zip` file](https://code.visualstudio.com/download).

2. Navigate to your `Downloads` folder.

3. Double-click the `.zip` file.

4. (On Mac) Move the application to your `Applications` folder.

## Installing the necessary VS Code extensions

To install the Remote - Containers extension in VS Code:

1. Open VS Code.
2. Click on the `Extensions` icon in the left sidebar (or press `Ctrl+Shift+X` on Windows or `Cmd+Shift+X` on macOS).
3. In the search bar, type `Remote - Containers`.
4. Click on the `Install` button next to the `Remote - Containers` extension by Microsoft.
5. (**Windows only**) Follow the same instructions to also install the `WSL` extension.

## Cloning the `dt-env-developer` repository

To clone the `dt-env-developer` repository, run:

```shell
git clone git@github.com:duckietown/dt-env-developer.git
```

```{attention}
Ignore the instructions in the `README` of this repository.

(Windows) If you are on Windows, make sure to run the above command from the `wsl` terminal.
```

## Running the Dev Container in VS Code

To run the Dev Container in VS Code:

1. Open VS Code and navigate to the `dt-env-developer` folder (`File` -> `Open Folder...` -> `/path/to/dt-env-developer`). You should see a popup appear in the bottom-right corner of your screen containing the message "Folder contains a Dev Container configuration file. Reopen folder to develop in a container ([learn more](https://aka.ms/vscode-remote/docker)).".

2. Click the `Reopen in Container` button.

3. (Optional) Click the `Reading Dev Container Configuration (show log)` link.

```{note}
The first time you load the Dev Container it may take some time as it is building the environment.
```

```{note}
To create a new local integrated terminal (outside the Dev Container), open the VS Code Command Palette (`Shift+Cmd+P` on macOS or `Shift+Ctrl+P` on Windows), enter `Terminal: Create New Integrated Terminal (Local)` and press `Enter`.
```

## Setting up the Duckietown Shell

To set up the Duckietown Shell inside the Dev Container, follow [these instructions](dt-account-set-token).

To set up the Duckietown Shell outside the Dev Container, [install Python 3.10/3.11/3.12](https://www.python.org/downloads/) and follow [these instructions](setup-dts).

```{attention}
If a popup asking you to input your credentials appears, you should do so and then click `Always Allow`. 
```

(devcontainer-running-matrix-renderer)=
## Running the Duckiematrix

The procedure for running the Duckiematrix will be slightly different in this workflow. In short, you
will run the `Engine` and `Renderer` inside and outside the Dev Container, respectively.

To start the `Engine`, run the following command inside the Dev Container:

```shell
dts matrix engine run --sandbox --verbose
```

```{note}
If you are using the Duckiematrix in the context of an LX, [launch the engine with dts code instead](caveat-devcontainer-lx).
```

To start the `Renderer` and connect it to the `Engine` running inside the Dev Container, run the following command outside the Dev Container:

```shell
dts matrix run
```

```{note}
To run the Linux version of the Duckiematrix on Windows, add `--os-family linux` to the above command.
```

To run the WebGL (browser) version of the Duckiematrix, add the `--browser` flag to the above command or run the following command inside the Dev Container:

```shell
dts matrix run --standalone --sandbox --verbose --browser
```

```{note}
For the WebGL (browser) version of the Duckiematrix, if the colors look desaturated, try a different browser.
```

## Caveats

### Accessing a Virtual Robot's Dashboard

To access a Virtual Robot's `Dashboard`, open the `noVNC` virtual desktop by navigating to [localhost:6080](http://localhost:6080). After connecting to the desktop, click on the little triangular icon in the bottom left corner, and then on `Web Browser`. Once the browser is up, proceed as if you were using a physical Duckiebot (i.e., start the virtual Duckiebot, then navigate to `robotname.local`.)

```{figure} ../_images/setup/devcontainer/devcontainer-dashboard-1-1.png
:alt: how to get to the Duckiebot dashboard through a devcontainer
:width: 90%
:name: duckiebot-dashboard-devcontainer-1
:align: center

Connecting to a virtual Duckiebot Dashboard inside a workspace requires a few extra steps.
```

```{figure} ../_images/setup/devcontainer/devcontainer-dashboard-2.png
:alt: virtual duckiebot inside devcontainer dashboard
:width: 90%
:name: duckiebot-dashboard-devcontainer-2
:align: center

Accessing the Dashboard of a virtual Duckiebot inside a devcontainer. 
```

### Accessing the Duckietown Viewer Apps

```{note}
`Duckietown Viewer` applications (i.e., `Image Viewer`, `Keyboard Controller`, etc.) may not work as expected, due to limitations with GUI applications in Docker containers.
```

To open the `Image Viewer` in your browser, run the following command, where `ROBOT_NAME` is the name of your robot:

```shell
dts duckiebot image_viewer ROBOT_NAME --browser
```

To open the `Image Viewer` in the `noVNC` virtual desktop, run the following command after navigating to [localhost:6080](http://localhost:6080), where `ROBOT_NAME` is the name of your robot:

```shell
dts duckiebot image_viewer ROBOT_NAME
```

### Attaching a Duckietown robot to the Duckiematrix

To attach a Duckietown robot to the Duckiematrix, run the following command, where `ROBOT_NAME` is the name of your robot and `ENGINE_LOCAL_NETWORK_ADDRESS` is the LAN IP address of the `Engine` (not `localhost`):

```shell
dts matrix attach ROBOT_NAME -e ENGINE_LOCAL_NETWORK_ADDRESS ENTITY_NAME
```

The `ENGINE_LOCAL_NETWORK_ADDRESS` will be shown in the terminal after starting the engine. The `ENTITY_NAME` default is `map_0/vehicle_0`. A working example could be therefore:

```shell
dts matrix attach ROBOTNAME -e 192.168.139.2 map_0/vehicle_0
```

### Running `dts code editor`

To be able to run `dts code editor`, you need to install `mkcert` on your host system:

`````{tab-set}

````{tab-item} macOS


1. Run `brew install mkcert` or [download the `darwin` binary for your system's architecture](https://github.com/FiloSottile/mkcert/releases/tag/v1.4.4).

2. Run `mkcert -install` (to install the local CA in your system).

````


````{tab-item} Windows

1. Download mkcert for Windows from [this link](https://dl.filippo.io/mkcert/v1.4.4?for=windows/amd64), saving it to your Downloads folder.

2. Then, open the Windows Terminal and run:

    ```
    .\Downloads\mkcert-v1.4.4-windows-amd64.exe --install
    ```

3. Select `Yes` in the prompt.
4. In the Ubuntu terminal, open the `~/.bashrc` file with a text editor, e.g., by running `nano ~/.bashrc`, and append the following lines at the end of the file:

    ```bash
    WINUSER=$(powershell.exe '$env:USERNAME' | tr -d '\r')
    export MKCERT_PATH="/mnt/c/Users/$WINUSER/AppData/Local/mkcert"
    ```

5. Save and exit the text editor (in `nano`, press `Ctrl+X`, `Enter`, then `Enter`).

6. Finally, run `source ~/.bashrc` to update the current shell or open a new `wsl` terminal window.
````
`````

(caveat-devcontainer-lx)=
### DT Workspaces - Duckiematrix for LXs

To run the Duckiematrix for `LXs`, run the following command to start the `Engine`:

```shell
dts code start_matrix --no-renderer
```

and then [attach the `Renderer`](devcontainer-running-matrix-renderer) launching it from the host machine.
