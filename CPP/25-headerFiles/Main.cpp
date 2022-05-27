#include <iostream>
#include <string>
#include "FunctionDeclaration.h"

int main() {
	std::string name;
	std::cout << "what is your name?\n>> ";
	std::getline(std::cin, name);

	Log("Hey There,", name);
	

	return 0;
}