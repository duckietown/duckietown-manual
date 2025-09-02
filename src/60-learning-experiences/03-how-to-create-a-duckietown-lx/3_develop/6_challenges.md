(lx-challenges)=
# Evaluated Challenges

```{warning}
Update April 2025: The challenges server is undergoing maintainance as we move towards a new simulation environment.
```

The agents developed in LXs can be evaluated against a set of benchmarks defined as a _Duckietown Challenge_.

Learners may evaluate their agent locally via 

    dts code evaluate

or on the _Duckietown Challenges Server_ via 

    dts code submit

In each of these cases, a report is created against these benchmark metrics along with visualizations of the agent's behavior in simulation.  Server submissions are appended to a running leaderboard, allowing learners to compare their solutions with previous work.

You can explore previous challenge definitions and the related student submissions on the [Duckietown Challenges Server](https://challenges.duckietown.org).

```{figure} ../../_images/lx-devmanual/create/challenges_server.png
:name: challenges-server

Each challenge and linked learner submissions can be found on the Duckietown Challenges Server.
```

## Development Guidelines

```{admonition} Communicating benchmarks:
It is recommended that the evaluation metrics for a challenge are clearly defined in the *Grading* section of the Learning Experience `README.md` file to give learners clear performance goals for their agent.
```

```{admonition} Encouraging frequent commits:
Students should also be encouraged to bookmark their development at each submission attempt with a git commit referencing the submission number.  This allows them to easily track and revert to prior attempts.
```

## Tutorial: Creating and Linking a Duckietown Challenge

Learning Experiences can be associated with a predefined challenge by updating the fields in the file `recipe/submission.yaml`.

```{attention}
The ability to create custom challenges for a Learning Experience has not yet been released.  Please check back later for future updates.
```