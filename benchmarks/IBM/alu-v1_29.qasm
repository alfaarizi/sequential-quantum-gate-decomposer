OPENQASM 2.0;
include "qelib1.inc";
qreg q[5];
u(pi/2,2.5520266,pi/2) q[2];
u(pi,-3*pi/2,-1.9223267) q[1];
cz q[2],q[1];
u(0,-8.4883095e-09,-4.2267938) q[1];
u(pi/2,-3.622493,-3*pi/2) q[0];
cz q[1],q[0];
u(pi/2,-2.3471589,-pi/2) q[4];
u(pi,-3*pi/2,5.0715597) q[3];
cz q[4],q[3];
u(pi,6.2617501,pi/2) q[3];
u(pi/2,0.10683567,-1.8752941) q[0];
cz q[3],q[0];
u(-6.2355369,5.7285988,2.1604058) q[2];
u(pi/2,0.656807,-0.10683562) q[0];
cz q[2],q[0];
u(9.0159436e-13,3.1119137e-08,-4.2625515) q[3];
u(1.7472098,pi,3.6961358) q[2];
cx q[3],q[2];
u(5*pi/4,-1.5107669e-08,9.2086372e-09) q[2];
cx q[3],q[2];
u(-5.6742007,-0.16903738,-pi) q[2];
u(1.1446345e-09,-1.9775052,4.2278429) q[0];
cz q[2],q[0];
u(-pi,2.1327638,1.2312879) q[3];
u(1.4419172,-0.7932931,5.6203759) q[1];
cx q[3],q[1];
u(1.5393477,1.3714881e-08,6.4416039e-09) q[1];
cx q[3],q[1];
u(-4.71239,-1.9993719,-1.4017589) q[2];
u(2.3340819,-2.3612349,-1.7803821) q[1];
cz q[2],q[1];
u(-1.3241733e-10,-1.3866406,4.868024) q[3];
u(0.76945709,3.0776985,-1.0329346) q[1];
cx q[3],q[1];
u(2.3552058,-1.1030949e-08,-3.9017795e-09) q[1];
cx q[3],q[1];
u(pi/2,-2.5674726,-0.79443372) q[4];
u(1.5275591,1.4454926,-5.5423177) q[1];
cz q[4],q[1];
u(3*pi/4,2.4073026,3.2875747) q[1];
u(pi/2,-2.5148302,5.7322352) q[0];
cz q[1],q[0];
u(-8.4793647e-12,1.2151611,-4.1826457) q[3];
u(pi/2,pi/2,-0.83650622) q[1];
cz q[3],q[1];
u(0,1.0122058e-08,4.3430534) q[4];
u(pi/2,pi/2,1.7294322) q[0];
cx q[4],q[0];
u(-3*pi/4,2.0728642e-08,1.4016678e-08) q[0];
cx q[4],q[0];
u(pi,1.8846128,-1.0368055) q[4];
u(pi/2,pi/2,-pi/4) q[1];
cz q[4],q[1];
u(pi/2,-8.8892469e-08,-3*pi/2) q[0];
u(3*pi/4,pi/2,5.2711544e-09) q[1];
u(-3.1578171e-10,2.4631889e-08,-5.9022582) q[2];
u(4.2676526e-12,3.8692386e-09,-0.62780174) q[3];
u(0,2.4866316e-08,1.210357) q[4];
