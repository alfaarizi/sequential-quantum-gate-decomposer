/*
Created on Fri Jun 26 14:13:26 2020
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
*/
/*! \file Adaptive.h
    \brief Header file for a class representing a gate used in adaptive decomposition.
*/

#ifndef ADAPTIVE_H
#define ADAPTIVE_H

#include "CRY.h"
#include "matrix.h"
#include "matrix_real.h"
#define _USE_MATH_DEFINES
#include <math.h>


/**
@brief A class representing a CRY gate.
*/
class Adaptive: public CRY {


public:

protected:
    ///
    int limit;


public:

/**
@brief Nullary constructor of the class.
*/
Adaptive();


/**
@brief Constructor of the class.
@param qbit_num_in The number of qubits spanning the gate.
@param target_qbit_in The 0<=ID<qbit_num of the target qubit.
@param theta_in logical value indicating whether the matrix creation takes an argument theta.
@param phi_in logical value indicating whether the matrix creation takes an argument phi
@param lambda_in logical value indicating whether the matrix creation takes an argument lambda
*/
Adaptive(int qbit_num_in, int target_qbit_in, int control_qbit_in);


/**
@brief Constructor of the class.
@param qbit_num_in The number of qubits spanning the gate.
@param target_qbit_in The 0<=ID<qbit_num of the target qubit.
@param theta_in logical value indicating whether the matrix creation takes an argument theta.
@param phi_in logical value indicating whether the matrix creation takes an argument phi
@param lambda_in logical value indicating whether the matrix creation takes an argument lambda
*/
Adaptive(int qbit_num_in, int target_qbit_in, int control_qbit_in, int limit_in);

/**
@brief Destructor of the class
*/
~Adaptive();

/**
@brief Call to retrieve the gate matrix
@param parameters An array of parameters to calculate the matrix of the U3 gate.
@return Returns with a matrix of the gate
*/
//Matrix get_matrix( const double* parameters );

/**
@brief ???????????????
*/
std::vector<Matrix> apply_derivate_to( Matrix_real& parameters, Matrix& input );



/**
@brief Call to apply the gate on the input array/matrix by U3*input
@param parameters An array of parameters to calculate the matrix of the U3 gate.
@param input The input array on which the gate is applied
*/
virtual void apply_to( Matrix_real& parameters, Matrix& input );


/**
@brief Call to apply the gate on the input array/matrix by input*U3
@param parameters An array of parameters to calculate the matrix of the U3 gate.
@param input The input array on which the gate is applied
*/
void apply_from_right( Matrix_real& parameters, Matrix& input );


/**
@brief ???????????
*/
void set_limit( int limit_in );


/**
@brief ???????????
*/
int get_limit();


/**
@brief Call to create a clone of the present class
@return Return with a pointer pointing to the cloned object
*/
Adaptive* clone();

};


#endif //Adaptive

