# Simulating Quantum Circuits on a Classical Computer

## **Problem**

Simulate the behavior of a simple quantum computer executing quantum circuits. The goal is to:

1. Define quantum gates (e.g., Hadamard, Pauli-X, CNOT).
2. Construct a quantum circuit using these gates.
3. Simulate the quantum state evolution as the gates are applied.
4. Perform measurements on the quantum state to observe the outcomes.

---

## **Scenario**

A quantum computer operates on qubits using quantum gates to perform computations. For this simulation:

- Start with two qubits in the \( |0\rangle \) state.
- Apply a series of gates:
  1. Apply a Hadamard gate to the first qubit to create superposition.
  2. Apply a CNOT gate with the first qubit as the control and the second qubit as the target to create entanglement.
- Measure both qubits to observe their final states.

---

## **Steps to Solve**

### **1. Define Qubit States**

- Represent the state of the two-qubit system using a vector:

  \[ |\psi\rangle = \begin{bmatrix} 1 \\\ 0 \\\ 0 \\\ 0 \end{bmatrix} \]

  where the basis states are \( |00\rangle, |01\rangle, |10\rangle, |11\rangle \).

---

### **2. Define Quantum Gates**

- Use NumPy to define the following gates as matrices:

  - **Hadamard Gate (H):** Creates superposition for a single qubit.
    \[
    H = \frac{1}{\sqrt{2}} \begin{bmatrix}
    1 & 1 \\\ 1 & -1
    \end{bmatrix}
    \]

  - **Pauli-X Gate:** Acts as a NOT gate, flipping \( |0\rangle \) to \( |1\rangle \).
    \[
    X = \begin{bmatrix}
    0 & 1 \\\ 1 & 0
    \end{bmatrix}
    \]

  - **CNOT Gate:** Entangles two qubits.
    \[
    \text{CNOT} = \begin{bmatrix}
    1 & 0 & 0 & 0 \\\ 0 & 1 & 0 & 0 \\\ 0 & 0 & 0 & 1 \\\ 0 & 0 & 1 & 0
    \end{bmatrix}
    \]

---

### **3. Construct the Circuit**

- Define a sequence of operations:
  1. Apply the Hadamard gate to the first qubit.
  2. Apply the CNOT gate to both qubits.

---

### **4. Simulate Quantum State Evolution**

- Use matrix multiplication to evolve the quantum state.
- Example:

  \[ |ψ*{\text{new}}\rangle = U \cdot |ψ*{\text{old}}\rangle \]

  where \( U \) is the gate being applied.

---

### **5. Perform Measurements**

- Compute the probability of each basis state by squaring the amplitudes of the final state vector.
- Use NumPy's `np.random.choice()` to simulate measurement outcomes based on these probabilities.

---

### **6. Analyze Results**

- Simulate the circuit over multiple iterations (e.g., 1,000 times).
- Use Pandas to:
  - Count occurrences of each measurement outcome.
  - Compute probabilities of outcomes \( |00\rangle, |01\rangle, |10\rangle, |11\rangle \).
- Visualize the results using Matplotlib.

---
