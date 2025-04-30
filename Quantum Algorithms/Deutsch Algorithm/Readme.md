## What is the Deutsch Algorithm?

_Imagine you have a mysterious machine (called an oracle) that takes a single bit (0 or 1) as input and gives a single bit (0 or 1) as output. This machine is running one of four possible functions:_

1. _f1: Always outputs 0 (f(0) = 0, f(1) = 0) → Constant_
2. _f2: Always outputs 1 (f(0) = 1, f(1) = 1) → Constant_
3. _f3: Outputs the input (f(0) = 0, f(1) = 1) → Balanced_
4. _f4: Outputs the opposite of the input (f(0) = 1, f(1) = 0) → Balanced_

- _A constant function gives the same output (0 or 1) for both inputs._
- _A balanced function gives different outputs (0 for one input, 1 for the other)._

_Your task is to figure out whether the function is constant (like f1 or f2) or balanced (like f3 or f4). On a classical computer, you’d need to check both inputs (f(0) and f(1)), meaning two queries to the oracle. The Deutsch Algorithm, using a quantum computer, can solve this with just one query by exploiting quantum properties like superposition and interference._

_Think of it like trying to figure out if a coin is rigged to show heads on both sides or heads on one side and tails on the other. Classically, you’d flip it twice to check both sides. Quantumly, you can “flip” it in a special way to learn the answer in one go._

## Why is it Special?

_The Deutsch Algorithm shows a quantum computer can be faster than a classical one, even if the speedup is small (one query vs. two). It’s like a proof-of-concept, showing quantum computers can do things differently by using quantum superposition (being in multiple states at once) and quantum gates (special operations that manipulate quantum states)._

## The Algorithm in Simple Terms

**Algorithm DeutschAlgorithm(oracle):**

1. Start with two qubits: first qubit = |0⟩, second qubit = |1⟩
2. Apply a Hadamard gate (H) to both qubits to put them in superposition
3. Send both qubits through the oracle (which applies the function f)
4. Apply a Hadamard gate to the first qubit again
5. Measure the first qubit: - If it’s |0⟩, the function is constant - If it’s |1⟩, the function is balanced
