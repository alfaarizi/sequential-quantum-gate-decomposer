## #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 15:44:26 2020
Copyright 2020 Peter Rakyta, Ph.D.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

You should have received a copy of the GNU General Public License
along with this program.  If not, see http://www.gnu.org/licenses/.

@author: Peter Rakyta, Ph.D.
"""

## \file qgd_N_Qubit_Decomposition.py
##    \brief A QGD Python interface class for the decomposition of N-qubit unitaries into a set of two-qubit and one-qubit gates.

import numpy as np
from os import path
from qgd_python.decomposition.qgd_N_Qubit_Decomposition_adaptive import qgd_N_Qubit_Decomposition_adaptive

##
# @brief A QGD Python interface class for the decomposition of N-qubit state into U3 and CNOT gates.
class qgd_N_Qubit_State_Preparation_adaptive(qgd_N_Qubit_Decomposition_adaptive):

	def __init__( self, State, level_limit_max=8, level_limit_min=0, topology=None, config={}, accelerator_num=0 ):
		if ( (type(State) == np.ndarray) and (State.shape[1]==1) ):
			super().__init__( State, level_limit_max, level_limit_min, topology=topology, config=config )
			self.config = config
		else:
			raise Exception("Initial state not properly formatted. Input state must be a column vector")





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
		for idx in range(len(gates)):

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
				circuit.u(-gate.get("Theta"), -gate.get("Lambda"), -gate.get("Phi"), gate.get("target_qbit"))

			if gate.get("type") == "CRY":
				# adding CNOT gate to the quantum circuit
				circuit.cry(-gate.get("Theta"), gate.get("control_qbit"), gate.get("target_qbit"))

			elif gate.get("type") == "RX":
				# RX gate
				circuit.rx(-gate.get("Theta"), gate.get("target_qbit"))

			elif gate.get("type") == "RY":
				# RY gate
				circuit.ry(-gate.get("Theta"), gate.get("target_qbit"))

			elif gate.get("type") == "RZ":
				# RZ gate
				circuit.rz(-gate.get("Phi"), gate.get("target_qbit"))

			elif gate.get("type") == "X":
				# X gate
				circuit.x(gate.get("target_qbit"))

			elif gate.get("type") == "SX":
 				# SX gate
				circuit.sx(gate.get("target_qbit"))

		return circuit
	def Start_Decomposition(self):
		if "Optimizer" in self.config:
			super(qgd_N_Qubit_State_Preparation_adaptive, self).set_Optimizer(self.config["Optimizer"])
		if "Cost_function" in self.config:
			super(qgd_N_Qubit_State_Preparation_adaptive, self).set_Cost_Function_Variant(self.config["Cost_function"])
		if ("compression_enabled" not in self.config ) and ("optims" not in self.config):
			super(qgd_N_Qubit_State_Preparation_adaptive, self).Start_Decomposition()
		else:
			if "optims" in self.config:
				for optim in self.config["optims"]:
					super(qgd_N_Qubit_State_Preparation_adaptive, self).set_Optimizer(optim)
					super(qgd_N_Qubit_State_Preparation_adaptive, self).get_Initial_Circuit()
			else:
				super(qgd_N_Qubit_State_Preparation_adaptive, self).get_Initial_Circuit()
			if self.config["compression_enabled"]==1:
				super(qgd_N_Qubit_State_Preparation_adaptive, self).Compress_Circuit()
			super(qgd_N_Qubit_State_Preparation_adaptive, self).Finalize_Circuit()
			

