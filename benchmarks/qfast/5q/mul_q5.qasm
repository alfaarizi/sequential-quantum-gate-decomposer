OPENQASM 2.0;
include "qelib1.inc";
qreg q[5];
u(2.9000688e-07,0.03772324,0.8010026) q[3];
u(0.60410775,-pi,1.570795) q[1];
cx q[3],q[1];
u(pi/4,0,0) q[1];
cx q[3],q[1];
u(1.1704401e-10,-1.0196063,-0.71417957) q[4];
u(pi,-3*pi/2,-2.0082473) q[2];
cz q[4],q[2];
u(pi/2,-0.35011364,2.1086373) q[2];
u(pi/2,-3.8265504,pi/2) q[1];
cz q[2],q[1];
u(pi,4.6435451,pi/2) q[1];
u(0,0,-pi/2) q[0];
cz q[1],q[0];
u(-2.0018687e-07,0.97851052,0.057583166) q[3];
u(0.81050248,pi,5.0625042) q[2];
cx q[3],q[2];
u(pi/4,0,0) q[2];
cx q[3],q[2];
u(pi/2,3.9005971,-4.6883291) q[4];
u(1.5456921,1.5370471,-pi) q[2];
cz q[4],q[2];
u(pi/2,-0.25604873,2.3825882) q[4];
u(pi,-3*pi/2,-5.1472123) q[1];
cz q[4],q[1];
u(-3.9870972e-10,0.17836594,1.5267168) q[4];
u(pi/2,-pi/2,0.033750047) q[2];
cz q[4],q[2];
u(pi/2,3.8861195,-4.5906268) q[4];
u(pi/2,pi/2,2.0521713) q[3];
cx q[4],q[3];
u(-pi/4,0,0) q[3];
cx q[4],q[3];
u(0,0,pi/2) q[0];
u(pi/2,pi,3*pi/2) q[1];
u(pi/2,-3.002663,pi/2) q[2];
u(pi/2,0,-pi/2) q[3];
u(-1.6528334e-07,0,1.0161633) q[4];
