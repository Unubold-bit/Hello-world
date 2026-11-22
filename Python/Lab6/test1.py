from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator

# 1. Set up 3 qubits and 2 classical bits in distinct registers
q = QuantumRegister(3, name="q")
c_alice = ClassicalRegister(2, name="alice_bits")
c_bob = ClassicalRegister(1, name="bob_result")
qc = QuantumCircuit(q, c_alice, c_bob)

# 2. Prepare a secret quantum state on q[0] (Alice's payload)
qc.rx(1.2, q[0])  # Rotate around X-axis by 1.2 radians
qc.rz(0.7, q[0])  # Rotate around Z-axis by 0.7 radians
qc.barrier()

# 3. Create an entangled Bell pair between q[1] (Alice) and q[2] (Bob)
qc.h(q[1])
qc.cx(q[1], q[2])
qc.barrier()

# 4. Alice entangles her secret qubit q[0] with her half of the Bell pair q[1]
qc.cx(q[0], q[1])
qc.h(q[0])
qc.barrier()

# 5. Alice measures both of her qubits mid-circuit
qc.measure(q[0], c_alice[0])
qc.measure(q[1], c_alice[1])

# 6. Dynamic Conditional Logic: Bob applies corrections based on Alice's classical bits
with qc.if_test((c_alice[1], 1)):
    qc.x(q[2])
with qc.if_test((c_alice[0], 1)):
    qc.z(q[2])
qc.barrier()

# 7. Verify: Reverse the original secret rotations on Bob's qubit q[2]
# If teleportation worked, q[2] will return cleanly to state |0>
qc.rz(-0.7, q[2])
qc.rx(-1.2, q[2])
qc.measure(q[2], c_bob[0])

# 8. Simulate the circuit 1,000 times
simulator = AerSimulator()
compiled = transpile(qc, simulator)
counts = simulator.run(compiled, shots=1000).result().get_counts()

print(qc.draw())
print("\nSimulation Counts:", counts)

