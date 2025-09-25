(dtmatrix-architecture)=
# Architecture

```{seo}
:description: The Duckiematrix's architecture.
:keywords: Duckietown, Duckiematrix, architecture
```

This chapter describes the Duckiematrix's architecture.

```{needget}
- Nothing
---
- Knowledge on the Duckiematrix's architecture
```

(dtmatrix-introduction-architecture-introduction)=
## Introduction

An instance of the Duckiematrix requires:

* An `Engine`.
* A `Renderer`.

(dtmatrix-introduction-architecture-the-engine)=
## The Engine

The `Engine` is responsible for reading a `Map`, scripts and assets from disk, and sending them all together, in a single compressed package known as the `Context`, to the `Renderers` connected to that `Engine`. The `Context` is composed of the components a `Renderer` requires to initialize a `Map`.

```{note}
It is enough for the `Renderers` to place the correct objects in their initial states.
```

(dtmatrix-introduction-architecture-the-renderer)=
## The Renderer

The `Renderer` is responsible for rendering the content of the `Context` and simulating Duckietown robot sensors.

```{note}
While the `Engine` only requires a terminal, the `Renderer` has a GUI (Graphical User Interface) component, which requires a screen.
However, this is not a strict limitation, as it is possible to run a `Renderer` using off-screen rendering, where a memory buffer serves as a virtual screen.
```

(dtmatrix-introduction-architecture-networks)=
## Networks

A `Network` is defined as an `Engine` and set of `Renderers` connected to that `Engine`.

```{figure} ../../_images/duckiematrix/introduction/block-architecture-1.jpg
:name: block-architecture-1
:alt: A block diagram of a simple `Network`.

A block diagram of a simple `Network`.
```

```{note}
While you can only have a single `Engine` per instance of the Duckiematrix, you can have multiple `Renderers` connected to the same `Engine`.
```

(dtmatrix-introduction-architecture-how-it-works)=
## How it works

`Renderers` are essentially static video games, in which a virtual environment is shown but nothing happens, until the `Engine` unfreezes everything for a short period of time, known as a time step.
The `Engine` is responsible for processing time steps as fast as possible, where for each time step, the `Engine` computes the physics of the objects in the scene, regulates when sensors should fire and lights should turn on/off, etc.
Changes from one time step to the next are represented as `diffs` (differences) in the content of the `Map` `Layers` that describe the scene. At every time step, `diffs` are sent to the `Renderers`, which in turn apply them to their scenes.
