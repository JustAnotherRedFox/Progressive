#include <iostream>
#include <array>

void Strings();

int main() {
	const int exempleSize = 7;
	int exemple[exempleSize];

	for (int i = 0; i < exempleSize; i++) {
		exemple[i] = 0;
	}

	for (int i = 0; i < exempleSize; i++) {
		std::cout << exemple[i] << std::endl;
	}

	std::array <int, 4> another; //a more modern way to initialize an array
	for (int i = 0; i < another.size(); i++) {  //a more correct way to reach the array size
		another[i] = 0;
	}

	Strings();

	return 0;
}