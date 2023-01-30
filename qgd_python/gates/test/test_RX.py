import numpy as np
import random

from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram

from qgd_python.utils import get_unitary_from_qiskit_circuit
from qgd_python.gates.qgd_RX import qgd_RX
import math


class Test_operations_squander:
    """This is a test class of the python iterface to the gates of the QGD package"""

    pi=np.pi

    # number of qubits
    qbit_num = 1

    # target qbit
    target_qbit = 0

    # parameters
    parameters = np.array( [pi/2*0.32, pi*1.2, pi/2*0.89] )

    # creating an instance of the C++ class
    RX = qgd_RX( qbit_num, target_qbit )

    def test_RX_get_matrix(self):

	#SQUANDER
        r"""
        This method is called by pytest. 
        Test to create an instance of RX gate.
        """

        # get the matrix              
        RX_squander = self.RX.get_Matrix( self.parameters )
        
        #print(RX_squander)

	#QISKIT

        # Create a Quantum Circuit acting on the q register
        circuit = QuantumCircuit(self.qbit_num)

        # Add the u3 gate on qubit pi, pi,
        circuit.rx(self.parameters[0]*2, self.target_qbit)

        # the unitary matrix from the result object
        RX_qiskit = get_unitary_from_qiskit_circuit( circuit )
        RX_qiskit = np.asarray(RX_qiskit)
        
        # Draw the circuit        
        #print(RX_qiskit)
        
        #the difference between the SQUANDER and the qiskit result        
        delta_matrix=RX_squander-RX_qiskit

        # compute norm of matrix
        error=np.linalg.norm(delta_matrix)

        print("The difference between the SQUANDER and the qiskit result is: " , np.around(error,2))
        assert( error < 1e-3 )        
 
    def test_RX_apply_to(self):
        r"""
        This method is called by pytest. 
        Test to create an instance of U3 gate and compare with qiskit.
        """

	#SQUANDER

        # get the matrix               
        RX_squander = self.RX.get_Matrix( self.parameters )

        # apply the gate on the input array/matrix                
        self.RX.apply_to(self.parameters, RX_squander )
        
        #print(RX_squander)

	#QISKIT      

        # Create a Quantum Circuit acting on the q register
        circuit = QuantumCircuit(self.qbit_num)

        # Add the rx gate on qubit pi, pi,
        circuit.rx(self.parameters[0]*2, self.target_qbit)

        # the unitary matrix from the result object
        RX_qiskit = get_unitary_from_qiskit_circuit( circuit )
        RX_qiskit = np.asarray(RX_qiskit)

        # the R gate 
        rx_gate=np.array([[math.cos(self.parameters[0]), -1.j*math.sin(self.parameters[0])], [-1.j*math.sin(self.parameters[0]) ,math.cos(self.parameters[0])] ])

        # apply the gate on the input array/matrix 
        RX_qiskit_apply_gate=np.matmul(RX_qiskit, rx_gate)

        #the difference between the SQUANDER and the qiskit result        
        delta_matrix=RX_squander-RX_qiskit_apply_gate

        # compute norm of matrix
        error=np.linalg.norm(delta_matrix)

        print("The difference between the SQUANDER and the qiskit result is: " , np.around(error,2))
        assert( error < 1e-3 ) 


