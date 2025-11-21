```{seo}
:description: Step by step instructions and troubleshooting tips for running a fully fledged Duckietown environment in a development container, enabling smooth operations on macOS (including M-chips) and Windows.
:keywords: duckietown setup, Dev Container, Duckietown Workspaces, duckietown macOS, duckietown windows
:keywords: duckietown setup, Dev Container, Duckietown Workspaces, duckietown macOS, duckietown windows
```

```{warning}
This feature is currently under development and is released in Beta mode. Most functionalities are currently working and have been extensively tested on macOS, but not on Windows. Please report all bugs in the Duckietown Slack community channel [#beta-devcontainer](https://duckietown.slack.com/archives/C09KJ1QC46R) or by email at [info@duckietown.com](mailto:info@duckietown.com). 
```

(setup-devcontainer)=
# Using Duckietown Workspace (Beta)
# Using Duckietown Workspace (Beta)

This page describes how to run Duckietown code inside a [Development (Dev) Container](https://containers.dev/), providing a functional environment inside of [Visual Studio Code](https://code.visualstudio.com/).

```{note}
This is the only workflow for running Duckietown code on an Apple Silicon (M-series) Mac and on Windows.
This is the only workflow for running Duckietown code on an Apple Silicon (M-series) Mac and on Windows.
```

## Host System Container Runtime Installation

In order to run Duckietown in a Dev Container, you need to install the following software on your host system, depending on your operating system:

:::::{tab-set}

::::{tab-item} macOS

On macOS we will be installing [Orbstack](https://orbstack.dev/), a lightweight container runtime that supports Apple Silicon (M-series) Macs.
## Host System Container Runtime Installation

In order to run Duckietown in a Dev Container, you need to install the following software on your host system, depending on your operating system:

:::::{tab-set}

::::{tab-item} macOS

On macOS we will be installing [Orbstack](https://orbstack.dev/), a lightweight container runtime that supports Apple Silicon (M-series) Macs.

```{attention}
If you have Docker Desktop installed, [uninstall it](https://docs.docker.com/desktop/uninstall/) and reboot.
```

To install Orbstack:

1. [Download the Orbstack `.dmg` file](https://orbstack.dev/download).

2. Navigate to your `Downloads` folder.

3. Double-click the `.dmg` file.

4. Move the application to your `Applications` folder.

```{tip}
If your Mac refuses to open an application because it is not trusted, hold down the `option` key and right-click
If your Mac refuses to open an application because it is not trusted, hold down the `option` key and right-click
it, then select `Open`. Your Mac will inform you that the application is not trusted but will allow you to open it.
```

::::

::::{tab-item} Windows

On Windows we will be installing WSL with Ubuntu and Docker Desktop.

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

4. Follow onscreen instructions to setup an account in Ubuntu on WSL.

Installing Docker Desktop

1. Install docker desktop from https://www.docker.com/ 

2. Start ubuntu by running `wsl` in the Windows Terminal

```{important}
From now on cloning and running the devcontainer should be done from the `wsl` terminal, except when otherwise specified.
```

::::
:::::

::::

::::{tab-item} Windows

On Windows we will be installing WSL with Ubuntu and Docker Desktop.

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

4. Follow onscreen instructions to setup an account in Ubuntu on WSL.

Installing Docker Desktop

1. Install docker desktop from https://www.docker.com/ 

2. Start ubuntu by running `wsl` in the Windows Terminal

```{important}
From now on cloning and running the devcontainer should be done from the `wsl` terminal, except when otherwise specified.
```

::::
:::::

## Installing Visual Studio Code

To install Visual Studio Code:

1. [Download the appropriate VS Code `.zip` file](https://code.visualstudio.com/download).

2. Navigate to your `Downloads` folder.

3. Double-click the `.zip` file.

4. Move the application to your `Applications` folder.

## Installing the necessary VS Code extensions

To install the Remote - Containers extension in VS Code:

1. Open VS Code.
2. Click on the `Extensions` icon in the left sidebar (or press `Ctrl+Shift+X` on Windows or `Cmd+Shift+X` on macOS).
3. In the search bar, type `Remote - Containers`.
4. Click on the `Install` button next to the `Remote - Containers` extension by Microsoft.
5. (**Windows only**) Follow the same instructions to install also the `WSL` extension (see next section).

## Cloning the `dt-env-developer` repository

To clone the `dt-env-developer` repository, run:

```shell
git clone git@github.com:duckietown/dt-env-developer.git
```

```{attention}
Ignore the instructions in the `README` of this repository.

(Windows) If you are on Windows, make sure to run the above command from the `wsl` terminal.
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
The first time you load the Dev Container it may take some time as it is building the environment.
```

## Setting up the Duckietown Shell

To set up the Duckietown Shell, follow [these instructions](dt-account-set-token).

```{attention}
If a popup asking you to input your credentials appears, you should do so and then click `Always Allow`. 
```

(devcontainer-running-matrix-renderer)=
## Running the Duckiematrix

The procedure for running the Duckiematrix will be slightly different in this workflow. In short, you
will run the `Engine` and `Renderer` inside and outside the Dev Container, respectively.

To start the `Engine`, run the following command in the Dev Container:

```shell
dts matrix engine run --sandbox --verbose
```

```tip
If you are using the Duckiematrix in the context of an LX, [launch the engine with dts code instead](caveat-devcontainer-lx).
```

`````{tab-set}

````{tab-item} macOS

To install the `Renderer`:

1. [Download the `Renderer` `.zip` file](https://duckietown-public-storage.s3.amazonaws.com/assets/duckiematrix/releases/duckiematrix-0.6.2-macosx.zip).

2. Navigate to your `Downloads` folder.

3. Double-click the `.zip` file.

4. Move the application to your `Applications` folder.

To start the `Renderer` and connect it to the `Engine` running in the Dev Container, run the following commands, where `TOKEN` is your Duckietown Token (do not forget the double quotes):

```shell
cd /Applications
open duckiematrix.app --args -e localhost --token "TOKEN"
```

````

````{tab-item} Windows

```{important}
These commands should be run from the Windows Terminal, not from the `wsl` terminal.
```

To install the `Renderer`:

1. [Download the `Renderer` `.zip` file](https://duckietown-public-storage.s3.amazonaws.com/assets/duckiematrix/releases/duckiematrix-0.6.2-windows.zip).

2. Navigate to your `Downloads` folder.

3. Double-click the `.zip` file.

4. Move the application to your `C:\Program Files` folder.

To start the `Renderer` and connect it to the `Engine` running in the Dev Container, run the following commands, where `TOKEN` is your Duckietown Token (do not forget the double quotes):

```shell
cd C:\Program Files
.\duckiematrix.exe -e localhost --token "TOKEN"
```

````

````{tab-item} Windows

```{important}
These commands should be run from the Windows Terminal, not from the `wsl` terminal.
```

To install the `Renderer`:

1. [Download the `Renderer` `.zip` file](https://duckietown-public-storage.s3.amazonaws.com/assets/duckiematrix/releases/duckiematrix-0.6.2-windows.zip).

2. Navigate to your `Downloads` folder.

3. Double-click the `.zip` file.

4. Move the application to your `C:\Program Files` folder.

To start the `Renderer` and connect it to the `Engine` running in the Dev Container, run the following commands, where `TOKEN` is your Duckietown Token (do not forget the double quotes):

```shell
cd C:\Program Files
.\duckiematrix.exe -e localhost --token "TOKEN"
```

````

`````

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
dts matrix attach vargo -e 192.168.139.2 map_0/vehicle_0
```

### Running `dts code editor`

To be able to run `dts code editor`, you need to install `mkcert` on your host system:
### Running `dts code editor`

To be able to run `dts code editor`, you need to install `mkcert` on your host system:

`````{tab-set}
`````{tab-set}

````{tab-item} macOS
````{tab-item} macOS


1. Run `brew install mkcert` or [download the `darwin` binary for your system's architecture](https://github.com/FiloSottile/mkcert/releases/tag/v1.4.4).

2. Run `mkcert -install` (to install the local CA in your system).
````
````

````{tab-item} Windows

1. Download mkcert for windows from [this link](https://dl.filippo.io/mkcert/v1.4.4?for=windows/amd64), saving it to your Downloads folder.

2. Then, open the Windows Terminal and run:

    ```
    .\Downloads\mkcert-v1.4.4-windows-amd64.exe --install
    ```

3. Select `Yes` in the prompt
4. In the Ubuntu terminal, open the `~/.bashrc` file with a text editor, e.g., by running `nano ~/.bashrc` and append the following lines at the end of the file:

    ```bash
    WINUSER=$(powershell.exe '$env:USERNAME' | tr -d '\r')
    export MKCERT_PATH="/mnt/c/Users/$WINUSER/AppData/Local/mkcert"
    ```

5. Save and exit the text editor (in `nano`, press `Ctrl+X`, `Enter`, then `Enter`).

6. Finally, run `source ~/.bashrc` to update the current shell or open a new `wsl` terminal window.
````
`````
````{tab-item} Windows

1. Download mkcert for windows from [this link](https://dl.filippo.io/mkcert/v1.4.4?for=windows/amd64), saving it to your Downloads folder.

2. Then, open the Windows Terminal and run:

    ```
    .\Downloads\mkcert-v1.4.4-windows-amd64.exe --install
    ```

3. Select `Yes` in the prompt
4. In the Ubuntu terminal, open the `~/.bashrc` file with a text editor, e.g., by running `nano ~/.bashrc` and append the following lines at the end of the file:

    ```bash
    WINUSER=$(powershell.exe '$env:USERNAME' | tr -d '\r')
    export MKCERT_PATH="/mnt/c/Users/$WINUSER/AppData/Local/mkcert"
    ```

5. Save and exit the text editor (in `nano`, press `Ctrl+X`, `Enter`, then `Enter`).

6. Finally, run `source ~/.bashrc` to update the current shell or open a new `wsl` terminal window.
````
`````

(caveat-devcontainer-lx)=
### Learning Experiences in the Duckiematrix

To run the Duckiematrix for `LXs`, run the following command to start the `Engine`:

```shell
dts code start_matrix --no-renderer
```

and then [attach the `Renderer`](devcontainer-running-matrix-renderer) launching it from the host machine.
