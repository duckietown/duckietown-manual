(duckiedrone-demo-takeoff)=
# Duckiedrone Takeoff Demo (ROS2)

```{seo}
:description: The Takeoff demo (demonstration) for a Duckiedrone.
:keywords: Duckietown, Duckiedrone, Takeoff, demo, demonstration, ROS2, mavros, PX4
```

This chapter describes the `Takeoff` demo (demonstration) for Duckiedrones using ROS2.

```{needget}
- A virtual Duckiedrone.
* ROS2 stack installed and configured.
* MAVROS2 interface properly set up.
---
A Duckiedrone successfully arming and taking off autonomously.
```

(demo-duckiedrone-takeoff-expected)=
## Introduction to Duckiedrone takeoff

```{vimeo} 1146828852
```

(demo-duckiedrone-takeoff-setup)=
## Setup

To set up the demo:

1. Create a virtual Duckiedrone:

    ```shell
    dts duckiebot virtual create -t duckiedrone -c DD24 ROBOT_NAME
    ```

2. Once the creation is complete, start it:

    ```shell
    dts duckiebot virtual start ROBOT_NAME
    ```

3. Start the ROS2 stack on the drone:

    ```shell
    dts stack up -d -H ROBOT_NAME ros2/duckiedrone
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
    dts matrix attach ROBOT_NAME map_0/vehicle_1
    ```


```{note}
Wait for all containers to be running before proceeding to the next step.
```

(demo-duckiedrone-takeoff-run)=
## Start

The code for the demo can be found in the [dt-ros2-interface repository](https://github.com/duckietown/dt-ros2-interface/tree/ente).

To clone the `dt-ros2-interface` repository, run:

```shell
git clone git@github.com:duckietown/dt-ros2-interface.git --branch ente
```

To build the `dt-ros2-interface` image on your Duckiedrone, run the following command from the newly created `dt-ros2-interface` directory:

```shell
dts devel build -H ROBOT_NAME
```

To run the demo on your Duckiedrone, run the following command from the newly created `dt-ros2-interface` directory:

```shell
dts devel run -H ROBOT_NAME -c bash -- -e ROS_DOMAIN_ID=42
```

Inside the bash prompt that appears:

1. Set the drone to takeoff mode:

    ```bash
    ros2 service call /mavros/set_mode mavros_msgs/srv/SetMode "{base_mode: 0, custom_mode: 'AUTO.TAKEOFF'}"
    ```

    Expected output:

    ```bash
    response:
    mavros_msgs.srv.SetMode_Response(mode_sent=True)
    ```

2. Arm the drone to initiate takeoff:

    ```bash
    ros2 service call /mavros/cmd/arming mavros_msgs/srv/CommandBool "{value: true}"
    ```

    Expected output:

    ```bash
    requester: making request: mavros_msgs.srv.CommandBool_Request(value=True)
    response:
    mavros_msgs.srv.CommandBool_Response(success=True, result=0)
    ```


Your Duckiedrone should now arm and begin its takeoff sequence to a default height of 2.5m.


## Stop

To stop the demo:

1. Land the drone by setting the drone into land mode:
    ```bash
    ros2 service call /mavros/set_mode mavros_msgs/srv/SetMode "{base_mode: 0, custom_mode: 'AUTO.LAND'}"
    ```

2. Select the terminal from which the demo was run.
3. Press <kbd>Ctrl</kbd>+<kbd>D</kbd>.

(demo-duckiedrone-takeoff-visualization)=

## How it works

The `Takeoff` demo consists of the following steps:

1. **MAVROS interface** establishes communication between ROS2 and the PX4 flight controller via the MAVLink protocol.
2. **Mode setting** configures the flight controller to `AUTO.TAKEOFF` mode, which prepares the drone for autonomous takeoff.
3. **Arming** enables the motors, allowing the drone to generate thrust.
4. **Takeoff execution** uses the flight controller's autopilot to execute a controlled vertical ascent to a predefined altitude.

The MAVROS node acts as a bridge, translating ROS2 service calls and topic publications into MAVLink messages that the flight controller understands, and vice versa.

(demo-duckiedrone-takeoff-parameter-tuning)=
## Debugging and parameter tuning

If the performance of your Duckiedrone is inconsistent or the takeoff does not execute properly, consider the following debugging steps.

### Verifying MAVROS connection

Check that MAVROS is properly connected to the flight controller:

```bash
ros2 topic echo /mavros/state
```

You should see output indicating that the flight controller is connected and the mode is being reported.

### Checking sensor data

Verify that sensor data is being published:

```bash
ros2 topic list
```

Look for topics such as `/mavros/imu/data`, `/mavros/battery`, and `/mavros/altitude` and echo them to verify data flow.

(demo-duckiedrone-takeoff-troubleshooting)=
## Troubleshooting

```{trouble}
The drone does not arm.
---
Verify that the flight controller is in a safe state and that all pre-arm checks have passed. Check the `/mavros/state` topic to ensure the mode is set correctly.
```

```{trouble}
MAVROS cannot connect to the flight controller.
---
Restart the virtual Duckiedrone using `dts duckiebot virtual restart ROBOT_NAME`.
```

```{trouble}
The drone arms but does not take off.
---
Verify that the takeoff mode was set correctly before arming. Some flight controllers require the mode to be set before arming.
```

```{trouble}
Service calls return errors.
---
Ensure that the ROS_DOMAIN_ID is set correctly (42) and that all containers in the ROS2 stack are running. Use `docker ps` or portainer (accessible through the dashboard or at ROBOT_NAME.local:9000) to verify container status.
```

