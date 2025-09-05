(dtmatrix-domains)=
# Engine Reachability Domains

```{seo}
:description: The Duckiematrix Engine reachability domains.
:keywords: Duckietown, Duckiematrix, Engine, reachability domains.
```

This chapter describes the Duckiematrix `Engine` reachability domains.

```{needget}
Completed [](dtmatrix-run).
---
Knowledge on the Duckiematrix `Engine` reachability domains.
```

(intermediate-engine-reachability-domains-introduction)=
## Introduction

The Duckiematrix is, by design, a distributed platform, meaning that you can scatter pieces around across an arbitrarily large geographical region, as long as they are able to talk to each other over the `Network`.
If you are not running an `Engine` locally, you need to tell the `Renderers` where to reach the `Engine` by providing an IP address or hostname.

Once the remote `Engine` is running, remote (or local) `Renderers` can join in.
Depending on where the `Renderers` are (logically) located within the `Network` with respect to the `Engine`, your setup will need to meet different requirements.

We can distinguish between three different `Engine` reachability domains:

* Local machine only.
* Local network only.
* Global network (Internet).

To run a local `Engine` using the embedded `sandbox` `Map`, run:

```shell
dts matrix engine run --sandbox
```

Once the `Engine` is ready to accept connections from `Renderers`, a list of IP addresses that the `Engine` can be reached at will be shown.

(intermediate-engine-reachability-domains-local-machine-only)=
## Local machine only

This is when the `Engine` and `Renderers` are run on the same machine, and communicate over the [loopback](https://en.wikipedia.org/wiki/Loopback) network.

(intermediate-engine-reachability-domains-local-network-only)=
## Local network only

This allows for the scattering of `Renderers` around a local network and is very useful for speeding up the simulation process, by distributing the rendering tasks among several machines.
The only requirement, in this case, is that all of the `Renderers` can reach the network in which the `Engine` resides.

(intermediate-engine-reachability-domains-global-network-internet)=
## Global network (Internet)

This requires having a machine with a public IP address, as the `Engine` needs access to a public IP address.
Also, all of the `Renderers` are required to be able to reach the Internet.

```{warning}
Exposing a Duckiematrix `Engine` to the Internet is not safe.
The Duckiematrix is not designed to account for malicious attacks.
Public `Engines` need to be properly protected against such attacks.
Use this method at your own risk.
```

(intermediate-engine-reachability-domains-behind-a-nat)=
## Behind a NAT

Note that, the `Renderers` are the ones initiating the connection with the `Engine`, not the other way around.
Therefore, it is important that the `Renderers` are able to reach the `Engine` when the connection has not been established yet, meaning that it is okay for the `Renderers` to be behind a [NAT](https://en.wikipedia.org/wiki/Network_address_translation) but not the `Engine`.
