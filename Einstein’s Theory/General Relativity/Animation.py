from manim import *


class SpacetimeSolarSystem(MovingCameraScene):  # Changed to MovingCameraScene
    def construct(self):
        # Step 1: Create the spacetime "sheet" (flat grid)
        spacetime = NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-7, 7, 1],
            axis_config={"stroke_opacity": 0},
            background_line_style={"stroke_opacity": 0.4, "stroke_color": BLUE_E},
        ).scale(1.5)
        self.add(spacetime)  # Start with flat sheet

        # Step 2: Create a more realistic Sun with layered glow
        sun = Circle(radius=0.4, color=YELLOW, fill_opacity=1).set_stroke(
            color=ORANGE, width=2
        )
        glow = VGroup(
            Circle(radius=0.8, color=YELLOW).set_opacity(0.4).set_stroke(width=0),
            Circle(radius=1.2, color=YELLOW).set_opacity(0.2).set_stroke(width=0),
            Circle(radius=1.6, color=ORANGE).set_opacity(0.1).set_stroke(width=0),
        )
        sun_with_glow = VGroup(glow, sun).move_to(ORIGIN)
        self.play(FadeIn(sun_with_glow), run_time=1.5)

        # Bend spacetime as Sun appears
        def warp_function(point):
            x, y, z = point
            r = np.sqrt(x**2 + y**2) + 0.1  # Avoid division by zero
            z_shift = -2.5 / r  # Stronger, smoother warp
            return np.array([x, y, z_shift])

        warped_spacetime = spacetime.copy().apply_function(warp_function)
        self.play(Transform(spacetime, warped_spacetime), run_time=3)
        self.wait(1)

        # Step 3: Create planets with realistic orbits
        # Earth with Moon
        earth = Dot(radius=0.15, color=BLUE_C)
        moon = Dot(radius=0.05, color=GRAY).move_to(RIGHT * 0.3)  # Moon orbits Earth
        earth_group = VGroup(earth, moon).move_to(RIGHT * 3 + UP * 0.5)
        earth_orbit = (
            Circle(radius=3, color=WHITE).set_opacity(0.2).rotate(PI / 12)
        )  # Tilted orbit

        # Mars
        mars = Dot(radius=0.12, color=RED_D).move_to(RIGHT * 4.5 + DOWN * 0.3)
        mars_orbit = (
            Circle(radius=4.5, color=WHITE).set_opacity(0.2).rotate(-PI / 18)
        )  # Slight tilt

        # Add planets and orbits
        self.play(
            FadeIn(earth_group),
            Create(earth_orbit),
            FadeIn(mars),
            Create(mars_orbit),
            run_time=2,
        )

        # Step 4: Animate realistic orbits
        # Earth and Moon orbit Sun, Moon orbits Earth
        self.play(
            Rotate(
                earth_group,
                angle=2 * PI,
                about_point=ORIGIN,
                rate_func=linear,
                run_time=5,
            ),
            Rotate(
                moon,
                angle=10 * PI,
                about_point=earth.get_center(),
                rate_func=linear,
                run_time=5,
            ),  # Faster Moon orbit
            Rotate(
                mars, angle=2 * PI, about_point=ORIGIN, rate_func=linear, run_time=6
            ),  # Slower Mars
            run_time=6,
        )

        # Step 5: Cinematic camera shift
        # Using MovingCameraScene’s camera (self.camera.frame)
        self.play(
            self.camera.frame.animate.move_to(UP * 2 + RIGHT * 2).set_width(
                self.camera.frame.get_width() * 1.2
            ),
            run_time=3,
        )

        # Step 6: Cosmic background and final touches
        stars = (
            Text("✨")
            .scale(10)
            .set_opacity(0.1)
            .to_edge(UP)
            .set_color_by_gradient(PURPLE, BLACK)
        )
        self.play(FadeIn(stars), run_time=1)
        self.wait(2)

        # Fade out for movie-like ending
        self.play(FadeOut(Group(*self.mobjects)), run_time=2)
