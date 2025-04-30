import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class QuantumSimulator:
    def __init__(self, root):
        print("Initializing QuantumSimulator")  # Debug
        self.root = root
        self.root.title("Quantum Gates 3D Simulator")
        self.root.geometry("450x600")  # Slightly larger for better button size
        self.root.resizable(False, False)

        # Color scheme
        self.background = "#040914"  # Dark navy
        self.button_bg = "#9575FF"  # Purple for gates
        self.special_button_bg = "#39C3EF"  # Cyan for utility
        self.button_border = "#6A48D7"
        self.special_button_border = "#2A93B8"
        self.display_bg = "#2A2A2A"  # Dark gray for LCD
        self.text_color = "#E0E0E0"  # Light gray for display
        self.button_text_color = "#FFFFFF"  # White for buttons
        self.active_button_bg = "#7F5FE6"
        self.active_special_button_bg = "#2EA8D2"

        # Fonts
        self.button_font = ("Arial", 14)  # Larger for readability
        self.display_font = ("Arial", 16, "bold")

        # Gate sequence
        self.gate_sequence = []

        # Configure root
        self.root.configure(bg=self.background)
        print("Root configured")  # Debug

        # Create GUI
        self.create_display()
        self.create_gate_buttons()
        self.create_utility_buttons()

        # Force update and raise window
        self.root.update()
        self.root.lift()
        print("GUI created, entering mainloop")  # Debug

    def create_display(self):
        print("Creating display")  # Debug
        display_frame = tk.Frame(self.root, bg=self.background)
        display_frame.pack(pady=5, padx=5, fill="x")

        self.display_var = tk.StringVar(value="No gates selected")
        display_label = tk.Label(
            display_frame,
            textvariable=self.display_var,
            font=self.display_font,
            fg=self.text_color,
            bg=self.display_bg,
            anchor="w",
            relief="sunken",
            bd=3,
            width=35,
        )
        display_label.pack(pady=5, padx=5, fill="x")
        print("Display packed")  # Debug

    def create_gate_buttons(self):
        print("Creating gate buttons")  # Debug
        gates_frame = tk.Frame(self.root, bg=self.background)
        gates_frame.pack(pady=5, padx=5)

        gates = ["H", "X", "Y", "Z", "CNOT", "SWAP", "T", "S"]
        for i, gate in enumerate(gates):
            btn = tk.Button(
                gates_frame,
                text=gate,
                font=self.button_font,
                bg=self.button_bg,
                fg=self.button_text_color,
                activebackground=self.active_button_bg,
                activeforeground=self.button_text_color,
                bd=2,
                relief="flat",
                width=8,  # Larger buttons
                command=lambda g=gate: self.add_gate(g),
            )
            btn.grid(row=i // 4, column=i % 4, padx=1, pady=1, sticky="nsew")
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#A68AFF"))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg=self.button_bg))
        print("Gate buttons gridded")  # Debug

    def create_utility_buttons(self):
        print("Creating utility buttons")  # Debug
        utility_frame = tk.Frame(self.root, bg=self.background)
        utility_frame.pack(pady=5, padx=5, fill="x")

        buttons = [
            ("Clear", self.clear_display),
            ("Simulate", self.simulate),
            ("About", self.show_about),
            ("Exit", self.exit_app),
        ]
        for i, (text, cmd) in enumerate(buttons):
            btn = tk.Button(
                utility_frame,
                text=text,
                font=self.button_font,
                bg=self.special_button_bg,
                fg=self.button_text_color,
                activebackground=self.active_special_button_bg,
                activeforeground=self.button_text_color,
                bd=2,
                relief="flat",
                width=10,  # Larger utility buttons
                command=cmd,
            )
            btn.grid(row=0, column=i, padx=1, pady=1, sticky="nsew")
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#4AD4FF"))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg=self.special_button_bg))
        print("Utility buttons gridded")  # Debug

    def add_gate(self, gate):
        self.gate_sequence.append(gate)
        display_text = " -> ".join(self.gate_sequence)
        self.display_var.set(display_text if display_text else "No gates selected")
        self.root.update()  # Force display update
        print(
            f"Added gate: {gate}, Sequence: {self.gate_sequence}, Display: {display_text}"
        )  # Debug

    def clear_display(self):
        self.gate_sequence = []
        self.display_var.set("No gates selected")
        self.root.update()  # Force display update
        print("Display cleared")  # Debug

    def simulate(self):
        print("Simulating gates:", self.gate_sequence)  # Debug
        if not self.gate_sequence:
            messagebox.showinfo("Simulation", "No gates to simulate!")
            return

        # Check for multi-qubit gates
        multi_qubit = any(gate in ["CNOT", "SWAP"] for gate in self.gate_sequence)
        if multi_qubit:
            messagebox.showwarning(
                "Simulation Warning",
                "CNOT and SWAP are multi-qubit gates and cannot be visualized on a single Bloch sphere. Showing single-qubit gates only.",
            )

        # Show Bloch sphere with animation
        self.show_bloch_sphere()

    def compute_bloch_vectors(self):
        # Initial state |0> = [1, 0]
        state = np.array([1, 0], dtype=complex)
        vectors = [[0, 0, 1]]  # Initial Bloch vector for |0>

        # Gate matrices
        gates = {
            "H": np.array([[1, 1], [1, -1]]) / np.sqrt(2),
            "X": np.array([[0, 1], [1, 0]]),
            "Y": np.array([[0, -1j], [1j, 0]]),
            "Z": np.array([[1, 0], [0, -1]]),
            "T": np.array([[1, 0], [0, np.exp(1j * np.pi / 4)]]),
            "S": np.array([[1, 0], [0, 1j]]),
        }

        # Apply gates and compute Bloch vectors
        for gate in self.gate_sequence:
            if gate in gates:  # Skip CNOT, SWAP
                state = gates[gate] @ state
                rho = np.outer(state, state.conj())
                sigma_x = np.array([[0, 1], [1, 0]])
                sigma_y = np.array([[0, -1j], [1j, 0]])
                sigma_z = np.array([[1, 0], [0, -1]])
                x = np.trace(rho @ sigma_x).real
                y = np.trace(rho @ sigma_y).real
                z = np.trace(rho @ sigma_z).real
                vectors.append([x, y, z])
                print(
                    f"Gate: {gate}, State: {state}, Bloch vector: [{x:.3f}, {y:.3f}, {z:.3f}]"
                )  # Debug
            else:
                vectors.append(vectors[-1])  # No change for CNOT/SWAP
        return vectors

    def show_bloch_sphere(self):
        print("Showing Bloch sphere")  # Debug
        vectors = self.compute_bloch_vectors()

        fig = plt.figure(figsize=(7, 7))
        ax = fig.add_subplot(111, projection="3d")

        # Draw sphere
        u = np.linspace(0, 2 * np.pi, 20)
        v = np.linspace(0, np.pi, 20)
        x = np.outer(np.cos(u), np.sin(v))
        y = np.outer(np.sin(u), np.sin(v))
        z = np.outer(np.ones(np.size(u)), np.cos(v))
        ax.plot_surface(x, y, z, color="c", alpha=0.3)

        # Draw axes
        ax.plot([-1, 1], [0, 0], [0, 0], "k-", lw=1)
        ax.plot([0, 0], [-1, 1], [0, 0], "k-", lw=1)
        ax.plot([0, 0], [0, 0], [-1, 1], "k-", lw=1)

        # Axis annotations
        ax.text(1.1, 0, 0, "+1", color="k")
        ax.text(-1.1, 0, 0, "-1", color="k")
        ax.text(0, 1.1, 0, "+i", color="k")  # Y-axis involves imaginary
        ax.text(0, -1.1, 0, "-i", color="k")
        ax.text(0, 0, 1.1, "+1", color="k")
        ax.text(0, 0, -1.1, "-1", color="k")
        ax.text(1.3, 0, 0, "X", color="k")
        ax.text(0, 1.3, 0, "Y", color="k")
        ax.text(0, 0, 1.3, "Z", color="k")

        # Initial vector (placeholder for animation)
        vector = vectors[0]
        quiver = ax.quiver(
            0,
            0,
            0,
            vector[0],
            vector[1],
            vector[2],
            color="r",
            lw=2,
            arrow_length_ratio=0.1,
        )

        # Animation function
        def update(frame):
            nonlocal quiver
            vector = vectors[min(frame, len(vectors) - 1)]
            quiver.remove()
            quiver = ax.quiver(
                0,
                0,
                0,
                vector[0],
                vector[1],
                vector[2],
                color="r",
                lw=2,
                arrow_length_ratio=0.1,
            )
            ax.set_title(
                f"Bloch Sphere - Gate: {self.gate_sequence[frame] if frame < len(self.gate_sequence) else 'Final'}"
            )
            print(
                f"Animation frame {frame}: Vector [{vector[0]:.3f}, {vector[1]:.3f}, {vector[2]:.3f}]"
            )  # Debug
            return [quiver]

        # Set limits and labels
        ax.set_xlim([-1.2, 1.2])
        ax.set_ylim([-1.2, 1.2])
        ax.set_zlim([-1.2, 1.2])
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        ax.set_box_aspect([1, 1, 1])

        # Animate
        ani = FuncAnimation(fig, update, frames=len(vectors), interval=500, blit=False)
        plt.show()

    def show_about(self):
        messagebox.showinfo(
            "About",
            "Quantum Gates 3D Simulator\nVersion 1.0\nDeveloped by xAI\n\nVisualize quantum gate sequences on an animated Bloch sphere.",
        )
        print("About dialog shown")  # Debug

    def exit_app(self):
        print("Exiting application")  # Debug
        self.root.quit()


if __name__ == "__main__":
    print("Starting application")  # Debug
    root = tk.Tk()
    app = QuantumSimulator(root)
    root.mainloop()
    print("Mainloop exited")  # Debug
