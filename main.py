from qiskit import QuantumCircuit, execute, IBMQ
from qiskit.tools.monitor import job_monitor
from qiskit import QuantumRegister
from qiskit import ClassicalRegister
print('\nQuantum Full Adder')
print('by yousef yousef \n')
IBMQ.enable_account('API token')
provider = IBMQ.get_provider(hub='ibm-q')
q = QuantumRegister(5, 'q')
c = ClassicalRegister(2, 'c')
circuit = QuantumCircuit(q, c)
for i, counter in enumerate(range(3)):
while (True):
try:
num = int(input("enter value: "))
break
except:
print("please enter numbers only ")
continue
if ((num == 1)):
circuit.x(q[counter ])
print(" Qubit", counter , " saved as 1 \n")
else:
print(" Qubit", counter , " saved as 0 \n")
circuit.cx(q[0], q[3])
circuit.cx(q[1], q[3])
circuit.cx(q[2], q[3])
circuit.ccx(q[0], q[1], q[4])
circuit.ccx(q[0], q[2], q[4])
circuit.ccx(q[1], q[2], q[4])
circuit.measure(q[3], c[0])
circuit.measure(q[4], c[1])
backend = provider.get_backend('ibmq_qasm_simulator')
job = execute(circuit, backend, shots=1)
job_monitor(job)
counts = job.result().get_counts()
print('RESULT: ', counts, '\n')
input(
