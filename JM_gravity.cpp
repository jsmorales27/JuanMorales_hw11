#include <iostream>
#include <typeinfo>
#include <math.h>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;
#define M 1000
#define G 10

int main (){
	float r0=1000;
	float v=0;
	float dt=0.01;
	float r=r0;
	float t=0;
	while (r>=(0.01*r0)){
		cout<<r<<","<<v<<","<<t<<"\n";
		v=v-(dt*G*M/pow(r,2));
		r=r+(dt*v);
		t=t+dt;
		}
	return 0;
}
