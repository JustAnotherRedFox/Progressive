#include <iostream>

void increment(int* value) {  //recieve the memory address of 'a' in a pointer instead of copy as usualy the parameter do

	(*value)++;  //dereferencing the pointer of 'a' and then altering its value
}

void decrement(int& value) { //recieve the value and creating a referencing instead of copy as usual
	value--; //modify the reference that modify the value stored in 'a'
}

int main() {
	int n = 10;
	increment(&n); //calling the function passing the memory address of 'a'
	decrement(n); //calling the function passing the the variable

	int variable = 1010;
	int* ptrVar = &variable; //pass the memory address to ptr
	*ptrVar = 10;			//change the value stored in the memory address inside the pointer 'ptr', that is the variable 'var'
	std::cout << ptrVar << std::endl;
	std::cout << variable;

	char* buffer = new char[32]; //allocating bytes in memory
	memset(buffer, 6, 32);		 //filling the bytes allocated

	char** pointer = &buffer; //pointer to a pointer

	delete[] buffer;             //deallocating bytes allocated

	int var = 5;      //a variable that store the value 5
	int* ptr = &var;  //a pointer that store the memory address of the variable 'var'
	int& ref = var;   //a reference or alias that referencies the variable 'var', can't be changed, only the value can be modified

	ref = 10;              //the variable 'var' will recieve the value '10', using the alias or reference 'ref'

	int a = 4;
	int b = 10;

	int* refer = &a; //creating an pointer to 'a'
	*refer = 40;     //changing the value stored in 'a'

	refer = &b;		//changing the pointer to 'b'
	*refer = 100;	//changing the value stored in 'b'

	return 0;
}