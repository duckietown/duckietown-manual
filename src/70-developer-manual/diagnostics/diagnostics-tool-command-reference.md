```{seo}
:description: Complete reference for `dts diagnostics run`, including syntax, required arguments, and all optional flags for tailoring a Duckietown diagnostics session.
:keywords: Duckietown diagnostics, dts diagnostics run options, system monitoring, experiment logging, command reference
```

(sec:devel_sw_diagnostics_reference)=
# Diagnostics Command Reference

Use the diagnostics tool to log resource usage on a Duckietown device and push the results to the cloud for analysis.

## Syntax

```shell
dts diagnostics run \
    [-H ROBOT]                 \   # where the tool itself runs
    -G EXPERIMENT              \   # experiment name
    -d SECONDS                 \   # capture length
    [OPTIONS]
```

## Legacy options

:::{list-table} Options available to the command `dts diagnostics run`
:header-rows: 1
:name: tab:devel_sw_diagnostics_dts_diag_run_options
:widths: 15, 15, 70

- - Argument
  - Default
  - Description
- - `-H`<br/>`--machine`
  - `unix:///var/run/docker.sock`
  - Docker socket or hostname where to run the diagnostics image. This is not the monitored target.
- - `-T`<br/>`--target`
  - `unix:///var/run/docker.sock`
  - Docker endpoint to monitor.
- - `--type`
  - `auto`
  - Specify a device type (e.g., `duckiebot`, `watchtower`).
- - `--app-id`
  - Automatic
  - ID of the API App used to authenticate the upload to the server. Must have access to the `data/set` API endpoint.
- - `--app-secret`
  - Automatic
  - Secret of the API App used to authenticate the upload to the server.
- - `-D`<br/>`--database`
  - `db_log_default`
  - Name of the logging database. Must be an existing database.
- - `-G`<br/>`--group`
  - Required
  - Name of the experiment (e.g., `new_fan`).
- - `-S`<br/>`--subgroup`
  - `default`
  - Name of the test within the experiment (e.g., `fan_model_X`).
- - `-d`<br/>`--duration`
  - Required
  - Length of the analysis in seconds. Use `-1` for an indefinite duration.
- - `-F`<br/>`--filter`
  - `[]`
  - Specify regular expressions used to filter the monitored containers.
- - `--system`
  - `False`
  - Log system processes as well.
- - `-m`<br/>`--notes`
  - `(empty)`
  - Custom notes to attach to the log.
- - `--no-pull`
  - `False`
  - Do not pull the diagnostics image before running the experiment.
- - `--debug`
  - `False`
  - Run in debug mode.
- - `--vv`<br/>`--verbose`
  - `False`
  - Run in verbose mode.
- - `--no-upload`
  - `False`
  - Do not upload the statistics to the Duckietown server.
:::

<!--
(sec:devel_sw_diagnostics_reference)=
# Reference

In this section, we will describe the various arguments that the diagnostics
tool accepts. Use them to configure the diagnostics tool to fit your needs.

## Usage

You can run a diagnostics test using the command:

```bash
dts diagnostics run \
    -H/--machine [ROBOT] \
    -G/--group [EXPERIMENT] \
    -d/--duration [SECONDS] \
    [OPTIONS]
```

## Options

The following table describes the __options__ available to the diagnostics
tool.

:::{list-table} Options available to the command `dts diagnostics run`
:header-rows: 1
:name: tab:devel_sw_diagnostics_dts_diag_run_options
:widths: 15, 15, 70

- - Argument
  - Default
  - Description
- - `-H`<br/>`--machine`
  - `unix:///var/run/docker.sock`
  - Docker socket or hostname where to run the diagnostics image. This is not the monitored target.
- - `-T`<br/>`--target`
  - `unix:///var/run/docker.sock`
  - Docker endpoint to monitor.
- - `--type`
  - `auto`
  - Specify a device type (e.g., `duckiebot`, `watchtower`).
- - `--app-id`
  - Automatic
  - ID of the API App used to authenticate the upload to the server. Must have access to the `data/set` API endpoint.
- - `--app-secret`
  - Automatic
  - Secret of the API App used to authenticate the upload to the server.
- - `-D`<br/>`--database`
  - `db_log_default`
  - Name of the logging database. Must be an existing database.
- - `-G`<br/>`--group`
  - Required
  - Name of the experiment (e.g., `new_fan`).
- - `-S`<br/>`--subgroup`
  - `default`
  - Name of the test within the experiment (e.g., `fan_model_X`).
- - `-d`<br/>`--duration`
  - Required
  - Length of the analysis in seconds. Use `-1` for an indefinite duration.
- - `-F`<br/>`--filter`
  - `[]`
  - Specify regular expressions used to filter the monitored containers.
- - `--system`
  - `False`
  - Log system processes as well.
- - `-m`<br/>`--notes`
  - `(empty)`
  - Custom notes to attach to the log.
- - `--no-pull`
  - `False`
  - Do not pull the diagnostics image before running the experiment.
- - `--debug`
  - `False`
  - Run in debug mode.
- - `--vv`<br/>`--verbose`
  - `False`
  - Run in verbose mode.
- - `--no-upload`
  - `False`
  - Do not upload the statistics to the Duckietown server.
:::
-->
