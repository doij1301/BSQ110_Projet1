from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import Aer, execute, transpile
from qiskit.tools.visualization import plot_histogram, plot_state_city
import qiskit.quantum_info as qi
from qiskit import IBMQ
from qiskit.tools import job_monitor
from qiskit.providers.ibmq import least_busy


def execution_ibmq(circuit):
    IBMQ.load_account()
    provider = IBMQ.get_provider(hub='ibm-q', group='open', project='main')
    # provider = IBMQ.get_provider(hub = 'ibm-q-qida',group='is-quantum-hub',project='algolab')

    for backends in provider.backends(filters=lambda x: not x.configuration().simulator):
        print(backends)

    backend = least_busy(provider.backends(filters=lambda
        x: x.configuration().n_qubits < 10 and not x.configuration().simulator and x.status().operational == True))

    job = execute(circuit, backend, shots=1000)
    job_monitor(job)
    counts = job.result().get_counts()
    print(counts)
