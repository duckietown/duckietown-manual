(dtmatrix-links)=
# Links

```{seo}
:description: Duckiematrix Links.
:keywords: Duckietown, Duckiematrix, Links
```

This chapter describes Duckiematrix Links.

```{needget}
- Completed [](the-duckiematrix-first-steps)
---
- Knowledge on Duckiematrix Links
```

(intermediate-links-introduction)=
## Introduction

In previous chapters, we saw how to run an instance of the Duckiematrix.
However, you may have noticed that the robots were not doing much more than sitting and waiting.
This is because we did not tell the `Engine` where to get robot commands from.
We can tell the `Engine` to setup a communication channel with one of those robots and return to us *the other end of the line*, using `Links`, or more properly `World` `Links`.

(intermediate-links-what-is-a-link)=
## What is a Link?

A `Link` is a bidirectional communication channel between a `Matrix` and `World` entity.

```{figure} ../../_images/duckiematrix/intermediate/links-1.jpg
:name: fig:links-1
:alt: An example of `Links` between two `Matrix` and `World` entities.

An example of `Links` between two `Matrix` and `World` entities.
```

(intermediate-links-how-to-link-a-matrix-and-world-entity)=
## How to Link a Matrix and World entity

To `Link` a `Matrix` and `World` entity, run the following command, where `MATRIX` is the `Matrix` key (e.g., `map_0/vehicle_0`) and `WORLD` is the `World` side proxy name (e.g., `duckiebot`):

```shell
dts matrix run --standalone --embedded --map sandbox --link MATRIX WORLD
```
