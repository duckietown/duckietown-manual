(dtmatrix-map-customization)=
# Duckiematrix - Customizing Maps

```{seo}
:description: How to create and use a custom Duckiematrix Map.
:keywords: Duckietown, Duckiematrix, custom, Map
```

This section describes how to create and use a custom Duckiematrix `Map`.

```{needget}
- A functional Duckiematrix: [](the-duckiematrix-first-steps)
---
Knowledge on how to create and use a custom Duckiematrix `Map`.
```

(intermediate-maps-custom-maps-create-a-custom-map)=
## Create a custom Map

To create a custom `Map`:

1. Download the `loop` `Map` zip file [here](https://duckietown-public-storage.s3.amazonaws.com/assets/duckiematrix/maps/loop.zip).
2. Unzip the `loop` `Map` zip file.
3. Move the `loop` `Map` to a convenient location, noting its path.
4. Edit the name and layers of the `loop` `Map`.

```{note}
Remember that a `Map` is defined as a directory containing the layers (YAML files) that form that `Map`.
```

(intermediate-maps-custom-maps-use-a-custom-map)=
## Use a custom Map

To run a local `Engine` and `Renderer` using a custom `Map`, run the following command, where `MAP` is the path to the custom `Map`:

```shell
dts matrix run --standalone --map MAP
```

```{note}
For any changes in the layers to appear in the `Renderer`, this command will need to be re-run.
```
