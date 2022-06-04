#include <iostream>

void newKeyword() {
	int* heapInt = new int; //allocate on the heap the value of int(4 bytes) and pass the memory address to the pointer heapInt
	int* heapArray = new int[50]; //allocate on the heap the value of int array of 50(200 bytes)

	//entity* heapEntity = new Entity(); will not only allocate memory like the 'malloc()' but also call the constructor

	delete heapInt;//the delete use a similar to 'free()' and alse call the destructor
	delete[] heapArray; //delete a array

}
