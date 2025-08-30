```{seo}
:description: Duckietown introduction to Markov decision processees (MDPs) used to develop reinforcement learning (RL) problem.
:keywords: markov decision process, MDP, reinforcement learning, RL, machine learning, ML, AI, embedded AI, POMDP, policy, duckietown
```
(slides-and-recordings-mdp)=
# Markov Decision Processes

The mathematical formalism that we will use to develop in particular reinforcement learning algorithms is the Markov Decision Process, or MDP. 

The MDP comprises a state representation (that satisfies the Markov property), an action space, a transition function, a reward function, and a discount factor. In the case that we are estimating the state through sensor data, this becomes a partially observable MDP, or POMDP. In this context, our objective is to find a good policy. 

```{vimeo} 587461397
:alt: Markov Decision Processes
```
