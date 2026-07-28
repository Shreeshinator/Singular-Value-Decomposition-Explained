# Singular Value Decomposition (SVD) — From First Principles

> **Goal:** Understand *why* SVD works, not just how to compute it.

---

# Table of Contents

1. What is the goal?
2. Why eigenvalue decomposition fails
3. Constructing (A^TA)
4. Why symmetric matrices are special
5. Finding the special input directions
6. Why we study (Av)
7. Deriving the singular values
8. Deriving the matrix (U)
9. Constructing (V,\Sigma,U)
10. Deriving (A=U\Sigma V^T)
11. What each matrix really means
12. Geometric interpretation
13. Rectangular matrices
14. Why SVD is useful
15. Final intuition

---

# 1. The Goal

A matrix is a function.

It takes an input vector

[
x
]

and produces

[
Ax.
]

The question is

> **Can we completely understand what this transformation is doing?**

Instead of looking at a table of numbers, we'd like to answer:

* Which directions are special?
* How much are they stretched?
* Where do they end up?

SVD answers exactly those questions.

---

# 2. Why Eigenvalue Decomposition Fails

The first idea is

> Find eigenvectors of (A).

An eigenvector satisfies

[
Av=\lambda v.
]

Meaning:

The vector keeps its direction and is only stretched.

Unfortunately...

Not every matrix has enough eigenvectors.

Example

[
A=
\begin{bmatrix}
1&2\
0&1
\end{bmatrix}
]

It has only one independent eigenvector.

Since we cannot build a basis from one vector in 2D,

eigenvalue decomposition fails.

We need another idea.

---

# 3. Construct (A^TA)

Instead of studying

[
A,
]

we construct

[
A^TA.
]

Question:

**Why?**

Because

[
(A^TA)^T
========

# A^T(A^T)^T

A^TA.
]

Therefore

[
A^TA
]

is always symmetric.

This is true for every real matrix.

---

# 4. Why Symmetric Matrices Are Special

Every real symmetric matrix satisfies the Spectral Theorem.

This gives three extremely important properties.

## Property 1

Every eigenvalue is real.

No complex numbers are required.

---

## Property 2

There are enough eigenvectors to form a basis.

Unlike general matrices.

---

## Property 3

Eigenvectors corresponding to different eigenvalues are orthogonal.

Therefore we can normalize them.

After normalization

[
v_i^Tv_j=
\begin{cases}
1&i=j\
0&i\ne j
\end{cases}
]

This means they form an orthonormal basis.

---

# 5. The Special Input Directions

Suppose

[
A^TAv=\lambda v.
]

This is just the eigenvalue equation.

The vectors

[
v_1,v_2,\ldots
]

are not chosen randomly.

They become the "special input directions."

Since they form a basis,

every input vector can be written as

[
x=c_1v_1+c_2v_2+\cdots+c_nv_n.
]

Already this is powerful.

Instead of studying every possible vector,

we only need to understand what happens to each (v_i).

---

# 6. Why Study (Av)?

Remember

(A) is the transformation we actually care about.

So naturally we ask

> What happens if we apply (A) to one of these special directions?

Compute

[
Av.
]

We don't know its direction.

We don't know its length.

Let's begin with the length.

---

# 7. Deriving the Singular Values

We know

[
|x|^2=x^Tx.
]

Replace

[
x
]

by

[
Av.
]

Then

[
|Av|^2=(Av)^T(Av).
]

Use the transpose rule

[
(AB)^T=B^TA^T.
]

Therefore

[
(Av)^T=v^TA^T.
]

Substitute

[
|Av|^2=v^TA^TAv.
]

Now use the eigenvalue equation

[
A^TAv=\lambda v.
]

Substitute again

[
|Av|^2
======

v^T(\lambda v).
]

Since

[
\lambda
]

is just a scalar,

# [

\lambda(v^Tv).
]

Normalize the eigenvector

[
|v|=1.
]

Therefore

[
v^Tv=1.
]

So

[
\boxed{|Av|^2=\lambda}
]

Take the square root

[
\boxed{|Av|=\sqrt{\lambda}}
]

This quantity appears naturally.

We give it a name.

[
\boxed{\sigma=\sqrt{\lambda}}
]

This is the singular value.

Notice

We did **not** invent this definition.

The algebra forced it.

---

# 8. Deriving U

We now know

* the direction of (Av) is unknown,
* its length is

[
\sigma.
]

How do we isolate only the direction?

Normalize it.

Define

[
\boxed{
u=\frac{Av}{\sigma}
}
]

This is simply the unit vector pointing in the direction of (Av).

Multiply both sides by

[
\sigma
]

to obtain

[
\boxed{
Av=\sigma u
}
]

Again,

this was not assumed.

It follows directly from normalization.

---

# 9. Constructing V

Collect all input directions.

[
V=
\begin{bmatrix}
|&|&&|\
v_1&v_2&\cdots&v_n\
|&|&&|
\end{bmatrix}
]

Columns of (V)

=

special input directions.

---

# 10. Constructing Σ

Collect every singular value.

[
\Sigma=
\begin{bmatrix}
\sigma_1&&\
&\sigma_2&\
&&\ddots
\end{bmatrix}
]

It simply stores stretch factors.

Nothing else.

---

# 11. Constructing U

Collect every output direction.

[
U=
\begin{bmatrix}
|&|&&|\
u_1&u_2&\cdots&u_n\
|&|&&|
\end{bmatrix}
]

Columns of (U)

=

special output directions.

---

# 12. Deriving (AV=U\Sigma)

For every singular vector,

[
Av_i=\sigma_i u_i.
]

Write all equations together.

Left side

[
AV
==

\begin{bmatrix}
Av_1&Av_2&\cdots
\end{bmatrix}
]

Right side

Multiplying by

[
\Sigma
]

scales each column of

[
U
]

independently.

Therefore

[
U\Sigma
=======

\begin{bmatrix}
\sigma_1u_1&
\sigma_2u_2&
\cdots
\end{bmatrix}
]

Both matrices have identical columns.

Hence

[
\boxed{AV=U\Sigma}
]

---

# 13. Deriving the SVD Formula

Multiply both sides on the right by

[
V^{-1}.
]

Since

[
V
]

is orthogonal,

[
V^{-1}=V^T.
]

Therefore

[
\boxed{
A=U\Sigma V^T
}
]

The derivation is complete.

---

# 14. What Does Each Matrix Mean?

## V

The special input coordinate system.

Every input vector is first expressed in this basis.

---

## Σ

Independent stretching.

Each coordinate is multiplied by its own singular value.

No mixing occurs.

---

## U

The special output coordinate system.

After stretching,

the result is expressed in the output basis.

---

# 15. What Does (V^T) Actually Do?

Suppose

[
x
]

is any vector.

Because

[
V
]

is orthonormal,

[
V^Tx
====

\begin{bmatrix}
v_1^Tx\
v_2^Tx\
\vdots
\end{bmatrix}
]

Each entry is the projection of

[
x
]

onto one singular vector.

Therefore

[
V^T
]

converts standard coordinates into coordinates in the singular-vector basis.

It does **not** lose information.

It only changes coordinates.

---

# 16. The Complete Pipeline

Read

[
A=U\Sigma V^T
]

from right to left.

```
Input vector

↓

Vᵀ

Find coordinates in the special input basis.

↓

Σ

Stretch each coordinate independently.

↓

U

Build the output vector in the special output basis.

↓

Final output
```

---

# 17. Rectangular Matrices

If

[
A
]

is

[
m\times n,
]

then

[
U:m\times m
]

[
\Sigma:m\times n
]

[
V:n\times n
]

If

[
m<n,
]

dimensions are reduced.

If

[
m>n,
]

the input is embedded into a higher-dimensional output space.

The dimension change happens because of the shape of

[
\Sigma,
]

not because of

[
U
]

or

[
V.
]

---

# 18. Why Is SVD So Useful?

SVD is used because it finds the coordinate systems where a complicated linear transformation becomes nothing more than independent stretching.

Applications include:

* Principal Component Analysis (PCA)
* Data compression
* Image compression
* Noise reduction
* Least-squares problems
* Robotics (Jacobian analysis and manipulability)
* Computer vision
* Recommender systems
* Latent Semantic Analysis (LSA)
* Control theory
* Machine learning

---

# Final Intuition

SVD says:

> Every linear transformation can be understood as three simpler transformations.

1. Rotate/change to the best input basis.
2. Stretch independently along each special direction.
3. Rotate/change into the output basis.

Or, in one sentence:

**SVD discovers the input directions that behave most simply under a linear transformation, tells you exactly how much each is stretched, and tells you where each one ends up.**
