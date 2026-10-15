```{seo}
:description: Learn how to create a Duckietown account and get a token to authenticate your Duckietown Shell.
:keywords: Duckietown, setup, accounts, Duckietown Hub, Duckietown token, DTS
```

(setup-account-duckietown-hub)=
# Duckietown Account

```{needget}
- Nothing
---
- A Duckietown account
```

A Duckietown account is necessary to operate Duckietown software. Duckietown accounts are created through the [Duckietown Hub](https://hub.duckietown.com).

- [Create a Duckietown account on the Duckietown Hub](https://hub.duckietown.com/signup/)

Take note of your Duckietown Hub login credentials and move on to the next step.

(duckietown-token)=
## Duckietown Token

Once logged in your Duckietown Hub account, go to [https://hub.duckietown.com/profile/](https://hub.duckietown.com/profile/) and scroll down until you find your Duckietown token. Take note of this token and do not share it publicly.

```{note}
You do not need a plan to create a Duckietown token. Use this token to log into DTS, including when using `daffy`. Access to `ente` and Duckiematrix follows the [plan and computer-access rules](setup-dts-plans).
```

```{figure} ../../_images/setup/accounts/dt-token.png
:alt: example Duckietown token dt2
:width: 90%
:name: duckietown-token-dt2
:align: center

Duckietown token for personal authentication.
```

```{attention}
Make sure your token starts with `dt2`. Legacy `dt1` tokens are only useful in corner cases which you should not run into.
```

(duckietown-plans)=
## Choosing a Duckietown plan

Creating an account or generating an identity token does not select a plan.

1. Verify your email address using the verification message from the Hub. Email verification is required before choosing a plan.

2. Open the [Duckietown Hub plans page](https://hub.duckietown.com/plans/) while logged in and choose the plan appropriate for your use, or redeem the seat code provided by your institution.

The free Independent User plan and active Institutional User plan provide the qualifying access described in [](setup-dts-plans). That section also explains the grace period ending on 1 February 2027 at 00:00 UTC, the one-computer limit, and how to transfer to a replacement computer. The Instructor add-on alone does not qualify after the grace period.
