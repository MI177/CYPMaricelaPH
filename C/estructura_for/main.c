#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char *argv[]) {
	int i;
	int j;
	for(i=1;i<12;i+=2){  //for in range 
		printf("Hola %d\n",i);
	}
	
	for(i=0;i<5;i+=1){
	
		for(j=0;j<10;j+=1){
			if (j==0||j==9 || i==0||i==4)
				printf("#");
			else
				printf(" ");
				
			
		
		}
		printf("\n");	
	}
	return 0;
}

/* #####
   ####
   ###
   ##
   #
   
   #####
    ####
     ###
      ##
       #
    
    #
    ##
    ###
    ####
*/


