(dtmatrix-maps)=
# Maps

```{seo}
:description: Duckiematrix Maps.
:keywords: Duckietown, Duckiematrix, Maps
```

This chapter describes Duckiematrix `Maps`.

```{needget}
Completed [](the-duckiematrix-first-steps).
---
Knowledge on Duckiematrix `Maps`.
```

(intermediate-maps-introduction)=
## Introduction

A `Map` is defined using a set of YAML files known as `Layers`.

(intermediate-maps-keys)=
## Keys

A `Key` has two functions:

1. It serves as a unique identifier for an object.
2. It encodes the hierarchical structure of a `Layer`.

(intermediate-maps-frames-layer)=
## The frames Layer

A `Frame` object has the following pseudo-schema, where the `relative_to` field will be discussed later in this section and the `pose` and `twist` (optional) fields describe the 3D pose and twist of the object, respectively:

```yaml
relative_to: str | ~
pose:
  x: float
  y: float
  z: float
  roll: float
  pitch: float
  yaw: float
twist:
  v_x: float
  v_y: float
  v_z: float
  w_x: float
  w_y: float
  w_z: float
```

A pseudo-schema of the `frames` `Layer` is as follows, where the `frames` object is a mapping between object `Keys` and their `Frame`:

```yaml
version: str
frames: dict[str, Frame]
```

The `frames` `Layer` is defined using a `frames.yaml` file, whose contents are similar to the following, where the `map_0` object is positioned at the origin and the `map_0/street_light_0` object is positioned `0.6 m` along the `x` and `y` axes, and `0 m` along the `z` axis, with a rotation of `3.1415 rad` about the `z` axis:

```yaml
version: 1.0
frames:
  map_0:
    relative_to: ~
    pose:
      x: 0.0
      y: 0.0
      z: 0.0
      roll: 0.0
      pitch: 0.0
      yaw: 0.0
  map_0/street_light_0:
    relative_to: ~
    pose:
      x: 0.6
      y: 0.6
      z: 0.0
      roll: 0.0
      pitch: 0.0
      yaw: 3.1415
```

In the example above, the `map_0/street_light_0` `Key` indicates that the `street_light_0` object is a child of the `map_0` object.
Therefore, if `map_0` moves, `street_light_0` will rigidly move with it.

```{note}
The existence of an object's ancestors is not enforced.
Therefore, a `Layer` in which an object with `Key` `a/b/c` is defined but neither `a` nor `a/b` are, is still a valid `Layer`.
In the case of the `frames` `Layer`, objects `a` and `a/b` would be created (such that `b` is a child of `a`) and their states would be set to coincide with the origin's state.
```

```{note}
While certain `Keys` suggest the types of objects they refer to (e.g., `map_0/street_light_0` likely refers to a street light), no assumptions can be made about the nature of the objects simply by looking at their `Keys`.
```

(intermediate-maps-frames-layer-relative-to-field)=
### The relative_to field

While the path-like structure of `Keys` encodes the hierarchical structure of a `Layer`, we may want to, for example, define the frame of an object with respect to another while keeping them on different branches of the hierarchy.
In this case, the `relative_to` field can be used.

For example, in the following `frames` `Layer`, we want to position the `map_0/vehicle_0` object `1 m` from the `map_0/street_light_0` object along the `x` axis:

```yaml
version: 1.0
frames:
  map_0:
    relative_to: ~
    pose:
      x: 0.0
      y: 0.0
      z: 0.0
      roll: 0.0
      pitch: 0.0
      yaw: 0.0
  map_0/street_light_0:
    relative_to: ~
    pose:
      x: 0.6
      y: 0.6
      z: 0.0
      roll: 0.0
      pitch: 0.0
      yaw: 3.1415
  map_0/vehicle_0:
    relative_to: map_0/street_light_0
    pose:
      x: 1.0
      y: 0.0
      z: 0.0
      roll: 0.0
      pitch: 0.0
      yaw: 0.0
```

```{note}
While we could have achieved the same result without the `relative_to` field, by using the pose of the `map_0/street_light_0` object with respect to the `map_0` object, this would have required a-priori compute and a loss of information, as well as a loss of readability and editability of the scenario.
```
