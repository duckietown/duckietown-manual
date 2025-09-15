(the-duckiematrix-first-steps)=
# Installing and Running the Duckiematrix

```{seo}
:description: Instructions on how to install and run the Duckiematrix simulation environment for Duckietown.
:keywords: duckiematrix, installation, duckiematrix first steps, how to install the duckiematrix, how to run the duckiematrix, how to start the duckiematrix
```

```{needget}
- A working Duckietown Shell installation: [](setup-dts)
-
---
- A successful Duckiematrix installation
- Knowledge on how to start the Duckiematrix
```


(duckiematrix-installation)=
## How to install the Duckiematrix

The Duckiematrix is installed with the [Duckietown Shell](setup-dts) with the command:

```shell
dts matrix install
```

(duckiematrix-how-to-start)=
## How to Run the Duckiematrix

The basic command to run the Duckiematrix is `dts matrix run`. However, in order to run the
Duckiematrix you need to provide two pieces of information:

1. Where the engine is running
2. What map to load

In *most* cases, you will probably want to run the engine locally. You can do so by adding the `--standalone` flag.
With respect to the map, you can choose to either define your own map and tell the Duckiematrix where to find it
on the file system, or you can choose to use one of the default maps that are provided by including the `--embedded` flag.
The default maps are named:

 - `sandbox`
 - `demo`
 - `empty`
 - `intersections`
 - `loop`

<!-- it would be good to provide more details about these maps here -->

In summary, the following command

```shell
dts matrix run --standalone --embedded --map sandbox
```
would start the Duckiematrix on your local machine and load the `sandbox` map that is predefined.
By default, the Duckiematrix runs in *tutorial* mode, where the key bindings are introduced. If you
want to disable this behavior your can add the `--no-tutorial` flag. If something is going wrong and
you do not see the renderer initializing, you can see what is going wrong by adding the `--verbose` flag.


(introduction-running-the-duckiematrix-using-a-remote-engine)=
## Using a Remote Engine

To run a local **renderer** and connect it to a remote **engine**, you simply need to specify the location
of the engine (as a hostname or IP address) using the `--engine` flag:

```shell
dts matrix run --engine ENGINE_HOSTNAME
```

In this case you do not need to specify a `map` since that was already specified when the Duckiematrix engine
was initially run.

## Using a Custom Map

The [map](dtmatrix-maps) can be defined on the local file system and loaded by the engine. To learn how to define
a local map see the page on [creating maps](dtmatrix-map-customization). This map can then be loaded by omitting the
`--embedded` flag and specifying the path:

```shell
dts matrix run --standalone --map PATH_TO_MAP
```