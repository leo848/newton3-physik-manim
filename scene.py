from manim import *


class Newton3(Scene):
    def show_title(self):
        title = Tex("Newton 3 - Das Wechselwirkungsprinzip")

        self.play(Write(title))
        self.wait()

        desc = Tex(
            "In den folgenden Simulationen wird Reibung vernachlässigt.", width=200
        )
        self.play(ReplacementTransform(title, desc))
        self.wait(2)

        self.ground = (
            Rectangle(color="gray", fill_opacity=0.8, width=15, height=1)
            .align_on_border(DOWN)
            .shift(DOWN)
        )
        self.play(ReplacementTransform(desc, self.ground))

    def play_sim_1(self):
        simtext = Tex("Simulation 1", width=150)

        self.play(Write(simtext))
        self.play(simtext.animate.scale(0.5).to_edge(UL))

        sq1 = Square(color="green", fill_opacity=0.5)
        sq2 = Square(color="red", fill_opacity=0.5)

        self.play(Create(sq1))
        self.play(
            sq1.animate.scale(0.5).next_to(self.ground, UP, buff=-0.05).shift(RIGHT * 3)
        )

        self.play(Create(sq2))
        self.play(
            sq2.animate.scale(0.5).next_to(self.ground, UP, buff=-0.05).shift(LEFT * 3)
        )

        self.wait()

        arrow = Arrow(sq1.get_center() + RIGHT / 4, sq1.get_center() + LEFT * 2)

        self.play(sq1.animate.add(arrow))
        self.play(sq1.animate(rate_func=linear, run_time=2.5).shift(LEFT * 5))

        sq1.submobjects = []

        sq2.add(Arrow(sq2.get_center() + RIGHT / 4, sq2.get_center() + LEFT * 2))
        self.play(sq2.animate(rate_func=linear, run_time=2.5).shift(LEFT * 5))

        self.play(Uncreate(sq1), Uncreate(sq2))

        self.play(Uncreate(simtext))

    def play_sim_2(self):
        simtext = Tex("Simulation 2", width=150)
        self.play(Write(simtext))
        self.play(simtext.animate.scale(0.5).to_edge(UL))

        c1 = Circle(color="red", fill_opacity=0.5)
        c2 = Circle(color="green", fill_opacity=0.5)

        self.play(Create(c1))
        self.play(c1.animate.shift(LEFT * 4))

        self.play(Create(c2))
        self.play(c2.animate.shift(RIGHT * 4))

        arrow1 = Arrow(c1.get_center() + LEFT / 4, c1.get_center() + RIGHT * 3)
        a1text = MathTex(r"\overrightarrow{F_A}")

        arrow2 = Arrow(c2.get_center() + RIGHT / 4, c2.get_center() + LEFT * 3)
        a2text = MathTex(r"\overrightarrow{F_B}")

        self.play(
            c1.animate.add(arrow1), Write(a1text), a1text.animate.next_to(arrow1, UP)
        )

        self.play(
            c2.animate.add(arrow2), Write(a2text), a2text.animate.next_to(arrow2, UP)
        )
        self.wait()

        ueqt = MathTex(r"=\;-")
        self.play(Write(ueqt), ueqt.animate.shift(UP * 0.75))
        self.wait()

        self.play(
            c1.animate(run_time=3, rate_func=linear).shift(RIGHT),
            c2.animate(run_time=3, rate_func=linear).shift(LEFT),
        )

        self.play(Uncreate(simtext))
        self.play(
            Uncreate(c1),
            Uncreate(c2),
            Uncreate(a1text),
            Uncreate(a2text),
            Uncreate(ueqt),
        )

    def play_sim_3(self):
        self.play(Create(self.ground))

        simtext = Tex("Simulation 3", width=150)
        self.play(Write(simtext))
        self.play(simtext.animate.scale(0.5).to_edge(UL))

        c1 = Circle(color="red", fill_opacity=0.5).scale(0.2).shift(DOWN)
        wall1 = Rectangle(color="blue", fill_opacity=0.5, width=1, height=6)

        self.play(Create(wall1))
        self.wait()
        self.play(wall1.animate.to_edge(DL, buff=0.75))

        self.play(Create(c1))

        wall1_mass = Tex("m = 1kg").to_edge(DL, buff=0.75)
        c1_mass = Tex("m = 1kg").shift(DOWN)

        self.play(Create(wall1_mass), Create(c1_mass))
        self.wait(1.5)
        self.play(Uncreate(wall1_mass), Uncreate(c1_mass))

        self.play(c1.animate.to_edge(DR, buff=0.75))

        self.play(c1.animate(rate_func=linear, run_time=4).shift(LEFT * 11.5))
        self.play(
            wall1.animate(rate_func=linear, run_time=0.0625).shift(UP * 0.125),
            c1.animate(run_time=0.0625, rate_func=linear).shift(LEFT * 0.0625 / 2),
        )
        self.play(
            Rotate(
                wall1,
                angle=-PI / 2,
                rate_func=rate_functions.ease_in_quart,
                run_time=2,
                about_point=c1.get_center() + UP / 8,
            ),
            c1.animate(rate_func=linear, run_time=2).shift(LEFT),
        )

        self.play(
            wall1.animate(rate_func=linear, run_time=0.0625).shift(DOWN * 0.125),
            c1.animate(run_time=0.0625, rate_func=linear).shift(LEFT * 0.0625 / 2),
        )
        self.wait()

        self.play(Uncreate(wall1), Uncreate(c1))

        if True:
            c2 = Circle(color="red", fill_opacity=0.5).scale(0.2).shift(DOWN)
            wall2 = Rectangle(color="yellow", fill_opacity=0.5, width=1, height=6)

            self.play(Create(wall2))
            self.wait()
            self.play(wall2.animate.to_edge(DL, buff=0.75))

            self.play(Create(c2))

            wall2_mass = Tex("m = 10kg").to_edge(DL, buff=0.75)
            c2_mass = Tex("m = 1kg").shift(DOWN)

            self.play(Create(wall2_mass), Create(c2_mass))
            self.wait(1.5)
            self.play(Uncreate(wall2_mass), Uncreate(c2_mass))

            self.play(c2.animate.to_edge(DR, buff=0.75))

            self.play(c2.animate(rate_func=linear, run_time=4).shift(LEFT * 11.5))

            self.play(
                wall2.animate(run_time=4, rate_func=linear).shift(LEFT),
                c2.animate(run_time=4, rate_func=linear).shift(RIGHT * 5.5),
            )

            self.play(Uncreate(c2), Uncreate(wall2), Uncreate(self.ground))

        if True:
            c3 = Circle(color="red", fill_opacity=0.5).scale(0.2).shift(DOWN)
            wall3 = Rectangle(color="brown", fill_opacity=0.5, width=1, height=6)

            self.play(Create(wall3))
            self.wait()
            self.play(wall3.animate.to_edge(DL, buff=0.75))

            self.play(Create(c3))

            wall3_mass = Tex("m > 1t").to_edge(DL, buff=0.75)
            c3_mass = Tex("m = 1kg").shift(DOWN)

            self.play(Create(wall3_mass), Create(c3_mass))
            self.wait(1.5)
            self.play(Uncreate(wall3_mass), Uncreate(c3_mass))

            self.play(c3.animate.to_edge(DR, buff=0.75))

            self.play(c3.animate(rate_func=linear, run_time=4).shift(LEFT * 11.5))

            self.play(
                c3.animate(run_time=4, rate_func=linear).shift(RIGHT * 11),
            )

            self.play(Uncreate(c3), Uncreate(wall3))

            self.play(Uncreate(simtext))

    def show_intermediate_texts(self, *strings, **kwargs):
        if kwargs.get("tex"):
            texts = [
                Tex(value) if type(value) == str else Tex(value[0])
                for (index, value) in enumerate(strings)
            ]
        else:
            texts = [
                Tex(value[0], width=value[1] * 100 if len(value) > 1 else 250)
                for (index, value) in enumerate(strings)
            ]

        for index, text, *rest in enumerate(texts):
            if index == 0:
                self.play(Write(text))
            else:
                if kwargs.get("transform") == "matching":
                    self.play(TransformMatchingShapes(texts[index - 1], text))
                else:
                    self.play(ReplacementTransform(texts[index - 1], text))
            self.wait(1.5)
            if index == len(strings) - 1 or len(rest) > 0 and rest[0] == -1:
                self.play(Uncreate(text))

    def construct(self):
        self.show_title()
        self.play_sim_1()
        self.show_intermediate_texts(
            ("Wie gerade beobachtet, ändert sich die Geschwindigkeit nicht.",),
            (
                "Dies wird durch Newtons 3. Gesetz beschrieben:\nactio gegengleich reactio",
                2.5,
                -1,
            ),
        )

        self.show_intermediate_texts(
            (
                r"actio ist hierbei die einwirkende Kraft $\overrightarrow{F_A}$,\newline reactio die Gegenkraft $\overrightarrow{F_B}.$",
                2,
            ),
            (r"Somit gilt: $\overrightarrow{F_A} = -\overrightarrow{F_B}$", 1.4),
            transform="matching",
        )

        self.play(Uncreate(self.ground))

        self.show_intermediate_texts(
            (
                r"Hier wird einmal das Prinzip\newline anhand von zwei Objekten,\newline A und B, visualisiert.",
            )
        )
        self.wait()
        self.play_sim_2()
        self.wait()

        self.show_intermediate_texts(
            (
                r"Aber sollte das nicht bedeuten, dass\newline sich beispielweise durch den Aufprall eines\newline Balls auf einer Wand sich auch diese bewegen sollte?",
                2,
            ),
            (r"Dieses Experiment wird jetzt einmal simuliert.", 2),
        )

        self.wait()
        self.play_sim_3()

        deft = Tex("Newtons Definition von Kraft:")
        fma = Tex("F = ma", width=100)
        fma1 = MathTex(r"\overrightarrow{F} = m \overrightarrow{a}", width=100)

        amf = MathTex(r"\overrightarrow{a} = \frac{\overrightarrow{F}}{m}", width=100)

        self.play(Write(deft))
        self.wait()
        self.play(TransformMatchingTex(deft, fma))
        self.wait()
        self.play(ReplacementTransform(fma, fma1))
        self.wait()
        self.play(TransformMatchingShapes(fma1, amf))

        self.wait()

        self.play(Unwrite(amf))

        manim = Tex(
            r"Dieses Video wurde mit der\newline Manim-Animationslibrary für Python erstellt."
        )
        qtext = Tex(r"Quellen:")

        quellen = [
            ("LeifiPhysik", r"https://leifiphysik.de/mechanik"),
            ("Wikipedia", r"https://wikipedia.de/wiki/Newtonsche\_Gesetze"),
            (
                "Studyflix",
                r"https://studyflix.de/ingenieurwissenschaften/newtonsche-axiome-1432",
            ),
        ]

        dank = Tex(r"Vielen Dank fürs Zuschauen!")

        self.play(Write(manim, run_time=6))
        self.play(ReplacementTransform(manim, qtext, run_time=4))

        self.wait()
        self.play(Unwrite(qtext))

        things = [(title + "\\newline " + basel,) for title, basel in quellen]
        print(things)

        self.show_intermediate_texts(*things)

        self.play(Write(dank, run_time=6))

        self.wait(2)

        self.play(FadeOut(dank, run_time=10))
