#include <iostream>

class Printable {
public:
	virtual std::string GetClassName() = 0;  //a interface or pure virtual function are function that is created as blueprint and only the derived class is who will istanciate
};

class Entity : public Printable{
public:
	virtual std::string GetName() { //an virtual function is a function created to be overrided by it's derived class
		return "Entity";
	}
	std::string GetClassName() override {
		return "Entity";
	}

};

class Player : public Entity {
private:
	std::string m_Name;

public:
	Player(const std::string& name) : m_Name(name) {}

	std::string GetName() override {
		return m_Name; 
	}

	std::string GetClassName() override {
		return "Player";
	}

};

class RandomClass : public Printable{
public:
	std::string GetClassName() override {
		return "RandomClass";
	}
};

void Print(Printable* obj) {
	std::cout << obj->GetClassName() << std::endl;
}

int main() {

	Entity* en = new Entity();
	Player* pl = new Player("hello");
	RandomClass* rc = new RandomClass();

	Print(en);
	Print(pl);
	Print(rc);



	return 0;
}