#pragma once

class Object {
public:
	Object() {
		std::cout << "object created" << std::endl;

	}

	~Object() {
		std::cout << "object Destroid" << std::endl;
	}
};

class SmartPtr {
private:
	Object* m_ptr;

public:
	SmartPtr(Object* ptr) : m_ptr(ptr) {}

	~SmartPtr() {
		delete m_ptr;
	}
};

void smartPointers() {
	//smart pointers as able to automatic delete the pointer allocated on heap
	std::unique_ptr<Entity> uniqueEntity = std::make_unique<Entity>();//the unique smart pointer only accept one pointer and desallow pass the pointer as argument as parameter or coping
	{
		std::shared_ptr<Entity> sharedEntity = std::make_shared<Entity>();//the shared smart pointer allow the pointer to be copied, using the total number of pointer as reference

	}

}