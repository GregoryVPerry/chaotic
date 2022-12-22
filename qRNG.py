#!/usr/bin/python3

# quantumRNG: dump 8192 int15 values from IBM Q quantum computer
# 
# portions of code borrowed from Russell Huffman's Quantum Dice
# https://qiskit.org/experiments/quantum-dice/
#
# 1) install Qiskit (IBM Quantum services library)
# 2) sign up for an account at https://quantum-computing.ibm.com
# 3) login to IBM Quantum, top right My Account -> Copy token
# 4) >>> import qiskit as qk
# 5) >>> qk.IBMQ.save_account('YOUR_TOKEN')
#

import sys
import numpy as np
from qiskit import QuantumCircuit, execute, Aer, IBMQ, ClassicalRegister, QuantumRegister
from qiskit.compiler import transpile, assemble
from qiskit.visualization import *
from qiskit.quantum_info import Pauli, state_fidelity, basis_state, process_fidelity

# load IBM Q creds
provider = IBMQ.load_account()

# create a 15 qubit quantum circuit with H gates (Hadamard gates) on each 
qc = QuantumCircuit(15, 15)

for i in range(15):
    qc.h(i)

qc.measure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
    
# assign quantum backend and dispatch circuit
backend = provider.get_backend(sys.argv[1])
shots = 8192
job = execute(qc, backend, shots=shots, memory=True)


memory = [] # destination list of 15-bit values sampled from quantum circuit

# independent results instead of probability
result = job.result()
memory = result.get_memory()

intArray = np.array([], dtype='int16')

for i in range(0, len(memory)):
    intArray = np.append(intArray, (int(memory[i], 2)))

print(*intArray.tolist(), sep='\n') # dump 8196 int15 values to stdout
