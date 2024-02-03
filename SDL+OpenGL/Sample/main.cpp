/*======= INCLUDES =======*/
#include <SDL.h>
#include <stdio.h>

/*====== Global Variables =====*/
const int SCREEN_WIDTH = 640;
const int SCREEN_HEIGHT = 480;

//The window to be rendered
SDL_Window* gWindow = NULL;

//The Surface contained by the window
SDL_Surface* gScreenSurface = NULL;

//The Image
SDL_Surface* gHelloWorld = NULL;

/*====== Function Prototyping =====*/
bool init();		//start up SDL and creates window
bool loadMedia();	//loads medias files
void close();		//Free media and shutdown SDL

/*===== Main Funtion =========*/
int main(int argc, char* args[]) {
	
	//Initialize SDL and Creating Window
	if (!init()) {
		printf("Failed To Initialize!");
	}
	else {

		//Load Media
		if (!loadMedia()) {
			printf("Failed To Load Media!");
		}
		else {

			//Main Loop Flag
			bool quit = false;

			//Event Handler
			SDL_Event e;

			//Application Loop || Main Loop || Game Loop
			while (!quit) {
				
				//Handle Events on queue
				while (SDL_PollEvent(&e) != 0) {
					//User Request Exit
					if (e.type == SDL_QUIT) {
						quit = true;
					}
				}

				//Apply the image
				SDL_BlitSurface(gHelloWorld, NULL, gScreenSurface, NULL);

				//Update the surface
				SDL_UpdateWindowSurface(gWindow);
			}


			//Free Resources and Close SDL
			close();

			return 0;
		}
	}
}

bool init() {

	//Initialize SDL
	if (SDL_Init(SDL_INIT_VIDEO) < 0) {
		printf("SDL Couldn't be Initialized! Error: %s\n", SDL_GetError());
		return false;
	}
	else {
		
		//Create Window
		gWindow = SDL_CreateWindow("SDL Tutorial", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, SCREEN_WIDTH, SCREEN_HEIGHT, SDL_WINDOW_SHOWN);
		if (gWindow == NULL) {
			printf("Unable to Create Window!%s\n", SDL_GetError());
			return false;
		}
		else {

			//Get Window Surface
			gScreenSurface = SDL_GetWindowSurface(gWindow);
		}
	}
	return true;
}

bool loadMedia() {
	
	//Load Splash Image
	gHelloWorld = SDL_LoadBMP("../Media/hello_world.bmp");
	if (gHelloWorld == NULL) {
		printf("Unable to load image!%s\n", SDL_GetError());
		return false;
	}

	return true;
}

void close() {
	
	//Dealocate Surface
	SDL_FreeSurface(gHelloWorld);
	gHelloWorld = NULL;

	//Destroy Window and dealucate ScreenSurface
	SDL_DestroyWindow(gWindow);
	gWindow = NULL;

	//Quit SDL Subsystems
	SDL_Quit();
}