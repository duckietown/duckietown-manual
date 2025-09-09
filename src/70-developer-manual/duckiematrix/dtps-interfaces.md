(dtmatrix-dtps-interfaces)=
# DTPS interfaces

```{seo}
:description: How to view DTPS (Duckietown Postal Service) topics coming from the Duckiematrix.
:keywords: Duckietown, Duckiematrix, DTPS, Duckietown Postal Service, topics
```

This chapter describes how to view `DTPS` (`Duckietown Postal Service`) topics coming from the Duckiematrix.

```{needget}
* Completed [](the-duckiematrix-first-steps).
* Completed [](sw-tools-dtps).
---
Knowledge on how to view `DTPS` topics coming from the Duckiematrix.
```

(introduction-dtps-html-interface)=
## HTML interface

```{figure} ../../_images/duckiematrix/introduction/dtps_html_interface.png
:name: dtps-html-interface
:alt: The `DTPS` HTML interface for the embedded `sandbox` `Map`.

The `DTPS` HTML interface for the embedded `sandbox` `Map`.
```

To open the `DTPS` HTML interface for the Duckiematrix, run the following command, where `ENGINE_HOSTNAME` is the optional hostname (or IP address) of the `Engine` and `TOPIC` is an optional topic (e.g., `robot/map_0/vehicle_0/sensor/camera/front_center/jpeg`):

```shell
dts matrix dtps [--engine ENGINE_HOSTNAME] [--topic TOPIC]
```
