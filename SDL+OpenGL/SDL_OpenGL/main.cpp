#include "defs.hpp"
#include <SDL.h>
#include <stdio.h>
#include <glad/glad.h>

/*======= Global Variables ======*/
SDL_Window* gWindow = nullptr;
SDL_GLContext gGLContext = nullptr;

void getGLInfo() {
	printf("========= OpenGL Info ==========\n---------------------------\n");
	printf("Vendor: %s\n", glGetString(GL_VENDOR));
	printf("Renderer: %s\n", glGetString(GL_RENDERER));
	printf("Version: %s\n", glGetString(GL_VERSION));
	printf("Shading Language Version: %s\n", glGetString(GL_SHADING_LANGUAGE_VERSION));
}

void init() {

	//Initiation SDL and SDL Subsystems
	if (SDL_Init(SDL_INIT_VIDEO) < 0) {
		printf("Failed to Initialize SDL! Error: %s\n", SDL_GetError());
		exit(1);
	}

	//Setting SDL_OpenGL Context Attributes
	SDL_GL_SetAttribute(SDL_GL_CONTEXT_MAJOR_VERSION, 4);
	SDL_GL_SetAttribute(SDL_GL_CONTEXT_MINOR_VERSION, 1); //To Test GPU Suport only version 4.0, try: 4.0 or 3.3
	SDL_GL_SetAttribute(SDL_GL_CONTEXT_PROFILE_MASK, SDL_GL_CONTEXT_PROFILE_CORE); //Disable all Deprecated(old openGL) functionalities
	SDL_GL_SetAttribute(SDL_GL_DOUBLEBUFFER, 1); //Use Double buffer
	SDL_GL_SetAttribute(SDL_GL_DEPTH_SIZE, 24);

	//Creating SDL Window
	gWindow = SDL_CreateWindow("SDL With OpenGL", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, SCREEN_WIDTH, SCREEN_HEIGHT, SDL_WINDOW_OPENGL);
	if (gWindow == nullptr) {
		printf("Unable to Create Window! Error: %s\n", SDL_GetError());
		exit(1);
	}

	//Creating OpenGL Context
	gGLContext = SDL_GL_CreateContext(gWindow);
	if (gGLContext == nullptr) {
		printf("Unable to Create GL Context! %s\n", SDL_GetError());
		exit(1);
	}

	//Initialize Glad Library
	if (!gladLoadGLLoader(SDL_GL_GetProcAddress)) {
		printf("Unable to Initialize Glad Lib!");
		exit(1);
	}

	getGLInfo();
}

void close() {

	//Destroy Window
	SDL_DestroyWindow(gWindow);

	//Quit SDL Subsystems
	SDL_Quit();
}

void handleInput() {
	//Event Handler
	SDL_Event event;

	//Handle Event On Queue
	while (SDL_PollEvent(&event) != 0) {
		switch (event.type) {

			//User Request Exit
			case SDL_QUIT:
				printf("Application Exited Successfuly!");
				exit(0);
				break;

			default:
				break;
		}
	}
}

void preDraw() {

}

void draw() {

}

int main(int argc, char* args[]) {
	init();

	//Application Loop a.k.a Game Loop a.k.a Main Loop
	while (1) {
		//Handle all Inputs
		handleInput();
		
		//Prepare Scene
		preDraw();

		//Render Scene
		draw();

		//Update the Screen
		SDL_GL_SwapWindow(gWindow);
	}

	close();

	return 0;
}
