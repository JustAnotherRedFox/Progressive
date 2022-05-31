#include <iostream>
//extern int s_variable = 3; //will use a external(from another file) variable
//static int s_var = 1; //will only be seen by the 1 translation unity(this file), the 's_' is a convention name that stand for: static variable
//#define struct class //will overwritten the key-word 'struct' by the key-word 'class'

class Log {		//creating a Log system with classes
	private:
		int m_LogLevel = LogLevelInfo;  //'m_' is a convention that stand for: private class member variable
	
	public:			//is possible to use more than one visibility to organize the code
		const int LogLevelError = 0;
		const int LogLevelWarning = 1;
		const int LogLevelInfo = 2;

	public:
		void SetLevel(int level) {
			m_LogLevel = level;
		}

		void Error(const char* message) {
			if (m_LogLevel >= LogLevelError) {
				std::cout << "[ERROR]: " << message << std::endl;
			}
			
		}

		void Warn(const char* message) {
			if (m_LogLevel >= LogLevelWarning) {
				std::cout << "[WARNING]: " << message << std::endl;
			}
			
		}

		void Info(const char* message) {
			if (m_LogLevel >= LogLevelInfo) {
				std::cout << "[INFO]: " << message << std::endl;
			}
			
		}

};

struct Entity { //struct are 'public:' by default
	int x;
	int y;

	void print() {
		std::cout << x << ", " << y << std::endl;
	}

};

enum NumberGroup { //the enum can be used to create a group of integer variables that increments 1 by 1 if not defined the value
	number1 = 5, number2, number3  //if not defined the var will increase they value in a sequencie of 1 so: number2 == 6, number3 == 7, etc...
};

int main() {
	NumberGroup groupVar = number1; //the variable 'groupVar' store the value of 'number1'   
	if (groupVar == 3) {
		//do something
	}
	
	Log log;  //creating an instance, in other words instanciating the class log
	log.SetLevel(log.LogLevelError);

	log.Warn("information");
	log.Error("information");
	log.Info("informatoin");

	Entity person;
	person.x = 1;
	person.y = 45;

	Entity p2;
	//p2.x = 4; //can exist only one instance of a static data, so 'p2.x' refers as 'Entity::x'


	person.print();
	
	return 0;
}
