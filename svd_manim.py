from manim import *
import numpy as np


class SVDFromFirstPrinciples(Scene):
    def construct(self):
        self.camera.background_color = "#0E1116"
        self.show_title()
        self.goal_section()
        self.eigen_failure_section()
        self.ata_section()
        self.symmetric_section()
        self.special_directions_section()
        self.why_av_section()
        self.singular_values_section()
        self.u_derivation_section()
        self.build_matrices_section()
        self.av_equals_usigma_section()
        self.full_svd_section()
        self.meaning_section()
        self.pipeline_section()
        self.rectangular_section()
        self.applications_section()
        self.final_intuition_section()

    def chapter(self, title, subtitle=None):
        header = Text(title, font_size=40, weight=BOLD)
        if subtitle:
            sub = Text(subtitle, font_size=24, color=GRAY_B).next_to(header, DOWN, buff=0.3)
            grp = VGroup(header, sub).to_edge(UP)
        else:
            grp = VGroup(header).to_edge(UP)
        self.play(FadeIn(grp, shift=UP), run_time=0.8)
        return grp

    def clear_stage(self, keep=None):
        keep = keep or []
        keep_set = set(keep)
        removable = [m for m in self.mobjects if m not in keep_set]
        if removable:
            self.play(*[FadeOut(m) for m in removable], run_time=0.6)

    def show_title(self):
        title = Text("Singular Value Decomposition", font_size=56, weight=BOLD)
        subtitle = Text("From First Principles", font_size=34, color=BLUE_C)
        grp = VGroup(title, subtitle).arrange(DOWN, buff=0.25)
        self.play(Write(title), FadeIn(subtitle, shift=UP), run_time=1.6)
        self.wait(0.5)
        self.play(grp.animate.scale(0.72).to_edge(UP), run_time=0.8)
        self.wait(0.3)

    def goal_section(self):
        self.clear_stage()
        header = self.chapter("1) The Goal", "Understand what a matrix transformation is really doing")
        x_vec = MathTex(r"\mathbf{x}", color=BLUE_C).move_to(LEFT * 3 + DOWN * 1.3)
        ax_vec = MathTex(r"A\mathbf{x}", color=GREEN_C).move_to(RIGHT * 3 + DOWN * 1.3)
        arrow = Arrow(LEFT * 2.2 + DOWN * 1.3, RIGHT * 2.2 + DOWN * 1.3, buff=0.2, color=YELLOW_C)
        question = Text("Which directions are special, how much are they stretched, and where do they go?", font_size=24)
        question.next_to(arrow, DOWN, buff=0.8)
        self.play(FadeIn(x_vec), GrowArrow(arrow), FadeIn(ax_vec), run_time=1.2)
        self.play(FadeIn(question, shift=UP), run_time=1.0)
        self.wait(0.8)
        self.clear_stage([header])
        self.play(FadeOut(header), run_time=0.4)

    def eigen_failure_section(self):
        self.clear_stage()
        header = self.chapter("2) Why Eigenvalue Decomposition Fails")
        eq = MathTex(r"A\mathbf{v}=\lambda\mathbf{v}").scale(1.1).shift(UP * 1.2)
        matrix = MathTex(
            r"A=\begin{bmatrix}1&2\\0&1\end{bmatrix}",
            r"\quad\Rightarrow\quad",
            r"\text{only one independent eigenvector}",
        ).arrange(RIGHT).shift(DOWN * 0.3)
        fail = Text("Not enough eigenvectors to form a basis in 2D.", font_size=26, color=RED_C).to_edge(DOWN)
        self.play(Write(eq), run_time=0.9)
        self.play(Write(matrix), run_time=1.3)
        self.play(FadeIn(fail, shift=UP), run_time=0.8)
        self.wait(0.8)
        self.clear_stage([header])
        self.play(FadeOut(header), run_time=0.4)

    def ata_section(self):
        self.clear_stage()
        header = self.chapter("3) Construct $A^TA$", "Turn any real matrix into a symmetric one")
        eq1 = MathTex(r"(A^TA)^T=A^TA").scale(1.2)
        eq2 = Text("So $A^TA$ is always symmetric.", font_size=28, color=GREEN_C).next_to(eq1, DOWN, buff=0.7)
        self.play(Write(eq1), run_time=1.0)
        self.play(FadeIn(eq2, shift=UP), run_time=0.9)
        self.wait(0.8)
        self.clear_stage([header])
        self.play(FadeOut(header), run_time=0.4)

    def symmetric_section(self):
        self.clear_stage()
        header = self.chapter("4) Why Symmetric Matrices Are Special")
        p1 = Text("1. Real eigenvalues", font_size=30)
        p2 = Text("2. Enough eigenvectors for a basis", font_size=30)
        p3 = Text("3. Distinct-eigenvalue eigenvectors are orthogonal", font_size=30)
        props = VGroup(p1, p2, p3).arrange(DOWN, aligned_edge=LEFT, buff=0.45).shift(DOWN * 0.3)
        ortho = MathTex(
            r"v_i^Tv_j=\begin{cases}1,&i=j\\0,&i\ne j\end{cases}"
        ).scale(0.95).to_edge(DOWN)
        self.play(LaggedStart(*[FadeIn(p, shift=RIGHT) for p in props], lag_ratio=0.25), run_time=1.5)
        self.play(Write(ortho), run_time=1.0)
        self.wait(0.8)
        self.clear_stage([header])
        self.play(FadeOut(header), run_time=0.4)

    def special_directions_section(self):
        self.clear_stage()
        header = self.chapter("5) The Special Input Directions")
        eig_eq = MathTex(r"A^TA\mathbf{v}_i=\lambda_i\mathbf{v}_i").shift(UP * 1.2)
        basis_eq = MathTex(r"\mathbf{x}=c_1\mathbf{v}_1+c_2\mathbf{v}_2+\cdots+c_n\mathbf{v}_n").shift(DOWN * 0.1)
        note = Text("Understand $A$ by understanding what it does to each $v_i$.", font_size=26, color=BLUE_B).to_edge(DOWN)
        self.play(Write(eig_eq), run_time=0.9)
        self.play(Write(basis_eq), run_time=1.1)
        self.play(FadeIn(note, shift=UP), run_time=0.8)
        self.wait(0.8)
        self.clear_stage([header])
        self.play(FadeOut(header), run_time=0.4)

    def why_av_section(self):
        self.clear_stage()
        header = self.chapter("6) Why Study $A\\mathbf{v}$")
        q = Text("We care about A itself, so we track what A does to each special direction.", font_size=28)
        av = MathTex(r"A\mathbf{v}_i").scale(1.4).set_color(YELLOW_C).shift(DOWN * 0.8)
        self.play(FadeIn(q, shift=UP), run_time=1.0)
        self.play(Write(av), run_time=0.9)
        self.wait(0.7)
        self.clear_stage([header])
        self.play(FadeOut(header), run_time=0.4)

    def singular_values_section(self):
        self.clear_stage()
        header = self.chapter("7) Deriving Singular Values")
        steps = VGroup(
            MathTex(r"\|A\mathbf{v}\|^2=(A\mathbf{v})^T(A\mathbf{v})"),
            MathTex(r"= \mathbf{v}^TA^TA\mathbf{v}"),
            MathTex(r"= \mathbf{v}^T(\lambda \mathbf{v})"),
            MathTex(r"= \lambda(\mathbf{v}^T\mathbf{v})"),
            MathTex(r"= \lambda"),
            MathTex(r"\|A\mathbf{v}\|=\sqrt{\lambda}\equiv \sigma"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25).scale(0.88).shift(DOWN * 0.25)
        box = SurroundingRectangle(steps[-1], color=GREEN_C, buff=0.15)
        for row in steps:
            self.play(Write(row), run_time=0.5)
        self.play(Create(box), run_time=0.6)
        self.wait(0.8)
        self.clear_stage([header])
        self.play(FadeOut(header), run_time=0.4)

    def u_derivation_section(self):
        self.clear_stage()
        header = self.chapter("8) Deriving $\\mathbf{u}_i$")
        eq1 = MathTex(r"\mathbf{u}_i=\frac{A\mathbf{v}_i}{\sigma_i}").scale(1.15).shift(UP * 0.6)
        eq2 = MathTex(r"A\mathbf{v}_i=\sigma_i\mathbf{u}_i").scale(1.15).shift(DOWN * 0.7)
        txt = Text("Normalize $A v_i$ to isolate direction.", font_size=27, color=BLUE_B).to_edge(DOWN)
        self.play(Write(eq1), run_time=1.0)
        self.play(TransformFromCopy(eq1, eq2), run_time=1.0)
        self.play(FadeIn(txt, shift=UP), run_time=0.7)
        self.wait(0.8)
        self.clear_stage([header])
        self.play(FadeOut(header), run_time=0.4)

    def build_matrices_section(self):
        self.clear_stage()
        header = self.chapter("9-11) Build $V$, $\\Sigma$, $U$")
        vmat = MathTex(r"V=[\mathbf{v}_1\ \mathbf{v}_2\ \cdots\ \mathbf{v}_n]").to_edge(LEFT).shift(RIGHT * 0.9 + DOWN * 0.4)
        smat = MathTex(
            r"\Sigma=\mathrm{diag}(\sigma_1,\sigma_2,\ldots,\sigma_r)"
        ).shift(DOWN * 0.4)
        umat = MathTex(r"U=[\mathbf{u}_1\ \mathbf{u}_2\ \cdots\ \mathbf{u}_m]").to_edge(RIGHT).shift(LEFT * 0.8 + DOWN * 0.4)
        labels = VGroup(
            Text("input directions", font_size=21, color=BLUE_B).next_to(vmat, DOWN),
            Text("stretch factors", font_size=21, color=YELLOW_B).next_to(smat, DOWN),
            Text("output directions", font_size=21, color=GREEN_B).next_to(umat, DOWN),
        )
        self.play(FadeIn(vmat, shift=UP), FadeIn(smat, shift=UP), FadeIn(umat, shift=UP), run_time=1.2)
        self.play(LaggedStart(*[FadeIn(lbl) for lbl in labels], lag_ratio=0.2), run_time=0.9)
        self.wait(0.8)
        self.clear_stage([header])
        self.play(FadeOut(header), run_time=0.4)

    def av_equals_usigma_section(self):
        self.clear_stage()
        header = self.chapter("12) Derive $AV = U\\Sigma$")
        eq1 = MathTex(r"A\mathbf{v}_i=\sigma_i\mathbf{u}_i").shift(UP * 1.2)
        eq2 = MathTex(r"AV=[A\mathbf{v}_1\ A\mathbf{v}_2\ \cdots]").shift(DOWN * 0.2)
        eq3 = MathTex(r"U\Sigma=[\sigma_1\mathbf{u}_1\ \sigma_2\mathbf{u}_2\ \cdots]").shift(DOWN * 1.3)
        final = MathTex(r"AV=U\Sigma", color=GREEN_C).scale(1.3).to_edge(DOWN)
        self.play(Write(eq1), run_time=0.8)
        self.play(Write(eq2), run_time=0.8)
        self.play(Write(eq3), run_time=0.8)
        self.play(Write(final), run_time=0.8)
        self.wait(0.8)
        self.clear_stage([header])
        self.play(FadeOut(header), run_time=0.4)

    def full_svd_section(self):
        self.clear_stage()
        header = self.chapter("13) Derive the SVD Formula")
        deriv = VGroup(
            MathTex(r"AV=U\Sigma"),
            MathTex(r"AVV^{-1}=U\Sigma V^{-1}"),
            MathTex(r"V^{-1}=V^T \quad (\text{orthogonal }V)"),
            MathTex(r"\boxed{A=U\Sigma V^T}", color=YELLOW_C),
        ).arrange(DOWN, buff=0.32).shift(DOWN * 0.25)
        for item in deriv:
            self.play(Write(item), run_time=0.65)
        self.wait(1.0)
        self.clear_stage([header])
        self.play(FadeOut(header), run_time=0.4)

    def meaning_section(self):
        self.clear_stage()
        header = self.chapter("14-15) What Each Matrix Means")
        v_text = Text("V: special input coordinate system", font_size=28, color=BLUE_B)
        s_text = Text("Σ: independent stretching (no mixing)", font_size=28, color=YELLOW_B)
        u_text = Text("U: special output coordinate system", font_size=28, color=GREEN_B)
        vt_text = Text("Vᵀ converts x into singular-vector coordinates", font_size=26, color=GRAY_B)
        items = VGroup(v_text, s_text, u_text, vt_text).arrange(DOWN, aligned_edge=LEFT, buff=0.45).shift(DOWN * 0.25)
        self.play(LaggedStart(*[FadeIn(it, shift=RIGHT) for it in items], lag_ratio=0.2), run_time=1.4)
        self.wait(0.8)
        self.clear_stage([header])
        self.play(FadeOut(header), run_time=0.4)

    def pipeline_section(self):
        self.clear_stage()
        header = self.chapter("16) Complete Pipeline")
        steps = [
            ("Input vector x", BLUE_C),
            ("Vᵀ: project into special input basis", BLUE_B),
            ("Σ: stretch each coordinate by σᵢ", YELLOW_B),
            ("U: map to output basis", GREEN_B),
            ("Final output Ax", GREEN_C),
        ]
        boxes = VGroup()
        for label, color in steps:
            box = RoundedRectangle(width=7.5, height=0.8, corner_radius=0.15, color=color)
            txt = Text(label, font_size=24).move_to(box.get_center())
            boxes.add(VGroup(box, txt))
        boxes.arrange(DOWN, buff=0.25).shift(DOWN * 0.2)
        arrows = VGroup(
            *[Arrow(boxes[i].get_bottom(), boxes[i + 1].get_top(), buff=0.06, stroke_width=4) for i in range(len(boxes) - 1)]
        )
        self.play(LaggedStart(*[FadeIn(b, shift=UP) for b in boxes], lag_ratio=0.17), run_time=1.3)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.15), run_time=1.0)
        self.wait(0.8)
        self.clear_stage([header])
        self.play(FadeOut(header), run_time=0.4)

    def rectangular_section(self):
        self.clear_stage()
        header = self.chapter("17) Rectangular Matrices")
        dims = VGroup(
            MathTex(r"A\in\mathbb{R}^{m\times n}"),
            MathTex(r"U\in\mathbb{R}^{m\times m}"),
            MathTex(r"\Sigma\in\mathbb{R}^{m\times n}"),
            MathTex(r"V\in\mathbb{R}^{n\times n}"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).shift(LEFT * 2.0 + DOWN * 0.3)
        notes = VGroup(
            Text("m < n: dimensionality can reduce", font_size=24, color=BLUE_B),
            Text("m > n: input can embed into higher output dimension", font_size=24, color=GREEN_B),
            Text("Shape change is controlled by Σ", font_size=24, color=YELLOW_B),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35).shift(RIGHT * 2.2 + DOWN * 0.3)
        self.play(FadeIn(dims, shift=RIGHT), run_time=1.0)
        self.play(FadeIn(notes, shift=LEFT), run_time=1.0)
        self.wait(0.8)
        self.clear_stage([header])
        self.play(FadeOut(header), run_time=0.4)

    def applications_section(self):
        self.clear_stage()
        header = self.chapter("18) Why SVD Is Useful")
        apps = [
            "PCA",
            "Data and image compression",
            "Noise reduction",
            "Least-squares fitting",
            "Robotics and Jacobian analysis",
            "Computer vision",
            "Recommender systems",
            "Latent semantic analysis",
            "Control theory",
            "Machine learning",
        ]
        bullets = VGroup(*[Text(f"• {app}", font_size=25) for app in apps]).arrange(
            DOWN, aligned_edge=LEFT, buff=0.2
        ).shift(DOWN * 0.2)
        self.play(LaggedStart(*[FadeIn(b, shift=RIGHT) for b in bullets], lag_ratio=0.09), run_time=1.7)
        self.wait(0.8)
        self.clear_stage([header])
        self.play(FadeOut(header), run_time=0.4)

    def final_intuition_section(self):
        self.clear_stage()
        header = self.chapter("Final Intuition")
        formula = MathTex(r"A=U\Sigma V^T", color=YELLOW_C).scale(1.5).shift(UP * 1.2)
        line1 = Text("1) Change to the best input basis", font_size=28, color=BLUE_B)
        line2 = Text("2) Stretch independently along special directions", font_size=28, color=YELLOW_B)
        line3 = Text("3) Change to the output basis", font_size=28, color=GREEN_B)
        lines = VGroup(line1, line2, line3).arrange(DOWN, aligned_edge=LEFT, buff=0.35).shift(DOWN * 0.6)
        close = Text(
            "SVD reveals the simplest coordinate systems for any linear transformation.",
            font_size=26,
            color=GRAY_B,
        ).to_edge(DOWN)
        self.play(Write(formula), run_time=0.9)
        self.play(LaggedStart(*[FadeIn(l, shift=RIGHT) for l in lines], lag_ratio=0.2), run_time=1.3)
        self.play(FadeIn(close, shift=UP), run_time=0.8)
        self.wait(1.5)
        self.play(FadeOut(VGroup(header, formula, lines, close)), run_time=0.8)
