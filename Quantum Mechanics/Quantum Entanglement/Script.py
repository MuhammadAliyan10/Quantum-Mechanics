from manim import *

class QuantumEntanglement(Scene):
    def construct(self):

        title = Text("Quantum Entanglement", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        particle1 = Circle(radius=0.5, color=BLUE).shift(LEFT * 3)
        particle2 = Circle(radius=0.5, color=RED).shift(RIGHT * 3)
        label1 = Text("Particle A", font_size=24).next_to(particle1, DOWN)
        label2 = Text("Particle B", font_size=24).next_to(particle2, DOWN)

        self.play(Create(particle1), Create(particle2))
        self.play(Write(label1), Write(label2))
        self.wait(1)
        connection = Line(particle1.get_right(), particle2.get_left(), color=YELLOW)
        self.play(Create(connection))
        self.wait(1)

        self.play(
            particle1.animate.set_fill(BLUE, opacity=0.8),
            particle2.animate.set_fill(RED, opacity=0.8),
        )
        self.wait(1)

        # Show a text explanation
        explanation = Text(
            "When one particle is measured,\nthe other instantly reacts,\nno matter the distance.",
            font_size=32,
            line_spacing=1.5,
        )
        explanation.next_to(particle2, DOWN * 2)
        self.play(Write(explanation))
        self.wait(2)

        # Fade out everything
        self.play(*[FadeOut(mob) for mob in self.mobjects])