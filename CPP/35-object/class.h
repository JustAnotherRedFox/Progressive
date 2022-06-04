#pragma once

class Entity {
public:
	float x, y;

	Entity(float x, float y) {
		this->x = x; //the -> operator direferencies the pointer 'this', so we can change the value stored in x
		this->y = y; 
		
	}

	void callMembers() {
		std::cout << x << std::endl;
		std::cout << this->y << std::endl;
	}

};