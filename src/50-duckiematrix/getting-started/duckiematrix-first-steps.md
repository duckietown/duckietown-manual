```{seo}
:description: Instructions on how to install and run the Duckiematrix simulation environment for Duckietown.
:keywords: duckiematrix, installation, duckiematrix first steps, how to install the duckiematrix, how to run the duckiematrix, how to start the duckiematrix
```

```{needget}
- A working Duckietown Shell installation: [](setup-dts)
---
- A successful Duckiematrix installation
- Knowledge on how to start the Duckiematrix
- Knowledge of Duckiematrix optional features
```

(the-duckiematrix-first-steps)=
# Duckiematrix installation

The Duckiematrix automatically installs the first time it is run, so no explicit installation action is required. 

:::::{tab-set}

::::{tab-item} Ubuntu

To get started immediately, open a terminal, and run:

```shell
dts matrix run --standalone --embedded --map sandbox
```

::::

::::{tab-item} Duckietown Workspace

There are two ways to use the Duckiematrix from Workspaces:

1. (better performance) If `dts` is installed on the host machine: 
    
    Inside the Workspace, start the engine with:
    
    ```shell
    dts matrix engine run --sandbox --verbose
    ```

    On the host machine instead, start the renderer with:
    
    ```shell
    dts matrix run
    ```

    and it will automatically connect to the engine running inside the workspace.

    ```{note}
    To run the Linux version of the Duckiematrix on Windows, add `--os-family linux` to the above command.
    ```

2. (broader compatibility) If `dts` is **not** installed on the host machine, inside the Workspace, run:

    ```shell
    dts matrix run --standalone --sandbox --verbose --browser
    ```

    the renderer will be run through the browser (WebGL).

    ```{note}
    For the WebGL version of the Duckiematrix, if the colors look desaturated, try a different browser.
    ```

<!--
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
-->

::::
:::::

```{note}
After the Duckiematrix renderer window opens, click on it and press <keyb>Enter</keyb> to enable keyboard interaction. Press <keyb>Esc</keyb> to release the mouse to desktop again.  
```

(duckiematrix-how-to-start)=
## How to run the Duckiematrix

As seen above, the command to (install and) run the Duckiematrix is `dts matrix run`. 

However, two additional pieces of information are required:

1. Where is the engine running. Options are:
    * locally (choice for most use cases): add the `--standalone` flag to the `matrix run` command;
    * remotely: read [](introduction-running-the-duckiematrix-using-a-remote-engine).

2. Which map to load. Options are:
    * use a default map: [](introduction-duckiematrix-maps)
    * create your own map: [](introduction-duckiematrix-custom-maps)


(duckiematrix-optional-flags)=
## Common optional `run` flags 

* `--help`: get a comprehensive list of optional flags with explanations of use.

* `--map`: followed by the path of a [customized map](introduction-duckiematrix-custom-maps).

* `--embedded`: in conjuntion with `--map` when using one of the [default maps](introduction-duckiematrix-maps). For example, you can run the `demo` map in an engine with:

    dts matrix engine run --embdedded --map demo

* `--no-tutorial`: by default, the Duckiematrix runs in *tutorial* mode, where the key bindings are introduced at startup. Use this flag to disable this introduction. Note that relevant keyboard bindings can always be found though the "Settings" tab in the renderer (bottom left of the screen).

* `--verbose`: provide a more detailed terminal output, useful for debugging in case of need.  

* `--browser`: to run the browser (WebGL) version of the Duckiematrix, especially useful when using [Duckietown Workspaces](setup-devcontainer) on macOS or Windows OSs.

```{note}
For the WebGL (browser) version of the Duckiematrix, if the colors look desaturated, try a different browser.
```

(introduction-running-the-duckiematrix-using-a-remote-engine)=
## Using a remote engine

To run a **local renderer** and connect it to a **remote engine**, specify the location of the engine (as a hostname or IP address) using the `--engine` flag:

```shell
dts matrix run --engine ENGINE_HOSTNAME
```

```{note}
If you are using a [Duckietown Workspace](setup-devcontainer) and the engine is running inside the dev container, run this renderer command from a terminal on your host machine.
```

In this case you do not need to specify a `map` since that was already specified when the Duckiematrix engine
was initially run.

(introduction-duckiematrix-connect-db-to-remote-engine)=
### Connecting a Duckiebot to a remote engine

Once a Duckiematrix engine is running, you can "attach" a Duckietown robot, physical or [virtual](dtmatrix-virtual-duckiebots), to an entity in the simulated world:

```shell
dts matrix attach [--engine ENGINE_HOSTNAME] DUCKIEBOT_NAME ENTITY_NAME [--dreamwalk]
```

where:

* `ENGINE_HOSTNAME` is not necessary if the engine is running locally.
* `DUCKIEBOT_NAME` is the hostname of your virtual or physical robot
* `ENTITY_NAME` is the name of the entity in the Duckiematrix world you are attaching `DUCKIEBOT_NAME` to. A list of available entities for the engine running can be found in the map configurations or more simply by clicking on the `Robots` tab at the bottom of a Duckiematrix rendering window, and then looking at the `Name`. 


```{figure} ../../_images/duckiematrix/introduction/01-Duckiematrix-entities.jpg
:name: fig:duckiematrix-splashscreen-1
:alt: Duckiematrix sandbox map splashscreen with highlighted Robots sections
:width: 70%

Find the available entity names by clicking on the "Robots" section
```

```{figure} ../../_images/duckiematrix/introduction/02-Duckiematrix-entities.jpg
:name: fig:duckiematrix-entity-name-example
:alt: where to find entity names in the Duckiematrix
:width: 70%

The default entity name for a Duckiebot is `map_0/vehicle_0`. 
```

<!--
#### Example uses of `dts matrix run` 

* Attaching a virtual robot to a local engine

* Attaching a physical robot to a local engine

* Attaching a virtual robot to a remote engine

* Attaching a physical robot to a remote engine


```{todo}
add actual command to attach a virtual duckiebot, and a physical one using the `--dreamwalk` flag
```
-->

(introduction-duckiematrix-maps)=
## Duckiematrix maps

With respect to the map, you can choose to either define your own map and tell the Duckiematrix where to find it
on the file system, or you can choose to use one of the default maps that are provided by including the `--embedded` flag.

The default maps are named:

 - `sandbox` : 5x5 tiles map with 4x 3-way intersections, traffic lights, demo traffic signs, watchtowers, one DB21 Duckiebot and garage for calibrations.

```{figure} ../../_images/duckiematrix/introduction/duckiematrix-map-sandbox.jpg
:name: dm-map-sandbox
:alt: Bird eye overview of Duckiematrix "sandbox" map
:width: 70%

The default `sandbox` map.
```

 - `demo`: same map layout and content as `sandbox` map, but including multiple Duckiebots (DB21, DB19), night-day cycle, and ornamental moving duckies.

```{figure} ../../_images/duckiematrix/introduction/duckiematrix-map-demo.jpg
:name: dm-map-demo
:alt: Bird eye overview of Duckiematrix "demo" map
:width: 70%

The default `demo` map includes multiple Duckiebots and night-day cycle.
```

 - `empty`: empty map (only grass)

```{figure} ../../_images/duckiematrix/introduction/duckiematrix-map-empty.jpg
:name: dm-map-empty
:alt: Bird eye overview of Duckiematrix "semptyandbox" map
:width: 70%

The default `empty` map.
```

 - `intersections`: same map layout as `sandbox`, but with one intersection having traffic signs arranged according to the appearance specifications. Good map for testing intersection navigation agents.

```{figure} ../../_images/duckiematrix/introduction/duckiematrix-map-intersections-1.jpg
:name: dm-map-intersections-bird-eye
:alt: Bird eye overview of Duckiematrix "intersection" map
:width: 70%

The default `intersections` map.
```
```{figure} ../../_images/duckiematrix/introduction/duckiematrix-map-intersections.jpg
:name: dm-map-intersections-pov
:alt: Duckiebot point of view in Duckiematrix "intersection" map
:width: 70%

The default `intersections` map from a Duckiebot's point of view.
```

 - `loop`: 3x3 tiles minimal road loop; the smallest legal Duckietown. One DB21 Duckiebot on the track. 


```{figure} ../../_images/duckiematrix/introduction/duckiematrix-map-loop.jpg
:name: dm-map-intersections-bird-eye
:alt: Bird eye overview of Duckiematrix "loop" map
:width: 70%

The default `loop` map: the minimal Duckietown.
```
<!-- it would be good to provide more details about these maps here -->


In summary, the following command:

```shell
dts matrix run --standalone --embedded --map sandbox
```

will:

1. download and install the latest version of the Duckiematrix if it has not already been installed, 
2. start it on your local machine and load the `sandbox` map.

```{note}
{{ dt_workspace_matrix_standalone_note.format(dt_workspace_note_prefix) }}
```

(introduction-duckiematrix-custom-maps)=
### Using a Custom Map

The [Duckiematrix map](dtmatrix-maps) loaded in the engine can be locally defined. To learn how to create a compliant map read: [creating Duckiematrix compliant maps](dtmatrix-map-customization). This map can then be loaded by omitting the `--embedded` flag and specifying the path, i.e.:

```shell
dts matrix run --standalone --map PATH_TO_MAP
```

```{note}
{{ dt_workspace_matrix_standalone_note.format(dt_workspace_note_prefix) }}
```
