import numpy as np
import random
import math

from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram

from qgd_python.utils import get_unitary_from_qiskit_circuit
from qgd_python.gates.qgd_SX import qgd_SX
from scipy.stats import unitary_group
      

class Test_operations_squander:
    """This is a test class of the python iterface to compare the SQUANDER and the qiskit decomposition"""

    pi=np.pi


    def test_SX_get_matrix(self):
        r"""
        This method is called by pytest. 
        Test to create an instance of U3 gate and compare with qiskit.
        """
        global SX_qiskit
        SX_qiskit = [0]*6

        for qbit_num in range(1,7):

            # target qbit
            target_qbit = qbit_num-1

            # creating an instance of the C++ class
            SX = qgd_SX( qbit_num, target_qbit )

	    #SQUANDER#

            # get the matrix                       
            SX_squander = SX.get_Matrix( )

	    #print(SX_squander)
      
	    #QISKIT

            # Create a Quantum Circuit acting on the q register
            circuit = QuantumCircuit(qbit_num)

            # Add the CNOT gate on control qbit and target qbit
            circuit.sx( target_qbit )

            # the unitary matrix from the result object
            SX_qiskit[qbit_num-1] = get_unitary_from_qiskit_circuit( circuit )
            SX_qiskit[qbit_num-1] = np.asarray(SX_qiskit[qbit_num-1])

            # Draw the circuit        
            #print(SX_qiskit)
        
            #the difference between the SQUANDER and the qiskit result        
            delta_matrix=SX_squander-SX_qiskit[qbit_num-1]

            # compute norm of matrix
            error=np.linalg.norm(delta_matrix)

            print("Get_matrix: The difference between the SQUANDER and the qiskit result is: " , np.around(error,2))
            assert( error < 1e-3 ) 


    def test_SX_apply_to(self):
        r"""
        This method is called by pytest. 
        Test to create an instance of U3 gate and compare with qiskit.
        """
        for qbit_num in range(1,7):

            # target qbit
            target_qbit = qbit_num-1

            # creating an instance of the C++ class
            SX = qgd_SX( qbit_num, target_qbit )
        
            #create text matrix 
            test_m = unitary_group.rvs(((2**qbit_num)))           
            test_matrix = np.dot(test_m, test_m.conj().T)

	    #QISKIT      

            # apply the gate on the input array/matrix 
            SX_qiskit_apply_gate=np.matmul(SX_qiskit[qbit_num-1], test_matrix)

	    #SQUANDER

            SX_squander = test_matrix

            # apply the gate on the input array/matrix                
            SX.apply_to(SX_squander)       

            #the difference between the SQUANDER and the qiskit result        
            delta_matrix=SX_squander-SX_qiskit_apply_gate

            # compute norm of matrix
            error=np.linalg.norm(delta_matrix)

            print("Apply_to: The difference between the SQUANDER and the qiskit result is: " , np.around(error,2))
            assert( error < 1e-3 ) 


