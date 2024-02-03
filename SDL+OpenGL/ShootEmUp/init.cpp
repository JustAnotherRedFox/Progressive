#include "init.h"
#include "common.hpp"
#include "structs.hpp"
#include "defs.hpp"
#include <stdio.h>

void initSDL() {

	//SDL Renderer Flags
	int rendererFlags = SDL_RENDERER_ACCELERATED;

	//SDL Window Flags
	int windowFlags = 0;

	//Initiating SDL and SDL Subsystems
	if (SDL_Init(SDL_INIT_VIDEO) < 0) {
		printf("Couldn't Initialize SDL!%s\n", SDL_GetError());
		exit(1);
	}

	//Creating SDL Window
	app.window = SDL_CreateWindow("Shoot'Em Up", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, SCREEN_WIDTH, SCREEN_HEIGHT, windowFlags);
	if (!app.window) {
		printf("Failed to open %d x %d window! Error: %s\n", SCREEN_WIDTH, SCREEN_HEIGHT, SDL_GetError());
		exit(1);
	}

	SDL_SetHint(SDL_HINT_RENDER_SCALE_QUALITY, "linear");

	//Creating SDL Renderer
	app.renderer = SDL_CreateRenderer(app.window, -1, rendererFlags);
	if (!app.renderer) {
		printf("Failed to create Renderer! Error: %s\n", SDL_GetError());
		exit(1);
	}
}

void close() {
	SDL_DestroyRenderer(app.renderer);
	app.renderer = NULL;

	SDL_DestroyWindow(app.window);
	app.window = NULL;

	//Close SDL Subsystems
	SDL_Quit();
}