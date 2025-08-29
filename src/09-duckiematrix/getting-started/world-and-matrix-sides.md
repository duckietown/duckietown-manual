(dtmatrix-sides)=
# Duckiematrix - The World and Matrix Sides

```{seo}
:description: The Duckiematrix's sides.
:keywords: Duckietown, Duckiematrix, sides
```

This chapter describes the Duckiematrix's sides.

```{needget}
- Completed [](dtmatrix-architecture)
---
- Knowledge on the Duckiematrix's sides
```

(introduction-sides-introduction)=
## Introduction

An instance of the Duckiematrix has two sides:

* The `Matrix` side.
* The `World` side.

(introduction-sides-the-matrix-side)=
## The Matrix side

The `Matrix` side contains all of the `Renderers`.

```{note}
When something is said to happen on the `Matrix` side, it means that it is something that is computed, or an event that occurs, in one or more `Renderers`.
```

(introduction-sides-the-world-side)=
## The World side

The `World` side is where we (human) users and robots reside.
Any `World` entity (e.g., user, algorithm, robot, etc.) that interacts with the `Engine` from the `World` side is known as an `Agent`.

```{note}
We are not making a distinction between physical and virtual robots here.
Robots, intended as computing entities, whether  physical or virtual, always reside on the `World` side. Their sensors and actuators though, reside on the `Matrix` side.
```

(introduction-sides-the-engine-has-no-side)=
## The Engine has no side

Sitting between the `World` and `Matrix` sides, the `Engine` does not belong to either.
In a `Network`, the `Engine` is responsible for, among other things, bridging data between the two sides, ensuring that each side gets what it needs from the other.

```{figure} ../../_images/duckiematrix/introduction/block-architecture-2.jpg
:name: fig:block-architecture-2
:alt: A block diagram of a simple `Network`.

A block diagram of a simple `Network`.
```
