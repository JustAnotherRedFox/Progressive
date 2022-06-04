#include <iostream>
#include <string>
#include <memory>
//#include "class.h"
//#include "smartPointer.h"
#include "copyingConstructor.h"

int main() {
	/*
	Entity obj(1.5f, 2.1f);
	obj.callMembers();
	Object* al = new Object;
	
	{
		SmartPtr et = new Object();
	}
	*/
	String phrase = "a good afternoon";
	String name = phrase;

	name[2] = '_';
	std::cout << phrase << std::endl;
	std::cout << name << std::endl;
	
	return 0;
}