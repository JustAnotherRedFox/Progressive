/*========= Includes ==========*/
#include "structs.hpp"
#include "init.h"
#include "input.h"
#include "draw.h"
//#include <stdio.h>		//printf()
//#include <cstring>		    //memset()

/*========= Global Variables ========*/
//External Var Definition
App app;

/*========= Main Function =========*/
int main(int argc, char* args[]) {
	//memset(&app, 0, sizeof(App));

	initSDL();

	while (1) {
		prepareScene();

		handleInput();

		presentScene();

		SDL_Delay(16);
	}

	close();

	return 0;
}