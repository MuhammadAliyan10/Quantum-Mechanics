from manim import *

class SpacetimeSolarSystem(Scene):
    def construct(self):
        # Step 1: Create the spacetime "sheet" (flat grid)
        spacetime = NumberPlane(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            axis_config={"stroke_opacity": 0},  # Hide axes
            background_line_style={"stroke_opacity": 0.4, "stroke_color": BLUE_E}
        ).scale(1.5)
        self.play(Create(spacetime), run_time=2)
        self.wait(1)

        # Step 2: Create the Sun and move it to the sheet
        sun = Dot(point=ORIGIN, radius=0.4, color=YELLOW).add_glow_effect(color=YELLOW, glow_factor=2)
        self.play(FadeIn(sun), run_time=1)

        # Bend the spacetime sheet under the Sun's mass
        def warp_function(point):
            x, y, z = point
            r = np.sqrt(x**2 + y**2) + 0.1  # Avoid division by zero
            z_shift = -2 / r  # Stronger warp for visual effect
            return np.array([x, y, z_shift])
        
        warped_spacetime = spacetime.copy().apply_function(warp_function)
        self.play(Transform(spacetime, warped_spacetime), run_time=3)
        self.wait(1)

        # Step 3: Create a simple solar system
        # Earth
        earth = Dot(radius=0.15, color=BLUE_C).move_to(RIGHT * 3 + UP * 0.5)
        earth_orbit = Circle(radius=3, color=WHITE).set_opacity(0.2)
        earth_orbit.shift(UP * 0.5)  # Slight offset to follow warp

        # Mars (another planet for variety)
        mars = Dot(radius=0.12, color=RED_D).move_to(RIGHT * 4.5 + DOWN * 0.3)
        mars_orbit = Circle(radius=4.5, color=WHITE).set_opacity(0.2)
        mars_orbit.shift(DOWN * 0.3)

        # Add planets and orbits
        self.play(
            FadeIn(earth), Create(earth_orbit),
            FadeIn(mars), Create(mars_orbit),
            run_time=2
        )

        # Animate orbits
        self.play(
            MoveAlongPath(earth, earth_orbit, rate_func=linear),
            MoveAlongPath(mars, mars_orbit, rate_func=linear),
            run_time=5
        )

        # Final touch: Cosmic background
        stars = Text("✨").scale(10).set_opacity(0.1).to_edge(UP).set_color_by_gradient(PURPLE, BLACK)
        self.play(FadeIn(stars), run_time=1)
        self.wait(2)
