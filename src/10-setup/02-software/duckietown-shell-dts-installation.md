(setup-dts)=
# Duckietown Shell (`dts`)

```{seo}
:description: How to install and set up the Duckietown Shell, the terminal based and most powerful UI in Duckietown.
:keywords: Duckietown, Duckiebot, dts, Duckietown Shell, UI, terminal interface
```

This section describes how to install and set up `dts` (`Duckietown Shell`), a CLI (Command-Line Interface) program that is used for Duckietown-related operations.

```{needget}
- [Docker is installed and set up](setup-sw-docker)
- [GitHub is installed and set up](setup-sw-github)
- [Duckietown account](setup-account-duckietown-hub)
---
- A computer with `dts` installed and correctly set up.
```

(setup-dts-installation)=
## Duckietown Shell (`dts`) Installation

:::::{tab-set}

::::{tab-item} Ubuntu

````{attention}
If you have already installed `dts` using `pip3`, run the following command and follow the on-screen instructions:

```shell
pip3 uninstall duckietown-shell
```
````

To install `dts`, run:

```shell
pipx install duckietown-shell
```

::::

::::{tab-item} Duckietown Workspace

The Duckietown Shell is pre-installed in Workspaces. Run the checkpoint to verify it is working as intended.

::::

:::::


````{warning}
If you are installing `dts` on an arm machine you will also need to install the `gcc` and `python3-dev` dependencies:

    sudo apt install -y gcc python3-dev

This includes Apple Silicon macs with Ubuntu arm64 virtual machines.
````

(setup-dts-checkpoint1)=
### Checkpoint 1 ✅

To verify that `dts` has been installed correctly:

````{testexpect}
Run:

```shell
which dts
---
The path to `dts`.
````

(setup-dts-configuration)=
## Duckietown Shell (`dts`) configuration

To appropriately configure the Duckietown Shell:

1. [Login into `dts` as a Duckietown User](dt-account-set-token)
2. [Provide `dts` with your DockerHub credentials](dt-account-dockerhub-config-docker-set)

(dt-account-set-token)=
### Logging in the Duckietown Shell

To log into `dts` with your user configurations:

1. Open a terminal and run `dts`
2. Select `ente` using <kbd>UpArrow</kbd> and <kbd>DownArrow</kbd>.
3. Press <kbd>Enter</kbd>.
4. Obtain and copy your [Duckietown token](duckietown-token)
5. Paste your `dt2` token into the terminal.
6. Press <kbd>Enter</kbd>.
7. Run `dts update`.

````{note}
The resulting output after step 6 should look like the following, where `UID` is your Duckietown UID (User ID):

```shell
dts :  Correctly identified as uid = UID
```
````

(dt-account-switch)=
### Switching user in the Duckietown Shell

You can switch users logged into `dts` by with:

```shell
dts tok set
```

To verify which user is logged in:

```shell
dts tok status
```

(dt-account-switch-profile)=
### Duckietown Shell (`dts`) profiles

To get a list of the available `dts` profiles, run:

```shell
dts profile list
```

to see the available profiles. E.g., 

```bash
   | Profile | Distribution | Staging
-- | ------- | ------------ | -------
>> |    ente |         ente |      No
```

To create a new `dts` profile:

1. Run `dts profile new`.
2. Select the name of the profile to create using <kbd>UpArrow</kbd> and <kbd>DownArrow</kbd>.
3. Press <kbd>Enter</kbd>.
4. Obtain and copy your [Duckietown token](duckietown-token)
5. Paste your `dt2` token into the terminal.
6. Press <kbd>Enter</kbd>.

To switch to a different `dts` profile, run the following command, where `PROFILE` is the name of the profile:

```shell
dts profile switch PROFILE
```

(dt-account-dockerhub-config-docker-set)=
### Configure Docker in the Duckietown Shell

To automate most of the back-end operations involving Docker, 

```bash
dts config docker credentials set --username DOCKERHUB_USERNAME --password DOCKERHUB_ACCESS_TOKEN
```

* recall your `DOCKERHUB_USERNAME` from [](dt-account-dockerhub) and 
* create a PAT following [DockerHub instructions on access tokens](https://docs.docker.com/security/access-tokens/)


```{attention}
* These credentials are **only stored locally**;
* **Never use your account password** instead of an personal access tokens (PAT);
```

```{admonition} For developers
:class: dropdown

With an extra **positional** argument, one could specify a custom Docker registry server other than
`docker.io`. Check `dts config docker set --help` for more details.
```

### Resetting the Duckietown Shell

To reset `dts` to "factory conditions", run:

```shell
rm -rf ~/.duckietown/shell
```

and proceed to reconfigure your `dts`: [](dt-account-set-token).

---

### Checkpoint 2 ✅

```{tip}
Never skip a checkpoint!\
If you have trouble with any of these commands, see the FAQs section below. If you cannot find answers, use the Duckietown support channels to get help.
```

````{testexpect}
If your Docker login was successful, you should be able to run
```bash
dts config docker credentials info
---
You should see an output similar to the following,

```bash
Docker credentials:
. registry:   docker.io
. username:   DOCKERHUB_USERNAME
. secret:   DOCKERHUB_ACCESS_TOKEN
````

<!--
(dt-account-dockerhub-shell-credentials)=
### 1) Configure the Duckietown Shell

The first thing you need to do with `dts` is to set the Duckietown software distribution you want to work with.
For this version of the book, we use daffy. Set the shell to use a profile on the daffy distribution by running the command

    dts profile switch daffy

(dt-account-register)=
### 2) Get a Duckietown Token

Now your Duckietown Shell needs a Duckietown token. The Duckietown Token allows you to authenticate yourself and your robots against the Duckietown network.

You can make a Duckietown account for free from the Duckietown Hub.
[Make an account here.](https://hub.duckietown.com/signup/)

The token is a string of letters and numbers that looks something like this:

    dt1-7vEuJsaxeXXXXX-43dzqWFnWd8KBa1yev1g3UKnzVxZkkTbfSJnxzuJjWaANeMf4y6XSXBWTpJ7vWXXXX

To find your token, first [log in](https://hub.duckietown.com/signin/) to your account,
then open [the profile page](https://hub.duckietown.com/profile/) in your browser:

Copy your token to use in the next step.
-->

### Troubleshooting

```{trouble}
I mistakenly set a wrong/unwanted username or password. How can I update the credentials?
---
Just run the command again with the correct credentials.
Only the latest inputs are stored for the same Docker registry.
```

````{trouble}
I would like to remove my stored Docker credentials. How could I achieve that?
---
Run: 
```bash
rm ~/.duckietown/shell/profiles/ente/databases/secrets_docker.yaml
````