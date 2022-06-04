#include <iostream>
#include "Header.h"

std::ostream& operator<<(std::ostream& stream, const Vector2& other) { //overloading the operator '<<' to use cout in 'Vector2 result'
	stream << other.x << ", " << other.y;
	return stream;
}

int main() {
	/*ternary operator*/
	//ternary();

	/*stack and heap allocation*/
	//stack frame
	Entity stackAllo; //the fastest way in c++ to instantiate an object, but in the end of the actual scope, in this case the main function the object will be destroid

	//allocate on the heap
	Entity* heapAllo = new Entity("pedro"); //will allocate memory for the 'heapAllo' object and return a pointer to the actual object, will not be destroid until explict told or in the end of the program

	std::cout << stackAllo.GetName() << std::endl;
	std::cout << heapAllo->GetName() << std::endl; //to call an pointer object we have to or direferencing[(*heapAllo).GetName()] or use the '->' operator

	delete heapAllo; //the c++ will not dealocate the memory automaticly with an heap allocation, it has to be done manualy using the keyword 'delete'

	/*operator overloading*/
	Vector2 position(4.0f, 4.0f);
	Vector2 speed(0.5f, 1.5f);
	Vector2 powerUp(1.1f, 1.1f);

	Vector2 result = position.Add(speed.Multiply(powerUp));
	Vector2 result2 = position + speed * powerUp; //same as above but with operator overload

	std::cout << result << std::endl;
	std::cout << result2 << std::endl;

	if (result == result2) {
		std::cout << "equals" << std::endl;
	}
	else if (result != result2) {
		std::cout << "not equals" << std::endl;
	}

	return 0;
}