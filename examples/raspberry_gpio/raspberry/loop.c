
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include "wiringPi.h"

int main (void){

	wiringPiSetup();
	int i;
	
	while(1){
	
		for (i=0; i<8; i++) {
		    pinMode(i,OUTPUT);
			sleep(1);
			digitalWrite(i, 1);
			sleep(1);
			digitalWrite(i, 0);
			sleep(1);
			pinMode(i, INPUT);
			sleep(1);
		}
		
	}
}
