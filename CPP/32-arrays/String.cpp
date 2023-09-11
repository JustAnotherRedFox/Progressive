#include <iostream>

void Strings() {

	const char* cWay = "A Good"; //is an array of char used on c code to make strings with size of 1 byte, so only accept the english alphabet and number.
	char manualWay[7] = {'A', ' ', 'G', 'o', 'o', 'd', 0}; //the same as above but manualy, the '0' show where the string stops
	std::string newWay = "A Good"; //an new c++ way to use strings

	std::cout << cWay << std::endl;
	std::cout << manualWay << std::endl;
	std::cout << newWay << std::endl;

	strlen(cWay); //use an function to return the size of the char* array
	newWay.size();//return the size of the string using an built-in method inside std::string

	std::cout << sizeof(char) << std::endl;
	std::cout << sizeof(char*) << std::endl;
	std::cout << sizeof(std::string) << std::endl;
}