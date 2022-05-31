#include <iostream>

class Person {
private:
	std::string m_Name;
	int m_Score;

public:
	Person() : m_Name("unknown"), m_Score(10) { //will initializer the variable so the code bellow is unecessary, the inializer has to be made in the same order of the declaration
		//m_Name = "unknown";
	}

	Person(const std::string& name, const int& score) : m_Name(name), m_Score(score) {//member initialize list
		//m_Name = name;
	}

	void CallName() {
		std::cout << m_Name << std::endl;
		std::cout << m_Score << std::endl;
	}
};

void function() {
	Person john("john", 0);
	Person adrian;
	john.CallName();
	adrian.CallName();

}