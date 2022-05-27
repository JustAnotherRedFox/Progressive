#include <iostream>


int main() {
	const char* string = "hey there!";
	
	int i = 0;
	for (int i = 0; i < strlen(string); i++) {
		std::cout << string[i] << std::endl;
	}
	
	while (true) {

		std::cout << "hey" << std::endl;
		i++;
		if (i > 20) {
			break; //stop or break the loop
		}
	}

	for (int i = 0; i <= 10; i++) {
		if (i % 2 == 0) {
			continue; //jump the current loop
		}

		std::cout << i << std::endl;
	}

	return 0; //will return a value and end a function, all code after it will not be executed
}