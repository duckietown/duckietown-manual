(dtmatrix-modes)=
# Duckiematrix - Modes

```{seo}
:description: The Duckiematrix's modes.
:keywords: Duckietown, Duckiematrix, modes
```

This chapter describes the Duckiematrix's modes.

```{needget}
Completed [](dtmatrix-sides).
---
Knowledge on the Duckiematrix's modes.
```

(modes-introduction)=
## Introduction

An instance of the Duckiematrix can run in two modes:

* `Realtime` mode.
* `Simulation` (`Gym`) mode.

(mode-realtime)=
## Realtime mode

`Realtime` mode is **asynchronous**, meaning that the `Matrix` and `World` side work asynchronously with respect to each other.

`Agents` can send input commands to the `Matrix` side as fast as they want and the `Matrix` side will consume them as fast as it can.
However, if the `Matrix` side does not manage to keep up with the `Agents`, some commands will be dropped and never reach it.

Similarly, sensors in the `Renderers` will (try to) produce data at the sensor's frequency, regardless of how much data the `Agents` can process. In fact, neither side will care whether there is an entity listening on the other side.

While this is the mode that most closely resembles the real behavior of a robot and `Agent`, it evolves with dynamics that are **non-deterministic**, meaning that experiments run in
`Realtime` mode are not reproducible.

The job of the `Engine`, in this case, is to run the physics engine on the commands from the `World` side whenever they are available and bridge data from the `Matrix` side over to the `World` side.

```{figure} ../../_images/duckiematrix/intermediate/mode-realtime-1.jpg
:name: fig:mode-realtime-1
:alt: A sequence diagram of a simple `Network` running in `Realtime` mode.

A sequence diagram of a simple `Network` running in `Realtime` mode.
```

(mode-gym)=
## Simulation (Gym) mode

`Simulation` (`Gym`) mode is **synchronous**, meaning that the `Matrix` and `World` side work synchronously with respect to each other.

Starting from the `Matrix` side, robots will produce their observations (sensor readings).
The `Engine` will then collect and send these observations as a whole to the `World` side.
The `Renderers` will then be paused until the `World` side has produced all of its commands.
The `Engine` will then collect these commands and run the physics engine, which will act on these commands.
An updated state of the scene is sent to the `Renderers`, which will start producing another batch of observations.

The strenuous job performed by the `Engine` in this case guarantees that all of the `Renderers` start a batch of rendering/sensing only once all the robots in the scene have received a command from the `World` side.
Overall performance in `Simulation` mode is greatly reduced compared to `Realtime` mode, due to the synchronicity of the events.

```{figure} ../../_images/duckiematrix/intermediate/mode-gym-1.jpg
:name: fig:mode-gym-1
:alt: A sequence diagram of a simple `Network` running in `Simulation` mode.

A sequence diagram of a simple `Network` running in `Simulation` mode.
```
