#include <iostream>

void function();

class Entity {
private:
	int value = 2;
	mutable int changeble = 0;
public:
	int GetValue() const { //a readonly method, he can't modify the variables, is useful to Getters
		changeble = 2; //the mutable keyword allow us to modify a variable even if the method is const
		return value;
	}

};

void PrintEntity(const Entity& e) {
	std::cout << e.GetValue() << std::endl; //with a const method i can call a const ref and pass through the cout
}

int main() {
	Entity e;
	const char* name1 = "string"; //a char array with 1 byte each character
	const wchar_t* name2 = L"string"; //a wide char that varies between 2 ~ 4 bytes
	const char16_t* name3 = u"string"; //a 2 bytes or 16bits char
	const char32_t* name4 = U"string"; //a 4 bytes or 32bits char

	const char* nameWSpace = R"(line 1  //the 'R' will ignore all scape caracter inclusive the '//' to comments
		line2
		line3)";

	const char* nameWSpace2 = "line1\n"  //the only other way to give space between strings
		"line2\n"
		"line3\n";

	const int MAX_AGE = 90; //define a constant so the variable is unchangeble

	const int* a = new int; //creating a const pointer that allow us reasign the address but not the value stored inside
	int* const b = new int; //that will do the oposite of the above, we can't reasign the address, but we do can change the value inside
	const int* const c = new int; //you can't change anything

	function();

	return 0;
}