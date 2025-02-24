
## 1. Variance Formula

$$Var[V-1] = Var[e^\Upsilon] = E[(e^\Upsilon)^2] - (E[e^\Upsilon])^2$$

## 2. Calculate E[e^Y]
Since we already have $E[e^\Upsilon]$ in [`formulas/jump_expectation.md`](../formulas/jump_expextation.md)

From previous calculation:
$$E[V] = E[e^\Upsilon] = p\cdot\frac{\eta_1}{\eta_1-1} + q\cdot\frac{\eta_2}{\eta_2+1}$$

## 3. Calculate E[(e^Y)^2]
### Step 3.1: For y>=0
$$
\begin{aligned}
E[(e^\Upsilon)^2|\Upsilon\geq 0] &= \int_0^\infty e^{2y} \eta_1e^{-\eta_1y} dy \\
&= \eta_1\int_0^\infty e^{-({\eta_1-2})y} dy \\
&= \eta_1 \left[-\frac{1}{\eta_1-2}e^{-(\eta_1-2)y}\right]_0^\infty \\
&= \frac{\eta_1}{\eta_1-2}
\end{aligned}
$$

### Step 3.2: For y<0
$$
\begin{aligned}
E[(e^\Upsilon)^2|\Upsilon< 0] &= \int_{-\infty}^0 e^{2y} \eta_2e^{\eta_2y} dy \\
&= \eta_2\int_{-\infty}^0 e^{({\eta_2+2})y} dy \\
&= \eta_2 \left[\frac{1}{\eta_2+2}e^{(\eta_2+2)y}\right]_{-\infty}^0 \\
&= \frac{\eta_2}{\eta_2+2}
\end{aligned}
$$

### Step 3.3: Combine Results
$$E[(e^\Upsilon)^2]=p\frac{\eta_1}{\eta_1-2}+q\frac{\eta_2}{\eta_2+2}$$

## 4. Final Variance Formula
$$
\begin{aligned}
Var[V-1] &=Var[e^\Upsilon]\\
&= E[(e^\Upsilon)^2] - (E[e^\Upsilon])^2 \\
&= p\frac{\eta_1}{\eta_1-2} + q\frac{\eta_2}{\eta_2+2} - (p\frac{\eta_1}{\eta_1-1} + q\frac{\eta_2}{\eta_2+1})^2
\end{aligned}
$$

## 5.Code Implementation

The jump expectation is calculated in [`src/models/jump_process.py`](../../src/models/jump_process.py#L17)

