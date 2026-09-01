(sd-card-update)=
# Updating an existing SD card

```{seo}
:description: Instructions on how to update an SD card previously flashed to initialize a Duckiebot, Duckiedrone, Traffic Light or Watchtower.
:keywords: Duckietown, Duckiebot, Duckiedrone, flashing, update, SD card, Traffic Light, Watchtower, dts sd_card update
```

```{needget}
* [Functional DTS installation](setup-dts)
* A previously flashed Duckietown SD card
* An SD card adapter appropriate for the computer you are using to flash the SD card
* A broadband internet connection
* 20 - 40 mins, depending on internet connection speed
---
An updated SD card for your Duckietown robot.
```

(update-initialized-sd-card)=
## Updating an initialized SD card

To update an initialized SD card, run the following command, where `TYPE` and `CONFIGURATION` are the values used to initialize the SD card, `HOSTNAME` is the new robot name, `WIFI` is the new comma-separated list of Wi-Fi networks, and `COUNTRY` is the new two-letter Wi-Fi country code:

```shell
dts sd_card update --type TYPE --configuration CONFIGURATION [--hostname HOSTNAME] [--wifi WIFI] [--country COUNTRY]
```

At least one of `--hostname`, `--wifi`, or `--country` is required; only the supplied settings are changed. Some disk images store Wi-Fi and country settings together, in which case you must provide both `--wifi` and `--country` in the same command.

```{attention}
Updating the `WIFI` configuration will replace existing data. 
```

If you omit `--device DEVICE`, DTS prompts you to select the physical SD-card device. Specify it to select the device directly.

To see all available options, run:

```shell
dts sd_card update --help
```

