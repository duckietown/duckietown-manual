# Virtual Duckiedrone Takeoff Demo

```{seo}
:description: The Takeoff demo (demonstration) for a virtual Duckiedrone.
:keywords: Duckietown, virtual, Duckiedrone, Takeoff, demo, demonstration, ROS2, mavros, PX4
```

This chapter describes the `Takeoff` demo (demonstration) for virtual Duckiedrones.

```{needget}
[A working Duckietown Shell installation](setup-dts)
---
A virtual Duckiedrone successfully arming and taking off autonomously.
```

## Introduction to virtual Duckiedrone takeoff

```{vimeo} 1146828852
```

## Setup

To set up the demo:

1. Create a virtual Duckiedrone by running the following command, where `ROBOT_NAME` is the name of your virtual Duckiedrone:

    ```shell
    dts duckiebot virtual create -t duckiedrone -c DD24 ROBOT_NAME
    ```

2. Once created, start your virtual Duckiedrone by running the following command, where `ROBOT_NAME` is the name of your virtual Duckiedrone:

    ```shell
    dts duckiebot virtual start ROBOT_NAME
    ```

3. Run the Duckiematrix using the `sandbox_drone` map by running:

    ```shell
    dts matrix run --standalone --embedded --map sandbox_drone
    ```

4. Start the matrix with the `sandbox_drone` map:

    ```shell
    dts matrix run --standalone -d --map sandbox_drone
    ```

    ```{note}
    {{ dt_workspace_matrix_standalone_note.format(dt_workspace_note_prefix) }}
    ```

5. Attach the Duckiedrone to the matrix engine:

    ```shell
    dts matrix attach ROBOT_NAME map_0/vehicle_0
    ```

```{attention}
Wait for all containers to be running before proceeding to the next step.
```

## Start

To run the demo on your virtual Duckiedrone, run the following command, where `ROBOT_NAME` is the name of your virtual Duckiedrone:

```shell
docker exec -it dts-virtual-ROBOT_NAME docker exec -it ros2-mavros bash
```

Inside the bash prompt:

1. Set your virtual Duckiedrone to takeoff mode by running:

    ```bash
    ros2 service call /mavros/set_mode mavros_msgs/srv/SetMode "{base_mode: 0, custom_mode: 'AUTO.TAKEOFF'}"
    ```

    ````{note}
    Expected output:

    ```bash
    response:
    mavros_msgs.srv.SetMode_Response(mode_sent=True)
    ```
    ````

2. Arm your virtual Duckiedrone to initiate takeoff by running:

    ```bash
    ros2 service call /mavros/cmd/arming mavros_msgs/srv/CommandBool "{value: true}"
    ```

    ````{note}
    Expected output:

    ```bash
    requester: making request: mavros_msgs.srv.CommandBool_Request(value=True)
    response:
    mavros_msgs.srv.CommandBool_Response(success=True, result=0)
    ```
    ````

Your virtual Duckiedrone should now arm and begin its takeoff sequence to a default height of `2.5 m`.

## Stop

To stop the demo:

1. Land your virtual Duckiedrone by setting it to `AUTO.LAND` mode by running:

    ```bash
    ros2 service call /mavros/set_mode mavros_msgs/srv/SetMode "{base_mode: 0, custom_mode: 'AUTO.LAND'}"
    ```

2. Select the terminal from which the demo was run.

3. Press <kbd>Ctrl</kbd>+<kbd>D</kbd>.

## How it works

The `Takeoff` demo consists of the following steps:

1. **MAVROS interface** establishes communication between ROS2 and the PX4 flight controller via the MAVLink protocol.

2. **Mode setting** configures the flight controller to `AUTO.TAKEOFF` mode, which prepares your virtual Duckiedrone for autonomous takeoff.

3. **Arming** enables the motors, allowing your virtual Duckiedrone to generate thrust.

4. **Takeoff execution** uses the flight controller's autopilot to execute a controlled vertical ascent to a predefined altitude.

The MAVROS node acts as a bridge, translating ROS2 service calls and topic publications into MAVLink messages that the flight controller understands, and vice versa.

## Debugging and parameter tuning

If the performance of your virtual Duckiedrone is inconsistent or the takeoff does not execute properly, consider the following debugging steps.

### Verifying MAVROS connection

Check that MAVROS is properly connected to the flight controller by running:

```bash
ros2 topic echo /mavros/state
```

You should see output indicating that the flight controller is connected and that the mode is being reported.

### Checking sensor data

Verify that sensor data is being published by running:

```bash
ros2 topic list
```

Look for topics such as `/mavros/imu/data`, `/mavros/battery` and `/mavros/altitude`, and echo them to verify data flow.

## Troubleshooting

```{trouble}
My virtual Duckiedrone does not arm.
---
Verify that the flight controller is in a safe state and that all pre-arm checks have passed. Check the `/mavros/state` topic to ensure that the mode is set correctly.
```

```{trouble}
MAVROS cannot connect to the flight controller.
---
Restart your virtual Duckiedrone using `dts duckiebot virtual restart ROBOT_NAME`, where `ROBOT_NAME` is the name of your virtual Duckiedrone.
```

```{trouble}
My virtual Duckiedrone arms but does not take off.
---
Verify that the takeoff mode was set correctly before arming. Some flight controllers require the mode to be set before arming.
```

```{trouble}
I see service call return errors.
---
Ensure that all containers in the `ros2` stack are running. Use `docker ps` or Portainer (accessible through your virtual Duckiedrone's `Dashboard` or at `ROBOT_NAME.local:9000`, where `ROBOT_NAME` is the name of your virtual Duckiedrone) to verify container statuses.
```
