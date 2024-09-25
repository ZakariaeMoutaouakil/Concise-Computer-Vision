# Taylor Expansion of I(x,y,t) up to 3rd-order Derivatives

The Taylor expansion of a function I(x,y,t) around the point (x₀, y₀, t₀) up to the 3rd-order derivatives can be
expressed in a compact form using matrix notation. Let's break it down step by step:

## 1. First-order Terms

The first-order terms can be written as a dot product of the gradient and the displacement vector:

$$\nabla I \cdot \begin{bmatrix} x - x_0 \\ y - y_0 \\ t - t_0 \end{bmatrix}$$

where $\nabla I = \begin{bmatrix} \frac{\partial I}{\partial x} \\ \frac{\partial I}{\partial y} \\ \frac{\partial I}{\partial t} \end{bmatrix}$

## 2. Second-order Terms

The second-order terms involve the Hessian matrix:

$$\frac{1}{2} \begin{bmatrix} x - x_0 & y - y_0 & t - t_0 \end{bmatrix} H \begin{bmatrix} x - x_0 \\ y - y_0 \\ t - t_0 \end{bmatrix}$$

where H is the Hessian matrix:

$$H = \begin{bmatrix}
\frac{\partial^2 I}{\partial x^2} & \frac{\partial^2 I}{\partial x \partial y} & \frac{\partial^2 I}{\partial x \partial t} \\
\frac{\partial^2 I}{\partial y \partial x} & \frac{\partial^2 I}{\partial y^2} & \frac{\partial^2 I}{\partial y \partial t} \\
\frac{\partial^2 I}{\partial t \partial x} & \frac{\partial^2 I}{\partial t \partial y} & \frac{\partial^2 I}{\partial t^2}
\end{bmatrix}$$

## 3. Third-order Terms

For the third-order terms, we can use a 3D tensor contraction. Let's denote the third-order tensor of partial
derivatives as T. The third-order terms can be written as:

$$\frac{1}{6} \sum_{i,j,k} T_{ijk} (x_i - x_{0i})(x_j - x_{0j})(x_k - x_{0k})$$

where $x_1 = x$, $x_2 = y$, $x_3 = t$, and $T_{ijk} = \frac{\partial^3 I}{\partial x_i \partial x_j \partial x_k}$

## Complete Taylor Expansion

Putting it all together, the Taylor expansion up to the 3rd-order derivatives can be written as:

$$\begin{align*}
I(x,y,t) &= I(x_0, y_0, t_0) + \nabla I \cdot \begin{bmatrix} x - x_0 \\ y - y_0 \\ t - t_0 \end{bmatrix} \\
&+ \frac{1}{2} \begin{bmatrix} x - x_0 & y - y_0 & t - t_0 \end{bmatrix} H \begin{bmatrix} x - x_0 \\ y - y_0 \\ t - t_0 \end{bmatrix} \\
&+ \frac{1}{6} \sum_{i,j,k} T_{ijk} (x_i - x_{0i})(x_j - x_{0j})(x_k - x_{0k}) + R_4
\end{align*}$$

where $R_4$ is the remainder term (4th-order and higher terms).

This compact form using matrix notation efficiently represents the Taylor expansion up to the 3rd-order derivatives for
a function of three variables.