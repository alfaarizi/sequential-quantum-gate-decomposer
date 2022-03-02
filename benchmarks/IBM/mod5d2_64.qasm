OPENQASM 2.0;
include "qelib1.inc";
qreg q[5];
u(pi/2,4.0964244,3*pi/4) q[1];
u(pi/2,-4.1232222,-3.4036926e-09) q[0];
cz q[1],q[0];
u(-pi,2.4369642,3.8992694) q[2];
u(3*pi/4,-1.2410256,-2.5256281) q[1];
cz q[2],q[1];
u(pi/2,2.5288463,0.23359642) q[3];
u(pi,-pi,2*pi) q[0];
cz q[3],q[0];
u(pi/2,3.9506119,3.754339) q[3];
u(pi/2,-pi/2,4.6038979) q[2];
cz q[3],q[2];
u(pi/2,-1.4261022,1.5471752) q[3];
u(pi,-pi,2*pi) q[0];
cz q[3],q[0];
u(pi,0.57695166,-6.1794719) q[4];
u(pi/2,-3.1416021,pi) q[2];
cz q[4],q[2];
u(3*pi/4,3.1920477,9.5867237e-06) q[2];
u(pi,-2.9054526,3.3777328) q[0];
cz q[2],q[0];
u(-pi,-1.6016062,-1.3003906) q[4];
u(2.1536154,1.9268396e-09,0.11000943) q[1];
cx q[4],q[1];
u(1.9732941,-4.4159496e-09,-4.8510115e-09) q[1];
cx q[4],q[1];
u(5.4090377,4.8557785,0.98666502) q[1];
u(pi,-3*pi/2,2.1599631) q[0];
cz q[1],q[0];
u(pi,2.5467387,4.1933944) q[4];
u(3*pi/4,0.48887572,6.2327303) q[2];
cz q[4],q[2];
u(0,-1.372474e-08,2.5358887) q[4];
u(pi/2,-0.69426691,-2.4846641) q[1];
cx q[4],q[1];
u(1.9732941,-1.4111884e-08,-1.7710088e-08) q[1];
cx q[4],q[1];
u(-3*pi,4.2085424,-1.6643793) q[4];
u(1.0189946,3.9881721e-09,-0.14469411) q[3];
cz q[4],q[3];
u(pi/2,-pi,pi/2) q[0];
u(pi/2,-3.2905567e-08,-5.8434051) q[1];
u(pi/2,pi/2,4.2235132) q[2];
u(pi/2,-6.9172888e-09,3*pi/2) q[3];
u(pi,-1.372474e-08,-1.0676422) q[4];
