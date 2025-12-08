```{seo}
:description: A quick recap of probabilistic theory as it is useful for understanding robotics applications, such as stochastic recursive filtering. 
:keywords: Duckietown, probability theory, stochasticy in robotics
```

```{needget}
- Foundations of mathematics
---
- Foundations of probability theory
```

(dt-probability-basics)=
# Probability basics for Duckietown

In this chapter we give a brief review of some basic probabilistic concepts.

For a more in-depth treatment of the subject we refer the interested reader to a textbook such as {cite}`Papoulis`.

(dt-probability-basics-random-variables)=
## Random Variables

The key underlying concept in probabilistic theory is that of an *event*, which is the output of a random trial. Examples of an event include the result of a coin flip turning up HEADS or the result of rolling a die turning up the number "4".

```{admonition} Definition: Random Variable
:class: attention
A (either discrete or continuous) variable that can take on any value that corresponds to the feasible output of a random trial.
```

$$
\newcommand{\state}{x}
  \newcommand{\aset}[1]{\mathcal{#1}}
  \newcommand{\heads}{\textsf{HEADS}}
  \newcommand{\tails}{\textsf{TAILS}}
$$

For example, we could model the event of flipping a fair coin with the random variable $X$. We write the probability that $X$ takes $\heads$ as $p(X=\heads)$. The set of all possible values for the variable $X$ is its *domain*, $\aset{X}$.

In this case,

$$
    \aset{X}=\{\heads,\tails\}.
$$

Since $X$ can only take one of two values, it is a *binary* random variable. In the case of a die roll,

$$
    \aset{X}=\{1,2,3,4,5,6\},
$$

and we refer to this as a *discrete* random variable. If the output is real value or a subset of the real numbers, e.g., $\aset{X} = \mathbb{R}$, then we refer to $X$ as a *continuous* random variable.

Consider once again the coin tossing event. If the coin is fair, we have

$$
    p(X=\heads)=p(X=\tails)=0.5.
$$

Here, the function $p(x)$ is called the *probability mass function* or PMF. The PMF is shown in [](fig:binary_pmf).

```{figure} ../_images/further_reading/preliminaries/probability/binary_pmf.svg
:alt: The pmf for a fair coin toss
:width: 80%
:name: fig:binary_pmf
:align: center

The Probability Mass Function (PMF) for a fair coin toss
```

<!--
<div figure-id="fig:binary_pmf" figure-caption="The pmf for a fair coin toss">
  <img src="binary_pmf.svg" style='width: 30em'/>
</div>
-->

Here are some very important properties of $p(x)$:

- $0\leq p(x) \leq (1)$

- $\sum_{x\in\aset{X}}=1$

In the case of a continuous random variable, we will call this function $f(x)$ and call it a *probability density function*, or PDF.

In the case of continuous RVs, technically the $p(X=x)$ for any value $x$ is zero since $\aset{X}$ is infinite. To deal with this, we also define another important function, the *cumulative density function*, which is given by $F(x) \triangleq p(X\leq x)$, and now we can define $f(x) \triangleq \frac{d}{dx}F(x)$.

A PDF and corresponding CDF are shown in [](fig:pdf_cdf). This happens to be a Gaussian distribution, defined more precisely in [](#gaussian).

```{figure} ../_images/further_reading/preliminaries/probability/pdf_cdf.svg
:alt: The continuous PDF and cdf
:width: 80%
:name: fig:pdf_cdf
:align: center

The continuous probability and cumulative density functions (PDF and CDF, respectively)
```

<!--
<div figure-id="fig:pdf_cdf" figure-caption="The continuous pdf and cdf">
  <img src="pdf_cdf.svg" style='width: 30em'/>
</div>
-->

(dt-probability-basics-joint-probabilities)=
### Joint Probabilities

If we have two different RVs representing two different events $X$ and $Y$, then we represent the probability of two distinct events $x \in \aset{X}$ and $y \in \mathcal{Y}$ both happening, which we will denote as follows:

$$
p(X=x \; \text{AND} \; Y=y) = p(x,y)
$$

The function $p(x,y)$ is called *joint distribution*.

(dt-probability-basics-conditional-probabilities)=
### Conditional Probabilities

Again, considering that we have to RVs, $X​$ and $Y​$, imagine these two events are linked in some way. For example, $X​$ is the numerical output of a die roll and $Y​$ is the binary even-odd output of the same die roll. Clearly these two events are linked since they are both uniquely determined by the same underlying event (the rolling of the die). In this case, we say that the RVs are *dependent* on one another.

In the event that we know one of events, this gives us some information about the other. We denote this using the following *conditional distribution*

$$
p(X=x \; \text{GIVEN} \; Y=y) \triangleq p(x|y).
$$


<div class="check" markdown="1">
Write down the conditional pmf for the scenario just described assuming an oracle tells you that the die roll is even. In other words, what is $p(x|\text{EVEN})$?

If you think this is very easy that's good, but don't get over-confident.
</div>


The joint and conditional distributions are related by the following (which could be considered a definition of the joint distribution):

$$
p(x,y) = p(x|y)p(y)
\label{eq:joint}
$$

and, similarly, the following could be considered a definition of the conditional distribution:

$$
p(x|y) = \frac{p(x,y)}{p(y)} \; \text{if} \; p(y) > 0
\label{eq:condition}
$$

In other words, the conditional and joint distributions are inextricably linked: you can't really talk about one without the other.

If two variables are *independent*, then the following relation holds: $p(x,y)=p(x)p(y)$.

(dt-probability-basics-bayes-rule)=
### Bayes' Rule

Upon closer inspection of \eqref{eq:joint}, we can see that the choice of which variable to condition upon is completely arbitrary. We can write:

$$
p(y|x)p(x) = p(x,y) = p(x|y)p(y)
$$

and then after rearranging things we arrive at one of the most important formulas for mobile robotics, Bayes' rule:

$$
p(x|y) = \frac{p(y|x)p(x)}{p(y)}
\label{eq:bayes}
$$

Exactly why this formula is so important might (at some point) be covered in more detail in later sections, but we will give an initial intuition here.

Consider that the variable $X$ represents something that we are trying to estimate but cannot observe directly, and that the variable $Y$ represents a physical measurement that relates to $X$. We want to estimate the distribution over $X$ given the measurement $Y$, $p(x|y)$, which is called the *posterior* distribution. Bayes' rule lets us to do this.

For every possible state, you take the probability that this measurement could have been generated, $p(y|x)$, which is called the *measurement likelihood*, you multiply it by the probability of that state being the true state, $p(x)$, which is called the *prior*, and you normalize over the probability of obtaining that measurement from any state, $p(y)$, which is called the *evidence*.


<div class="check" markdown="1">
From Wikipedia:
Suppose a drug test has a 99% true positive rate and a 99% true negative rate, and that we know that exactly 0.5% of people are using the drug. Given that a person's test gives a positive result, what is the probability that this person is actually a user of the drug.

Answer: $\approx$ 33.2%.

This answer should surprise you. It highlights the power of the *prior*.
</div>

(dt-probability-basics-marginal-distributions)=
### Marginal Distribution

If we already have a joint distribution $p(x,y)$ and we wish to recover the single variable distribution $p(x)$, we must *marginalize* over the variable $Y$. The involves summing (for discrete RVs) or integrating (for continuous RVs) over all values of the variable we wish to marginalize:

$$
\begin{align}
p(x) &= \sum_{\mathcal{Y}} p(x,y) \\
f(x) &= \int p(x,y) dy
\end{align}
$$

This can be thought of as projecting a higher dimensional distribution onto a lower dimensional subspace. For example, consider [](fig:marginals), which shows some data plotted on a 2D scatter plot, and then the marginal histogram plots along each dimension of the data.

```{figure} ../_images/further_reading/preliminaries/probability/marginals.svg
:alt: A 2D joint data and 2 marginal 1D histogram plots
:width: 80%
:name: fig:marginals
:align: center

A 2D joint data and 2 marginal 1D histogram plots
```

<!--
<div figure-id="fig:marginals" figure-caption="A 2D joint data and 2 marginal 1D histogram plots">
  <img src="marginals.svg" style='width: 30em'/>
</div>
-->

Marginalization is an important operation since it allows us to reduce the size of our state space in a principled way.

(dt-probability-basics-cond-independence)=
### Conditional Independence

If two RVs, $X$ and $Y$ are correlated, we may be able to encapsulate the dependence through a third random variable $Z$. Therefore, if we know $Z$, we may consider $X$ and $Y$ non correlated to each other. 

```{figure} ../_images/further_reading/preliminaries/probability/conditional_independence.png
:alt: A graphical representation of the conditional independence of X and Y given Z
:width: 40%
:name: fig:conditional_independence
:align: center

A graphical representation of the conditional independence of $X$ and $Y$ given $Z$
```

<!--
<div figure-id="fig:conditional_independence" figure-caption="A graphical representation of the conditional independence of $X$ and $Y$ given $Z$">
  <img src="conditional_independence.pdf" style='width:10em; height:auto' />
</div>
-->

```{note}
Graphical models deserve an independent discussion. Doing a good job of sufficiently describing graphical models and the dependency relations that they express requires careful thought. Until the editors of this manual get it it, we refer curious readers to e.g.: Koller and Friedman.
```

(dt-probability-basics-moments)=
### Moments

The $n$th moment of an RV, $X$, is given by $E[X^n]$ where $E[]$ is the expection operator with:

$$
E[f(X)] = \sum_{\aset{X}} x \, f(x)
$$

in the discrete case, and

$$
E[f(X)] = \int x\, f(x) dx
$$

in the continuous case.

The 1st moment is the *mean*, $\mu_X=E[X]$.

The $n$-th central moment of an RV, $X$ is given by $E[(X-\mu_X)^n]$.

The second central moment is called the *covariance*, $\sigma^2_X=E[(X-\mu_X)^2]$.

<!--
Another equation:

$$
p(x|y) = \aset{X}
$$
-->

(dt-probability-basics-entropy)=
### Entropy


```{admonition} Definition: Entropy
:class: attention
The *entropy* of an RV is a scalar measure of the uncertainty about the value the RV.
```

<!--
\begin{definition}\label{def:entropy}
The *entropy* of an RV is a scalar measure of the uncertainty about the value the RV.
\end{definition}
-->

A common measure of entropy is the *Shannon entropy*, whose value is given by

$$
H(X)=-E[\log_2 p(x)]
\label{eq:shannon}
$$

This measure originates from communication theory and literally represents how many bits are required to transmit a distribution through a communication channel. For many more details related to information theory, we recommend {cite}`MacKay_book`.

As an example, we can easily write out the Shannon entropy associated with a binary RV (e.g. flipping a coin) as a function of the probability that the coin turns up heads (call this $p$):

$$
H(X) = -p\log_2 p - (1-p)\log_2 (1-p).
\label{eq:binary_entropy}
$$

```{figure} ../_images/further_reading/preliminaries/probability/entropy.svg
:alt: A graphical representation of the conditional independence of X and Y given Z
:width: 60%
:name: fig:entropy_binary
:align: center

The Shannon entropy of a binary RV $X$.
```
<!--
<div figure-id="fig:entropy_binary" figure-caption="The Shannon entropy of a binary RV $X$">
  <img src="entropy.svg" style='width: 30em;'/>
</div>
-->

Notice that our highest entropy (uncertainty) about the outcome of the coin flip is when it is a fair coin (equal probability of heads and tails). The entropy decays to 0 as we approach $p=0$ and $p=1$ since in these two cases we have no uncertainty about the outcome of the flip. It should also be clear why the function is symmetrical around the $p=0.5$ value.

(dt-probability-gaussian-distribution)=
### The Gaussian Distribution

In mobile robotics we use the Gaussian, or normal, distribution a lot.


The 1-D Gaussian distribution pdf is given by:

$$
\mathcal{N}(x|\mu,\sigma^2) = \frac{1}{\sqrt{2\pi \sigma^2}}e^{-\frac{1}{2\sigma^2}(x-\mu)^2}
\label{eq:gaussian1D}
$$

where $\mu$ is called the *mean* of the distribution, and $\sigma$ is called the *standard deviation*. A plot of the 1D Gaussian was previously shown in [](fig:pdf_cdf).

We will rarely deal with the univariate case and much more often deal with the multi-variate Gaussian:

$$
\mathcal{N}(\state|\mathbf{\mu},\mathbf{\Sigma}) = \frac{1}{(2\pi)^{D/2}|\mathbf{\Sigma}|^{1/2}}\exp[-\frac{1}{2}(\state-\mathbf{\mu})^T\mathbf{\Sigma}^{-1}(\state - \mathbf{\mu})]
\label{eq:gaussianND}
$$

The value from the exponent: $(\state-\mathbf{\mu})^T\mathbf{\Sigma}^{-1}(\state - \mathbf{\mu})$ is sometimes written
$||\state - \mathbf{\mu}||_\mathbf{\Sigma}$ and is referred to as the *Mahalanobis distance* or *energy norm*.

Mathematically, the Gaussian distribution has some nice properties as we will see. But is this the only reason to use this as a distribution. In other words, is the assumption of Gaussianicity a good one?

There are two very good reasons to think that the Gaussian distribution is the "right" one to use in a given situation.

1. The *central limit theorem* says that, in the limit, if we sum an increasing number of independent random variables, the distribution approaches Gaussian

2. It can be proven [editor's note: add reference] that the Gaussian distribution has the maximum entropy subject to a given value for the first and second moments. In other words, for a given mean and variance, it makes the *least* assumptions about the other moments.

Suggested exercise: derive the formula for Gaussian entropy.

(dt-probability-banana-distribution)=
### Banana distributions?

```{admonition} Comment from AC
:class: tip
The Banana distribution is the official distribution in robotics!
```

```{admonition} Counter-comment from LP
:class: tip
The [Banana distribution is Gaussian](http://www.roboticsproceedings.org/rss08/p34.pdf)!
```


(dt-probability-refs)=
### References

```{bibliography}
:filter: docname in docnames
```