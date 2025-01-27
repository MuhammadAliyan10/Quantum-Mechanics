# Quantum State Evolution and Measurement

## **Problem**

In quantum mechanics, particles are described by quantum states (wavefunctions). These states evolve over time, and measurements collapse them into observable outcomes.

The task is to:

1. Simulate the evolution of a quantum system's state over time.
2. Compute the probabilities of observing each state at specific times.
3. Analyze the measurement outcomes over multiple iterations (experiments) and summarize the results.

---

## **Scenario**

- A quantum system starts in a superposition state:

  \[ |ψ(0)\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) \]

- The system evolves under a unitary transformation \( U \) at each timestep. Assume \( U \) represents a simple rotation in the Hilbert space.
- At specific time intervals, we measure the state. Measurement collapses the state into either \( |0\rangle \) or \( |1\rangle \) with probabilities based on their amplitudes.
- We repeat the simulation over 1,000 experiments and analyze the distribution of measurement outcomes over time.

---

## **Steps to Solve**

### **1. Quantum State Initialization**

- Define the initial quantum state \( |ψ(0)\rangle \).
- Use NumPy to represent the state as a vector:

  \[ |ψ(0)\rangle = \begin{bmatrix}
  \frac{1}{\sqrt{2}} \\
  \frac{1}{\sqrt{2}}
  \end{bmatrix} \]

---

### **2. Define Unitary Transformation**

- Define the unitary operator \( U \), representing a rotation in the Hilbert space.
- Example:

  \[ U = \begin{bmatrix}
  \cos(\theta) & -\sin(\theta) \\
  \sin(\theta) & \cos(\theta)
  \end{bmatrix} \]

- Use \( \theta = \frac{\pi}{8} \) for the rotation angle.

---

### **3. Evolve the Quantum State**

- At each timestep, apply the unitary transformation \( U \) to the current state using matrix multiplication.
- Use NumPy's `np.dot()` function for this operation.

---

### **4. Perform Measurements**

- At specific intervals (e.g., every 10 timesteps):

  - Compute probabilities of states \( |0\rangle \) and \( |1\rangle \) as the square of the wavefunction amplitudes.

    \[ P(0) = |a_0|^2, \quad P(1) = |a_1|^2 \]

  - Perform a random collapse based on these probabilities using `np.random.choice()`.

---

### **5. Simulate Multiple Experiments**

- Repeat the simulation for 1,000 experiments.
- Collect measurement outcomes at each timestep.

---

### **6. Analyze Results Using Pandas**

- Group results by time and outcome.
- Compute the frequency of each outcome at each timestep.
- Calculate probabilities \( P(0) \) and \( P(1) \) from the frequencies.
- Visualize the probabilities over time using Matplotlib.

---

## **Extensions**

1. **Multi-Qubit Systems**: Extend the simulation to handle entangled states.
2. **Different Unitary Operators**: Experiment with other types of quantum gates (e.g., Hadamard or CNOT).
3. **Noise Modeling**: Add decoherence or noise to simulate realistic quantum systems.
