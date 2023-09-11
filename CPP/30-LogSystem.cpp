#include <iostream>

class Log {		//creating a Log system with classes

	public:			//is possible to use more than one visibility to organize the code
		enum Level {
			LevelError = 0, LevelWarning, LevelInfo  //the '= 0' is not necessary but helps in readability
		};

	private:
		Level m_LogLevel = LevelInfo;  //'m_' is a convention that stand for: private class member variable

	public:
		void SetLevel(Level level) {
			m_LogLevel = level;
		}

		void Error(const char* message) {
			if (m_LogLevel >= LevelError) {
				std::cout << "[ERROR]: " << message << std::endl;
			}

		}

		void Warn(const char* message) { //a function inside a class is called method
			if (m_LogLevel >= LevelWarning) {
				std::cout << "[WARNING]: " << message << std::endl;
			}

		}

		void Info(const char* message) {
			if (m_LogLevel >= LevelInfo) {
				std::cout << "[INFO]: " << message << std::endl;
			}

		}
		
		Log(){ //this is a construct function, a function that is called wen a class is instancieted
			std::cout << "class created" << std::endl;
		}
		
		~Log() { //this is a desconstruct function, a function that is called wen a class is destroyed
			std::cout << "class destructed" << std::endl;
			
		}

};

int main() {
	Log log;

	log.SetLevel(Log::LevelError);
	log.Warn("saying");

	return 0;
}