

## Model Formulation
The following dynamic is proposed to model the asset price:
$$\frac{dS(t)}{S(t-)}=\mu\ dt + \sigma \ dW(t)+d\left(\sum_{i=1}^{N(t)}(V_i-1)\right)$$

where:
- W(t) is a standard Brownian motion
- N(t) is a Poisson process with rate lambda
- $V_i$ are jumps ($\Upsilon=log(V_i)$ follows a double exponential distribution)
    

## 1. Starting Point: Given p.d.f.


$$
f_\Upsilon(y) = \begin{cases}
p\ \eta_1\ e^{-\eta_1y}, & y \geq 0 \text{ (upward jump)} \\
q\ \eta_2\ e^{\eta_2y}, & y < 0 \text{ (downward jump)}
\end{cases}
$$

where:
- $p$ and $q$ are the probabilities of upward and downward jumps.
- $\eta_1>1$ is the parameter for upward jump rate.
- $\eta_2>0$ is the parameter for downward jump rate.


## 2. Goal

We want to calculate E[V-1], where $V=e^\Upsilon$.
This means we need to find $E[e^\Upsilon]-1$.

## 3. Step-by-Step Derivation
### Step 1: Use Law of Total Expectation
$$ E[X] = E[E[X|Y]]$$
Split the expectation into two parts based on $y\geq 0$ and $y<0$:

$$
\begin{aligned}
E(e^\Upsilon)&=P(\Upsilon \geq 0)E[e^\Upsilon|\Upsilon \geq 0]+P(\Upsilon < 0)E[e^\Upsilon|\Upsilon < 0]\\
&= p\cdot E[e^\Upsilon|\Upsilon\geq 0] + q\cdot E[e^\Upsilon|\Upsilon< 0]

\end{aligned}
$$



### Step 2: Calculate E[e^Y|Y>=0]
For $y\geq 0$,

$$
\begin{aligned}
E[e^\Upsilon|\Upsilon\geq 0] &= \frac{1}{P(\Upsilon\geq 0)}\int_0^\infty e^y {f_\Upsilon(y)} dy \\
&= \int_0^\infty e^y \eta_1e^{-\eta_1y} dy \\
&= \eta_1\int_0^\infty e^{-({\eta_1-1})y} dy \\
&= \eta_1 [-\frac{1}{\eta_1-1}e^{-(\eta_1-1)y}]_0^\infty \\
&= \eta_1 [0 - (-\frac{1}{\eta_1-1})] \\
&= \frac{\eta_1}{\eta_1-1}
\end{aligned}
$$

### Step 3: Calculate E[e^Y|Y<0]
For $y < 0$:

$$
\begin{aligned}
E[e^\Upsilon|\Upsilon< 0] &= \frac{1}{P(\Upsilon< 0)}\int_{-\infty}^0 e^y f_\Upsilon(y) dy \\
&= \int_{-\infty}^0 e^y \eta_2e^{\eta_2y} dy \\
&= \eta_2\int_{-\infty}^0 e^{({\eta_2+1})y} dy \\
&= \eta_2 [\frac{1}{\eta_2+1}e^{(\eta_2+1)y}]_{-\infty}^0 \\
&= \eta_2 [\frac{1}{\eta_2+1} - 0] \\
&= \frac{\eta_2}{\eta_2+1}
\end{aligned}
$$

### Step 4: Combined Results
$$E[V] = E[e^\Upsilon] = p\cdot\frac{\eta_1}{\eta_1-1} + q\cdot\frac{\eta_2}{\eta_2+1}$$

### Step 5: Final Result

$$E[V-1] = p\cdot\frac{\eta_1}{\eta_1-1} + q\cdot\frac{\eta_2}{\eta_2+1} - 1$$

## 4.Code Implementation

The jump expectation is calculated in [`src/models/jump_process.py`](../../src/models/jump_process.py#L3-L15)