# Singular Value Decomposition (SVD) from First Principles

> This is a draft chapter explaining SVD from first principles.

## Goal

Given a matrix **A**, we want to understand exactly what it does to **every** vector.

Instead of memorizing

    A = U Σ Vᵀ

we will derive every piece.

---

## Step 1 — Why not use eigenvectors of A?

For a matrix A, an eigenvector satisfies

    Av = λv

This means the vector keeps its direction.

Unfortunately, many matrices do **not** have enough independent eigenvectors.

Example:

    A = [[1, 2],
         [0, 1]]

It has only one independent eigenvector, so eigenvalue decomposition fails.

---

## Step 2 — Construct AᵀA

Instead of studying A directly, build

    AᵀA

Why?

Because

    (AᵀA)ᵀ = AᵀA

Therefore AᵀA is always symmetric.

A real symmetric matrix always has:

- Real eigenvalues
- Enough eigenvectors to form a basis
- Orthogonal eigenvectors

Now we have a reliable starting point.

---

## Step 3 — Find the eigenvectors of AᵀA

Solve

    AᵀAv = λv

Call these vectors

    v₁, v₂, ..., vₙ

These become our **special input directions**.

Every vector x can be written as

    x = c₁v₁ + c₂v₂ + ... + cₙvₙ

So if we understand what A does to every vᵢ,
we understand what A does to every vector.

---

## Step 4 — Study Av

We care about A, so apply A to one special direction:

    Av

We don't know its direction or its length.

Let's compute the length.

For any vector x,

    ||x||² = xᵀx

Replace x with Av:

    ||Av||² = (Av)ᵀ(Av)

Use the transpose rule

    (AB)ᵀ = BᵀAᵀ

to obtain

    ||Av||² = vᵀAᵀAv

Now substitute

    AᵀAv = λv

giving

    ||Av||² = vᵀ(λv)
            = λ(vᵀv)

Normalize v so that

    vᵀv = 1

Therefore

    ||Av||² = λ

Take the square root

    ||Av|| = √λ

Define

    σ = √λ

This is the singular value.

---

## Step 5 — Find the output direction

We know the length of Av is σ.

To keep only the direction, normalize it:

    u = Av / σ

Multiply both sides by σ:

    Av = σu

So:

- v = special input direction
- σ = stretch amount
- u = special output direction

---

## Step 6 — Build the matrices

V is formed from all input directions:

    V = [v₁ v₂ ... vₙ]

Σ is the diagonal matrix of stretch amounts:

    Σ = diag(σ₁, σ₂, ..., σₙ)

U is formed from all output directions:

    U = [u₁ u₂ ... uₙ]

---

## Step 7 — Derive AV = UΣ

For every singular vector,

    Avᵢ = σᵢuᵢ

Stack the equations column by column:

    AV = UΣ

---

## Step 8 — Derive the final formula

Multiply both sides by V⁻¹:

    AVV⁻¹ = UΣV⁻¹

Since V is orthogonal,

    V⁻¹ = Vᵀ

Therefore

    A = UΣVᵀ

---

## What each matrix means

**V**

Changes the input into the special coordinate system.

**Σ**

Stretches each special direction independently.

**U**

Changes from the special output coordinates back to the standard basis.

---

## The full pipeline

Input vector x

↓

Vᵀ

Find coordinates in the special input basis.

↓

Σ

Stretch each coordinate independently.

↓

U

Convert back to the standard output basis.

↓

Final output Ax

---

This chapter is intended as the foundation for later topics including PCA, pseudoinverses, robotics Jacobians, and least-squares problems.
