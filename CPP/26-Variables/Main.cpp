#include <iostream>

int main() {
	const char* string = "hello world is a wandfull day out there, isn't? my fellow pal";
	std::string phrase = "hello";
	char character = 'A';
	int number = 20;
	float fPoint = 2.52f;
	double dFPoint = 3.159;
	bool confirm = true;

	std::cout << "const char* size: " << sizeof(string)    << " bytes" << std::endl;
	std::cout << "std::string size: " << sizeof(phrase)    << " bytes" << std::endl;
	std::cout << "char        size: " << sizeof(character) << " bytes" << std::endl;
	std::cout << "int         size: " << sizeof(number)    << " bytes" << std::endl;
	std::cout << "float       size: " << sizeof(fPoint)    << " bytes" << std::endl;
	std::cout << "double      size: " << sizeof(dFPoint)   << " bytes" << std::endl;
	std::cout << "bool        size: " << sizeof(confirm)   << " bytes" << std::endl;

	return 0;
}