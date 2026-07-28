# Singular Value Decomposition (SVD) — Explained

This repository presents a first-principles explanation of Singular Value Decomposition (SVD), with:

- a full conceptual derivation in [`MAIN.md`](./MAIN.md),
- and a comprehensive [Manim](https://www.manim.community/) animation script that walks through the entire story.

---

## What this project teaches

By the end, you should be able to explain:

1. Why eigenvalue decomposition is not enough for all matrices.
2. Why \(A^TA\) is the right object to study.
3. How symmetric-matrix properties guarantee orthonormal directions.
4. How singular values arise naturally as \(\sigma_i = \sqrt{\lambda_i}\).
5. How \(u_i = \frac{Av_i}{\sigma_i}\) defines output directions.
6. Why \(A = U\Sigma V^T\) is both algebraically correct and geometrically meaningful.
7. How to interpret SVD as: change basis \(\rightarrow\) stretch \(\rightarrow\) change basis.

---

## Repository structure

- [`MAIN.md`](./MAIN.md): full written derivation and intuition.
- [`svd_manim.py`](./svd_manim.py): complete Manim animation covering all major sections in `MAIN.md`.

---

## Manim animation coverage map

The animation is organized to mirror the markdown flow:

1. Goal of understanding matrix transformations
2. Why plain eigendecomposition fails
3. Constructing and motivating \(A^TA\)
4. Why symmetry matters (spectral theorem consequences)
5. Special input directions \(v_i\)
6. Why analyzing \(Av\) matters
7. Derivation of singular values
8. Derivation of \(u_i\)
9. Building \(V\), \(\Sigma\), \(U\)
10. Deriving \(AV = U\Sigma\)
11. Deriving \(A = U\Sigma V^T\)
12. Matrix-by-matrix meaning
13. Geometric pipeline interpretation
14. Rectangular matrix shape discussion
15. Applications and final intuition

---

## Setup

### 1) Prerequisites

- Python 3.10+
- FFmpeg installed and available in PATH
- A working LaTeX setup is recommended for best equation rendering

### 2) Install dependencies

```bash
pip install manim numpy
```

---

## Render the animation

From the repository root:

```bash
manim -pqh svd_manim.py SVDFromFirstPrinciples
```

Useful variants:

```bash
# Low-quality preview (faster)
manim -pql svd_manim.py SVDFromFirstPrinciples

# 1080p production render
manim -p -qh svd_manim.py SVDFromFirstPrinciples
```

---

## Learning workflow

Recommended order:

1. Read `MAIN.md` once quickly for the full narrative.
2. Watch the animation end-to-end.
3. Re-read `MAIN.md` slowly while pausing on each animation section.
4. Re-render and iterate on scenes if you want to adapt the explanation style.

---

## Customization ideas

- Split the single scene into multiple chapter scenes for lecture use.
- Add your own numerical matrix examples in the eigenvalue-failure section.
- Tune animation timings (`wait`, `run_time`) for classroom pacing.
- Export vertical format for short-form educational clips.

---

## Why SVD matters

SVD is foundational in:

- PCA and dimensionality reduction
- Data and image compression
- Denoising
- Least-squares optimization
- Recommender systems
- Computer vision and robotics
- Modern machine learning pipelines

---

## License / usage

Use and modify this material for study, teaching, and experimentation.
If you publish derivative educational content, attribution to this repository is appreciated.
