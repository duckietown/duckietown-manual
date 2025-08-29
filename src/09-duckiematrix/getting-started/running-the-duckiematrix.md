(dtmatrix-run)=
# Running the Duckiematrix

```{seo}
:description: How to run the Duckiematrix.
:keywords: Duckietown, Duckiematrix, run
```

This chapter describes how to run the Duckiematrix.

```{needget}
* Knowledge of the Duckiematrix sides: [](dtmatrix-sides)
* Completed [](setup-dts)
---
- Knowledge on how to run the Duckiematrix.
```

(introduction-running-the-duckiematrix-using-a-local-engine)=
## Using a local Engine

To run a local `Engine` and `Renderer` using the embedded `sandbox` `Map` with the tutorial enabled, run:

```shell
dts matrix run --standalone --embedded --map sandbox --tutorial
```

```{note}
Use the `--verbose` option to print more information to your terminal, including a list of IP addresses that the `Engine` can be reached at.
```

(introduction-running-the-duckiematrix-using-a-remote-engine)=
## Using a remote Engine

To run a local `Renderer` and connect it to a remote `Engine`, run the following command, where `ENGINE_HOSTNAME` is the hostname (or IP address) of the remote `Engine`:

```shell
dts matrix run --engine ENGINE_HOSTNAME
```