# Quantum Gate Decomposer

Quantum Gate Decomposer is an optimization method to decompose an arbitrary NxN Unitary matrix into a sequence of U3 and CNOT gates. 
The algorithm implemented in the code decomposes a given unitary into an identity matrix. 
In order to get the decomposition of a unitary into U3 and CNOT gates instead of operation chain transforming it to unity, one should give the complex transpose of the unitary as the input for the decomposition.

## Dependencies

Quantum Gate Decomposer was developed and tested with Python 3.6 and 3.7
Quantum Gate Decomposer needs the following packages to be installed on the system:

* [Qiskit](https://qiskit.org/documentation/install.html)
* [Numpy](https://numpy.org/install/)
* [optimparallel](https://pypi.org/project/optimparallel/)
* [scipy](https://www.scipy.org/install.html)


## How to use

The usage of the decomposer is demonstrated in test files in the file **test/decomposition.py**. The file contains several examples to calculate the decomposition of two, three and four qubit unitaries. The test examples can be run by the file ** run_tests.py** in the main directory with command:

*$ python3 run_tests.py*

### Two-qubit decomposition
For the decomposition of two-qubit unitaries use class **decomposition/Two_Qubit_Decomposition.py**. The class can be initialized with the following input parameters:

* *Umtx* The unitary matrix to be decomposed. (In order to get the decomposition of a unitary into U3 and CNOT gates instead of operation chain transforming it to unity, one should give the complex transpose of the unitary as the input for the decomposition.)
* *optimize_layer_num* Optional logical value. If true, then the optimalization tries to determine the lowest number of the operation layers needed for the decomposition. If False (default), the optimalization is performed for the maximal number of layers. (each operation layers consists of 0,1,2,3 CNOT gates and several U3 gates)
* *parallel* Optional logical value. If true, parallelized optimalization is used in the decomposition. The parallelized optimalization is efficient if the number of blocks optimized in one shot (given by attribute *optimalization_block*) is at least 10). For False (default) sequential optimalization is applied.
* *method* Optional string value labeling the optimalization method used in the calculations. Deafult is 'L-BFGS-B'. For details see https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html#scipy.optimize.minimize
* *initial_guess* String indicating the method to guess initial values for the optimalization. Possible values: 'zeros' (deafult),'random'

The decomposition of the unitary can be start with the method

*Two_Qubit_Decomposition.start_decomposition()*

The decomposition can be retrived in a Qiskit compatible form using method

*Two_Qubit_Decomposition.get_quantum_circuit()*

The method returns with a [quantum circuit](https://qiskit.org/documentation/apidoc/circuit.html) defined in the framework of the Qiskit package.

### N-qubit decomposition
For the decomposition of N-qubit unitaries use class **decomposition/N_Qubit_Decomposition.py**. The class can be initialized with the following input parameters:

* *Umtx* The unitary matrix to be decomposed. (In order to get the decomposition of a unitary into U3 and CNOT gates instead of operation chain transforming it to unity, one should give the complex transpose of the unitary as the input for the decomposition.)
* *optimize_layer_num* Optional logical value. If true, then the optimalization tries to determine the lowest number of the operation layers needed for the decomposition. If False (default), the optimalization is performed for the maximal number of layers. (each operation layers consists of 0,1,2,3 CNOT gates and several U3 gates)
* *parallel* Optional logical value. If true, parallelized optimalization is used in the decomposition. The parallelized optimalization is efficient if the number of blocks optimized in one shot (given by attribute *optimalization_block*) is at least 10). For False (default) sequential optimalization is applied.
* *method* Optional string value labeling the optimalization method used in the calculations. Deafult is 'L-BFGS-B'. For details see https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html#scipy.optimize.minimize
* *initial_guess* String indicating the method to guess initial values for the optimalization. Possible values: 'zeros' (deafult),'random'
* *identical_blocks* A dictionary of the form {'n': integer} indicating that how many CNOT gates should be included in one layer during the disentanglement of the n-th qubit from the others
* *iteration_loops* A dictionary {'n': integer} giving the number of optimalization subloops done for each step in the optimalization process. (For general matrices 1 works fine, higher value increase both the convergence tendency, but also the running time.)

The decomposition of the unitary can be start with the method

*N_Qubit_Decomposition.start_decomposition()*

The decomposition can be retrived in a Qiskit compatible form using method

*N_Qubit_Decomposition.get_quantum_circuit()*

The method returns with a [quantum circuit](https://qiskit.org/documentation/apidoc/circuit.html) defined in the framework of the Qiskit package.
