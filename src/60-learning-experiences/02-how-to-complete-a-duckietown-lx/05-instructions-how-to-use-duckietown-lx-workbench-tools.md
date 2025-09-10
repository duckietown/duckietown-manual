```{seo}
:description: Discover how to use the Duckietown Workbench environment to run simulations and agent-based tools in robotics education.
:keywords: Duckietown, workbench, robotics simulation, tools, learning experience
```

(dts-code-workbench)=
# `dts code workbench`

## What does it do?

The `dts code workbench` command runs the workbench portion of a learning experience, 
which provides a virtual desktop tool (the VNC) with three different purposes,

1. **VNC Visualization Tools**: In any LX notebook activity, you may be directed to use the `dts code workbench` 
   command to open the VNC and run a visualization or calibration tool.  This provides a more advanced 
   interface to complement the notebook experience;
2. **Duckietown Simulator**: The simulator interface runs agents developed in the LX on a Duckiebot in a virtual 
   world. Keep an eye out for any duckies that may be wandering around the simulated road;
3. **Duckiebot Agent Interface**: The `dts code workbench` command is also your interface for running agents on your 
   real world Duckiebot.

The focus of the workbench is to provide a streamlined experience for testing and deploying the activities and 
solutions that you develop while working through a learning experience.


## How do I run it?

1. To run an activity visualization or calibration in the VNC, run

         dts code workbench --sim

   and follow the instructions in the notebook to select the correct desktop icon and run the tool.

2. To test in simulation, use the command

       dts code workbench --sim
   
   There will be two URLs popping up to open in your browser: one is the direct view of the
   simulated environment. The other is VNC and only useful for some exercises, follow the instructions
   in the notebooks to see if you need to access VNC.
   
   This simulation test is just that, a test. Don't trust it fully. If you want a more accurate
   metric of performance, use the `dts code evaluate` command described on the next page.

3. You can test your agent on the robot using the command,
   
       dts code workbench --duckiebot [ROBOT_NAME]
   
   This is the modality "all software runs on the robot".
   
   You can also test using
   
       dts code workbench --duckiebot [ROBOT_NAME] --local 
   
   This is the modality "drivers running on the robot, agent running on the laptop."

If you run into any issues using this command, you can search the troubleshooting symptoms below or reference the [](how-to-get-help) section of this manual.

## Troubleshooting

```{trouble}

`dts :  The path '/home/myuser/not_an_lx_directory' does not appear to be a Duckietown project. 
     :  The metadata file '.dtproject' is missing.`

---
You need to be in the root directory of the LX in order to run the `dts code` commands.
```

```{trouble}
 
 These errors appear: `requests.exceptions.HTTPError: 500 Server Error: Internal Server Error for url: http+docker://localhost/v1.43/containers/84ce.../start`
 
 and it is complained that certain ports are in conflict and could not be used.
 
 ---
 
 Please check your running docker containers and ports with: `docker ps --format "table {{.Names}}\t{{.Image}}\t{{.ID}}\t{{.Ports}}"`
 And stop the ones unnecessary, that occupy the mentioned conflicted ports.
 ```

## Extra Options

```{warning}
If this is your first time using the `dts code workflow`, do not worry about the following section just yet. Continue 
on to the next page to evaluate the soliution to your first LX activity.
```

Once you are comfortable with the `dts code` workflow, you may want to use some additional control provided 
over each command.  This section documents each of the flags available to extend the `dts code workbench` command.

You can also explore the [Behind the Scenes - dts code workbench](behind-the-scenes-code-workbench) chapter 
for more details on what happens in the background when you run the `dts code workbench` command.

### Command options

```
Usage:

  $ dts code workbench --sim
  $ dts code workbench --duckiebot [ROBOT_NAME]

optional arguments:
  -h, --help            show this help message and exit
  -C WORKDIR, --workdir WORKDIR
                        Directory containing the project to bring up
  --duckiebot DUCKIEBOT, -b DUCKIEBOT
                        Name of the Duckiebot on which to run the exercise
  -s, --simulation, --sim, --simulator
                        Should we run it in the simulator instead of the real robot?
  --stop                Just stop all the containers
  --local, -l           Should we run the agent locally (i.e. on this machine)? Important Note: this is not expected to work on MacOSX
  --recipe RECIPE       Path to use if specifying a custom recipe
  --pull                Should we pull all of the images
  --no-cache            Ignore the Docker cache
  --bind BIND           Address to bind to (VNC)
  --logs LOGS           Use --logs NAME:LEVEL to set up levels. The container names and their defaults are [agent:Levels.LEVEL_DEBUG
                        manager:Levels.LEVEL_NONE simulator:Levels.LEVEL_NONE bridge:Levels.LEVEL_NONE vnc:Levels.LEVEL_NONE]. The levels are
                        none, debug, info, warning, error.
  --log_dir LOG_DIR     Logging directory
  -L LAUNCHER, --launcher LAUNCHER
                        Launcher to invoke inside the exercise container (advanced users only)
  --registry REGISTRY   Docker registry to use (advanced users only)
  --interactive, -i     Will run the agent in interactive mode with the code mounted
  --keep                Do not auto-remove containers once done. Produces garbage containers but it is very useful for debugging.
  --sync                RSync code between this computer and the agent
  --challenge CHALLENGE
                        Run in the environment of this challenge.
  --scenarios SCENARIOS
                        Uses the scenarios in the given directory.
  --step STEP           Run this step of the challenge
  --nvidia              Use the NVIDIA runtime (experimental).
```