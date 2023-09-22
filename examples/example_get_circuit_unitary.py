# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 14:42:56 2020
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

@author: Peter Rakyta, Ph.D.
"""
## \file example_get_circuit_unitary.py
## \brief Simple example python code demonstrating the basic usage of the Python interface of the Quantum Gate Decomposer package

## [import adaptive]
from squander import N_Qubit_Decomposition_adaptive       
## [import adaptive]

import numpy as np
import random


# The gate stucture created by the adaptive decomposition class reads as:
# [ || U3, U3, ..., U3, || CRY, U3, U3 || CRY, U3, U3 || CRY, U3, U3 || .... ]
# The individual blocks are separated by ||. Each U3 gate has 3 free parameters, the CRY gates have 1 free parameter
# The first qbit_num gates are U3 transformations on each qubit. 
# In the quantum circuit the operations on the unitary Umtx are performed in the following order:
# U3*U3*...*U3 * CRY*U3*U3 * CRY*U3*U3 * CRY*U3*U3 * ... * CRY*U3*U3 * Umtx


# the ratio of nontrivial 2-qubit building blocks
nontrivial_ratio = 0.5

# number of qubits
qbit_num = 3

# matrix size of the unitary
matrix_size = pow(2, qbit_num )

# number of adaptive levels
level = 2


##
# @brief Call to construct random parameter, with limited number of non-trivial adaptive layers
# @param num_of_parameters The number of parameters
def create_randomized_parameters( num_of_parameters ):


    parameters = np.zeros(num_of_parameters)

    # the number of adaptive layers in one level
    num_of_adaptive_layers = qbit_num*(qbit_num-1)
    parameters[0:qbit_num*3] = (2*np.random.rand(qbit_num*3)-1)*2*np.pi

    # the number of nontrivial adaptive layers
    num_nontrivial = int(nontrivial_ratio*num_of_adaptive_layers)


    layer_indices = list(range(num_of_adaptive_layers))

    for idx in range(num_nontrivial):

        # randomly choose an adaptive layer to be nontrivial
        chosen_layer = random.randint(1, len(layer_indices)-1) 
        adaptive_layer_idx = layer_indices[chosen_layer]
        layer_indices.pop( chosen_layer )


        # set the radom parameters of the chosen adaptive layer
        start_idx = qbit_num*3 + (adaptive_layer_idx-1)*7
        end_idx = start_idx + 7
        parameters[start_idx:end_idx] = (2*np.random.rand(7)-1)*2*np.pi
    

    return parameters



# creating a class to decompose the unitary
cDecompose = N_Qubit_Decomposition_adaptive( np.eye(matrix_size), level_limit_max=5, level_limit_min=0 )

# adding decomposing layers to the gat structure
for idx in range(level):
    cDecompose.add_Adaptive_Layers()

cDecompose.add_Finalyzing_Layer_To_Gate_Structure()


# get the number of free parameters
num_of_parameters = cDecompose.get_Parameter_Num()

# create randomized parameters having number of nontrivial adaptive blocks determined by the parameter nontrivial_ratio
parameters = create_randomized_parameters( num_of_parameters )

# getting the unitary corresponding to quantum circuit
unitary = cDecompose.get_Matrix( parameters )

print( parameters )
print( unitary ) 




