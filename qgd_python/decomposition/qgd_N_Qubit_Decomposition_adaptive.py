## #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 15:44:26 2020
Copyright (C) 2020 Peter Rakyta, Ph.D.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see http://www.gnu.org/licenses/.

@author: Peter Rakyta, Ph.D.
"""

## \file qgd_N_Qubit_Decomposition.py
##    \brief A QGD Python interface class for the decomposition of N-qubit unitaries into a set of two-qubit and one-qubit gates.


import numpy as np
from os import path
from qgd_python.decomposition.qgd_N_Qubit_Decomposition_adaptive_Wrapper import qgd_N_Qubit_Decomposition_adaptive_Wrapper



##
# @brief A QGD Python interface class for the decomposition of N-qubit unitaries into U3 and CNOT gates.
class qgd_N_Qubit_Decomposition_adaptive(qgd_N_Qubit_Decomposition_adaptive_Wrapper):
    
    
## 
# @brief Constructor of the class.
# @param Umtx The unitary matrix to be decomposed.
# @param optimize_layer_num Set true to optimize the minimum number of operation layers required in the decomposition, or false when the predefined maximal number of layer gates is used (ideal for general unitaries).
# @param initial_guess String indicating the method to guess initial values for the optimalization. Possible values: "zeros" ,"random", "close_to_zero".
# @return An instance of the class
    def __init__( self, Umtx, level_limit_max=8, level_limit_min=0, method='LIMITED', topology=None ):

        ## the number of qubits
        self.qbit_num = int(round( np.log2( len(Umtx) ) ))

        # validate input parameters
        if method == 'LIMITED' or method == 'limited' :
            pass
        elif method == 'GENERAL' or method == 'general' :
            pass
        else: 
            print('Invalid input argument method=', method, '. Falling back to default.')
            method = 'limited'

        topology_validated = list()
        if isinstance(topology, list) or isinstance(topology, tuple):
            for item in topology:
                if isinstance(item, tuple) and len(item) == 2:
                    item_validated = (np.intc(item[0]), np.intc(item[1]))
                    topology_validated.append(item_validated)
                else:
                    print("Elements of topology should be two-component tuples (int, int)")
                    return
        elif topology == None:
            pass
        else:
            print("Input parameter topology should be a list of (int, int) describing the connected qubits in the topology")
            return
        

        # call the constructor of the wrapper class
        super(qgd_N_Qubit_Decomposition_adaptive, self).__init__(Umtx, self.qbit_num, level_limit_max, level_limit_min, method=method, topology=topology_validated)


##
# @brief Wrapper function to call the start_decomposition method of C++ class N_Qubit_Decomposition
# @param prepare_export Logical parameter. Set true to prepare the list of gates to be exported, or false otherwise.
    def Start_Decomposition(self,prepare_export=True):

	# call the C wrapper function
        super(qgd_N_Qubit_Decomposition_adaptive, self).Start_Decomposition(prepare_export=prepare_export)


##
# @brief Call to reorder the qubits in the matrix of the gate
# @param qbit_list The reordered list of qubits spanning the matrix
    def Reorder_Qubits( self, qbit_list ):

	# call the C wrapper function
        super(qgd_N_Qubit_Decomposition_adaptive, self).Reorder_Qubits(qbit_list)


##
# @brief @brief Call to print the gates decomposing the initial unitary. These gates brings the intial matrix into unity.
    def List_Gates(self):

	# call the C wrapper function
        super(qgd_N_Qubit_Decomposition_adaptive, self).List_Gates()

##
# @brief Export the unitary decomposition into Qiskit format.
# @return Return with a Qiskit compatible quantum circuit.
    def get_Quantum_Circuit( self ):

        from qiskit import QuantumCircuit

        # creating Qiskit quantum circuit
        circuit = QuantumCircuit(self.qbit_num)

        # retrive the list of decomposing gate structure
        gates = self.get_Gates()

        # constructing quantum circuit
        for idx in range(len(gates)-1, -1, -1):

            gate = gates[idx]

            if gate.get("type") == "CNOT":
                # adding CNOT gate to the quantum circuit
                circuit.cx(gate.get("control_qbit"), gate.get("target_qbit"))

            elif gate.get("type") == "CZ":
                # adding CZ gate to the quantum circuit
                circuit.cz(gate.get("control_qbit"), gate.get("target_qbit"))

            elif gate.get("type") == "CH":
                # adding CZ gate to the quantum circuit
                circuit.ch(gate.get("control_qbit"), gate.get("target_qbit"))

            elif gate.get("type") == "SYC":
                # Sycamore gate
                print("Unsupported gate in the circuit export: Sycamore gate")
                return None;

            elif gate.get("type") == "U3":
                # adding U3 gate to the quantum circuit
                circuit.u(gate.get("Theta"), gate.get("Phi"), gate.get("Lambda"), gate.get("target_qbit"))

            elif gate.get("type") == "RX":
                # RX gate
                circuit.rx(gate.get("Theta"), gate.get("target_qbit"))

            elif gate.get("type") == "RY":
                # RY gate
                circuit.ry(gate.get("Theta"), gate.get("target_qbit"))

            elif gate.get("type") == "RZ":
                # RZ gate
                circuit.rz(gate.get("Phi"), gate.get("target_qbit"))

            elif gate.get("type") == "X":
                # RZ gate
                circuit.x(gate.get("target_qbit"))

            elif gate.get("type") == "SX":
                # RZ gate
                circuit.sx(gate.get("target_qbit"))


        return circuit




##
# @brief Export the unitary decomposition into Qiskit format.
# @return Return with a Qiskit compatible quantum circuit.
    def get_Cirq_Circuit( self ):

        import cirq


        # creating Cirq quantum circuit
        circuit = cirq.Circuit()

        # creating qubit register
        q = cirq.LineQubit.range(self.qbit_num)

        # retrive the list of decomposing gate structure
        gates = self.get_Gates()

        # constructing quantum circuit
        for idx in range(len(gates)-1, -1, -1):

            gate = gates[idx]

            if gate.get("type") == "CNOT":
                # adding CNOT gate to the quantum circuit
                circuit.append(cirq.CNOT(q[self.qbit_num-1-gate.get("control_qbit")], q[self.qbit_num-1-gate.get("target_qbit")]))

            elif gate.get("type") == "CZ":
                # adding CZ gate to the quantum circuit
                circuit.append(cirq.CZ(q[self.qbit_num-1-gate.get("control_qbit")], q[self.qbit_num-1-gate.get("target_qbit")]))

            elif gate.get("type") == "CH":
                # adding CZ gate to the quantum circuit
                circuit.append(cirq.CH(q[self.qbit_num-1-gate.get("control_qbit")], q[self.qbit_num-1-gate.get("target_qbit")]))

            elif gate.get("type") == "SYC":
                # Sycamore gate
                circuit.append(cirq.google.SYC(q[self.qbit_num-1-gate.get("control_qbit")], q[self.qbit_num-1-gate.get("target_qbit")]))

            elif gate.get("type") == "U3":
                print("Unsupported gate in the Cirq export: U3 gate")
                return None;

            elif gate.get("type") == "RX":
                # RX gate
                circuit.append(cirq.rx(gate.get("Theta")).on(q[self.qbit_num-1-gate.get("target_qbit")]))

            elif gate.get("type") == "RY":
                # RY gate
                circuit.append(cirq.ry(gate.get("Theta")).on(q[self.qbit_num-1-gate.get("target_qbit")]))

            elif gate.get("type") == "RZ":
                # RZ gate
                circuit.append(cirq.rz(gate.get("Phi")).on(q[self.qbit_num-1-gate.get("target_qbit")]))

            elif gate.get("type") == "X":
                # RZ gate
                circuit.append(cirq.x(q[self.qbit_num-1-gate.get("target_qbit")]))

            elif gate.get("type") == "SX":
                # RZ gate
                circuit.append(cirq.sx(q[self.qbit_num-1-gate.get("target_qbit")]))


        return circuit


##
# @brief Call to import initial quantum circuit in QISKIT format to be further comporessed
# @param qc_in The quantum circuit to be imported
    def import_Qiskit_Circuit( self, qc_in ):  

        from qiskit import QuantumCircuit, transpile
        from qiskit.circuit import ParameterExpression
        from qgd_python.gates.qgd_Gates_Block import qgd_Gates_Block

        qc = transpile(qc_in, optimization_level=0, basis_gates=['cz', 'u3'], layout_method='sabre')
        #print('Depth of imported Qiskit transpiled quantum circuit:', qc.depth())
        print('Gate counts in teh imported Qiskit transpiled quantum circuit:', qc.count_ops())
        #print(qc)
        
        # get the size of the register
        gate = qc.data[0]
        qubits = gate[1]
        register_size = qubits[0].register.size

        # prepare dictionary for single qubit gates
        single_qubit_gates = dict()
        for idx in range(register_size):
            single_qubit_gates[idx] = []

        # prepare dictionary for two-qubit gates
        two_qubit_gates = list()

        # construct the qgd gate structure            
        Gates_Block_ret = qgd_Gates_Block(register_size)
        optimized_parameters = list()

        for gate in qc.data:

            name = gate[0].name
            if name == 'u3':
                # add u3 gate 
                qubits = gate[1]
                qubit = qubits[0].index
                single_qubit_gates[qubit].append( {'params': gate[0].params, 'type': 'u3'} )

            elif name == 'cz':
                # add cz gate 
                qubits = gate[1]
                two_qubit_gate = {'type': 'cz', 'qubits': [qubits[0].index, qubits[1].index]}

                qubit0 = qubits[0].index
                qubit1 = qubits[1].index

                # creating an instance of the wrapper class qgd_Gates_Block
                Layer = qgd_Gates_Block( register_size )

                # retrive the corresponding single qubit gates and create layer from them
                if len(single_qubit_gates[qubit0])>0:
                    gate0 = single_qubit_gates[qubit0][0]
                    single_qubit_gates[qubit0].pop(0)
                    
                    if gate0['type'] == 'u3':
                        Layer.add_U3( qubit0, True, True, True )
                        params = gate0['params']
                        params.reverse()
                        for param in params:
                            optimized_parameters = optimized_parameters + [float(param)]
                        optimized_parameters[-1] = optimized_parameters[-1]/2                            
                        

                if len(single_qubit_gates[qubit1])>0:
                    gate1 = single_qubit_gates[qubit1][0]
                    single_qubit_gates[qubit1].pop(0)
                    
                    if gate1['type'] == 'u3':
                        Layer.add_U3( qubit1, True, True, True )
                        params = gate1['params']
                        params.reverse()                      
                        for param in params:
                            optimized_parameters = optimized_parameters + [float(param)]
                        optimized_parameters[-1] = optimized_parameters[-1]/2

                ## add cz gate to the layer  
                #Layer.add_CZ( qubit1, qubit0 )

                
                Layer.add_RX( qubit0 )    
                Layer.add_adaptive( qubit0, qubit1 )
                Layer.add_RZ( qubit1 )
                Layer.add_RX( qubit0 )
                optimized_parameters = optimized_parameters + [np.pi/4, np.pi/2, -np.pi/2, -np.pi/4]
                #optimized_parameters = optimized_parameters + [np.pi]

                Gates_Block_ret.add_Gates_Block( Layer )
   
       

        # add remaining single qubit gates
        # creating an instance of the wrapper class qgd_Gates_Block
        Layer = qgd_Gates_Block( register_size )

        for qubit in range(register_size):

            gates = single_qubit_gates[qubit]
            for gate in gates:

                if gate['type'] == 'u3':
                    Layer.add_U3( qubit, True, True, True )
                    params = gate['params']
                    params.reverse()
                    for param in params:
                        optimized_parameters = optimized_parameters + [float(param)]
                    optimized_parameters[-1] = optimized_parameters[-1]/2                        

        Gates_Block_ret.add_Gates_Block( Layer )

        optimized_parameters = np.asarray(optimized_parameters, dtype=np.float64)

        # setting gate structure and optimized initial parameters
        self.set_Gate_Structure(Gates_Block_ret)
        self.set_Optimized_Parameters( optimized_parameters )
          
##
# @brief Call to set custom layers to the gate structure that are intended to be used in the decomposition from a binary file created from SQUANDER
# @param filename String containing the filename
    def set_Gate_Structure_From_Binary( self, filename ):  

        return super(qgd_N_Qubit_Decomposition_adaptive, self).set_Gate_Structure_From_Binary( filename )


##
# @brief Call to add an adaptive layer to the gate structure previously imported gate structure
    def add_Layer_To_Imported_Gate_Structure( self ):  

        return super(qgd_N_Qubit_Decomposition_adaptive, self).add_Layer_To_Imported_Gate_Structure()



##
# @brief Call to set the radius in which randomized parameters are generated around the current minimum duting the optimization process
    def set_Randomized_Radius( self, radius ):  

        return super(qgd_N_Qubit_Decomposition_adaptive, self).set_Randomized_Radius(radius)

##
# @brief Call to append custom layers to the gate structure that are intended to be used in the decomposition from a binary file created from SQUANDER
    def add_Gate_Structure_From_Binary( self, filename ):  

        return super(qgd_N_Qubit_Decomposition_adaptive, self).add_Gate_Structure_From_Binary( filename )
        
##
# @brief Call to set unitary matrix from a binary file created from SQUANDER
    def set_Unitary_From_Binary( self, filename ):  

        return super(qgd_N_Qubit_Decomposition_adaptive, self).set_Unitary_From_Binary( filename )
 
##
# @brief Call to set unitary matrix from a numpy array
    def set_Unitary( self, Umtx_arr ):  

        return super(qgd_N_Qubit_Decomposition_adaptive, self).set_Unitary( Umtx_arr )
        
##
# @brief Call to get unitary matrix
    def get_Unitary( self ):

        return super(qgd_N_Qubit_Decomposition_adaptive, self).get_Unitary()
        
##
# @brief Call to export unitary matrix to binary file
    def export_Unitary( self, filename ):

        return super(qgd_N_Qubit_Decomposition_adaptive, self).export_Unitary(filename)

##
# @brief Call to get global phase
    def get_Global_Phase( self ):
	
        return super(qgd_N_Qubit_Decomposition_adaptive, self).get_Global_Phase()

##
# @brief Call to set global phase 
    def set_Global_Phase( self, angle ):
	
        return super(qgd_N_Qubit_Decomposition_adaptive, self).set_Global_Phase(angle)
##
# @brief Call to get the name of the SQUANDER project
    def get_Project_Name( self ):
	
        return super(qgd_N_Qubit_Decomposition_adaptive, self).get_Project_Name()

##
# @brief Call to set the name of the SQUANDER project ( recommended format : *new project name*_ ) 
    def set_Project_Name( self, project_name_new ):
	
        return super(qgd_N_Qubit_Decomposition_adaptive, self).set_Project_Name(project_name_new)
##
# @brief Call to apply global phase on Unitary matrix
    def apply_Global_Phase( self ):
	
        return super(qgd_N_Qubit_Decomposition_adaptive, self).apply_Global_Phase()
##
# @brief Call to apply the imported gate structure on the unitary. The transformed unitary is to be decomposed in the calculations, and the imported gate structure is released.
    def apply_Imported_Gate_Structure( self ):  

        return super(qgd_N_Qubit_Decomposition_adaptive, self).apply_Imported_Gate_Structure()

## 
# @brief Call to set the optimizer used in the gate synthesis process
# @param optimizer String indicating the optimizer. Possible values: "BFGS" ,"ADAM", "BFGS2".
    def set_Optimizer( self, optimizer="BFGS" ):

        # Set the optimizer
        super(qgd_N_Qubit_Decomposition_adaptive, self).set_Optimizer(optimizer)  


## 
# @brief Call to set the optimizer used in the gate synthesis process
# @param costfnc Variant of the cost function. Input argument 0 stands for FROBENIUS_NORM, 1 for FROBENIUS_NORM_CORRECTION1, 2 for FROBENIUS_NORM_CORRECTION2
    def set_Cost_Function_Variant( self, costfnc="1" ):

        # Set the optimizer
        super(qgd_N_Qubit_Decomposition_adaptive, self).set_Cost_Function_Variant(costfnc=costfnc)  


## 
# @brief Call to set the threshold value for the count of interations, above which the parameters are randomized if the cost function does not decreases fast enough.
# @param threshold The value of the threshold
    def set_Iteration_Threshold_of_Randomization( self, threshold=2500 ):

        # Set the optimizer
        super(qgd_N_Qubit_Decomposition_adaptive, self).set_Iteration_Threshold_of_Randomization(threshold)  


