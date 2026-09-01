(setup-db-sd-card-flashing-intro)=
# Duckietown Robots SD Card Initialization

```{seo}
:description: Instructions on how to flash an SD card to initialize a Duckiebot, Duckiedrone, Traffic Light or Watchtower.
:keywords: Duckietown, Duckiebot, Duckiedrone, flashing, initialization, SD card, Traffic Light, Watchtower, dts sd card init, dts sd_card init
```

```{needget}
* An SD card with at least `64 GB` of space
* An SD card adapter appropriate for the computer you are using to flash the SD card
* A broadband internet connection
* 20 - 40 mins, depending on internet connection speed and procedure (easy/complete)
* At least 40 GB of free space on your hard drive before starting
* [Functional DTS installation](setup-dts) if using the [Complete - Initialization](setup-db-sd-card-flashing-complete) procedure.
---
An initialized SD card for your Duckiebot with customized settings.
```

While the hardware represents the body of the robot, the software running on it is its mind. In this chapter we set up the mind of the Duckiebot.

In other words, we initialize an SD card for Duckietown robots (e.g., Duckiebots, Duckiedrones, Traffic Lights), by flashing a Duckietown image on an SD card, the hard drive of the robot.

```{attention}
**Updating from daffy to ente**: If you have a Duckiebot running the `daffy` version and want to update to `ente`, you must reflash a new SD card using the procedures below. The `dts duckiebot update` command does not currently support switching between `daffy` and `ente` versions. For information about updating within the same version, see [](ops-db-update).
```

We provide two approaches to create a new SD card for a Duckietown robot:

1. ["The Fast Way"](setup-db-sd-card-flashing-fast): requires less time, can be performed with any operating system, does not need to have the Duckietown Shell installed, but allows for no customization of the robot name. Recommended for testing of a single robot.

2. ["The Complete Way"](setup-db-sd-card-flashing-complete): requires a functional [Duckietown Shell installation](setup-dts), takes roughly twice the time of the faster approach, but allows for full customization. Recommended when operating more than one Duckiebot.

After creating an SD card, you can change selected settings, such as the hostname, Wi-Fi configuration, or `duckie` account password, without reflashing it by following the `dts sd_card update` command instructions: [](update-initialized-sd-card).