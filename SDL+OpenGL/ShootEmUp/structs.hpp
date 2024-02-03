#ifndef __STRUCTS_HPP__
#define __STRUCTS_HPP__

/*======= INCLUDES ======*/
#include "common.hpp"

/*======= OBJECT DEFINITIONS ======*/
typedef struct {
	SDL_Renderer* renderer;
	SDL_Window* window;
} App;

//External Var Declaration
extern App app;

#endif