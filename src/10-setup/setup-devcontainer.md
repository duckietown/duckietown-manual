```{seo}
:description: Learn how to run Duckietown code in a devcontainer
:keywords: duckietown setup, devcontainer
```

(setup-devcontainer)=
# Running Everything in a Devcontainer (Beta)

This page describes how to run Duckietown code inside a [development container](https://containers.dev/), providing a functional environment inside of [Visual Studio Code](https://code.visualstudio.com/).

```{note}
This is the only workflow for running Duckietown on an Apple Silicon (M-series) Mac computer.
```

`````{tab-set}

````{tab-item} MacOSX

1. Completely remove Docker Desktop

    If you have installed docker desktop, you will need to completely remove it. We will be installing a replacement (Orbstack). 
    To do so you can follow the instructions [here](https://docs.docker.com/desktop/uninstall/) and then it is probably a good
    idea to reboot your computer. 


2. Install Visual Studio Code

    Go to the [VSCode download page](https://code.visualstudio.com/download) and download the appropriate version. 

    **Note**: If you have an Apple computer with an M-series chip, you will need to download the `Apple silicon` version
    of VSCode

    Once the `.zip` file downloads you can double click to inflate it and then you may want to move it to your
    `Applications` folder so that you can launch it through spotlight. 

    **Tip**: If Mac refuses to open the application because it is not trusted, you can hold `option` and two finger click
    with the mouse and choose `Open`. Mac will tell you that this is not trusted but allow you to open the program 
    anyways. 

3. Install Orbstack

    Go to [Orbstack download page](https://orbstack.dev/download) and download the appropriate version (be sure to choose
    `Apple Silicon` if you have an M-Series chip.

    Once the `.dmg` file has downloaded you can click on it in your `Downloads` and drag it to your Applications folder. 
    Then you can open it with spotlight or any other means. 


4. Clone the Dev Container repository

    Clone the development repository 

    ```bash
    git clone git@github.com:duckietown/dt-env-developer.git
    ```
    you **do not** need to pay any attention to the instructions in the README of this repository. 


5. Run the Dev Container in VSCode  

    Open Visual Studio Code.

    Click File -> Open Folder and navigate to the `dt-env-developer` folder that you clone previously and select it. 

    You should see a Window pop up in the bottom right asking if you would like open this folder in a `devcontainer`. 
    You should click on the button that you would like to do so. 

    The first time you load the devcontainer it can take some time so be patient. You can always look at the logs
    to make sure that things are still happening. 


6. Test the Shell

    In a terminal, run 

    ```bash
    dts commands
    ```

    This may take some time to download the commands, and it may ask you for your Duckietown token. You can find your 
    token on [the profile page of the Duckietown Hub](https://hub.duckietown.com/profile/) (you may have to sign in). 

    Once the shell is configured, you should have a fully functional development environment.

    **Note**: You may get a popup asking you to input your credentials. You should do so and then click `Always Allow`. 

7. Running the Duckiematrix

    The procedure for running the Duckiematrix will be slightly different in this devcontainer workflow. In short, we
    will run the `ENGINE` inside the devcontainer, but we will run the `RENDERER` (i.e. the GUI interface) natively on your Mac.

    To start the engine, inside a terminal in the VSCode devcontainer run:

    ```bash
    dts matrix engine run --sandbox
    ```

    To install the renderer on macOS you can download the `.app` file from [this link](https://duckietown-public-storage.s3.amazonaws.com/assets/duckiematrix/latest-macosx). After downloading it, you can rename it to `duckiematrix.app` and move it to your `Applications` folder.


    Then you can start the Duckiematrix renderer with:

        duckiematrix.app --args -e localhost --token "YOUR_DT2_TOKEN"

    This will connect to the Duckiematrix engine running on localhost. Make sure to replace `YOUR_DT2_TOKEN` with your actual Duckietown token and keep the double quotes.

# Devcontainer Caveats

There are small caveats and special instructions for using the development container.

## Duckietown Viewer/Keyboard Controller etc.

The viewer and keyboard controller may not work as expected due to limitations with GUI applications in Docker containers. As a workaround, you can use the `--browser` option to open the viewer in your web browser:

    dts duckiebot image_viewer devbot --browser

## Accessing Virtual Robot Dashboard

To access the Virtual Robot you can use the noVNC virtual desktop available at [localhost:6080](http://localhost:6080). You can open the web browser and connect to the dashboard.

## Attaching a virtual duckiebot to the Duckiematrix

When you attach a virtual robot to the Duckiematrix you need to use one of the LAN IP addresses of the engine, not `localhost`:

    dts duckiebot matrix attach ![ROBOT_NAME] -e ![ENGINE_LOCAL_NETWORK_ADDRESS]

## dts code run

1. Install `mkcert` on your mac, either through `brew install mkcert` or by downloading the `darwin` binary for your system's architecture from [the mkcert releases page](https://github.com/FiloSottile/mkcert/releases/tag/v1.4.4).
1. Run `mkcert -install` to install the local CA in your system. (It will ask for your sudo password.)
````

````{tab-item} Linux
Coming Soon
````

`````
