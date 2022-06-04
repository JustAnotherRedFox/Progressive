#pragma once

class String {
private:
	char* m_Buffer;
	unsigned int m_Size;

public:
	String(const char* string) {
		m_Size = strlen(string);
		m_Buffer = new char[m_Size + 1]; //adding an space for the null terminator character
		memcpy(m_Buffer, string, m_Size); //will copy the data from m_Buffer to string, with the size in bytes of m_Size(considering wich char = 1byte
		m_Buffer[m_Size] = 0; //adding the null terminator character
	}

	String(const String& other) : m_Size(other.m_Size) { //this is a copy constructor{ className(const ClassName& varName) }, it will be called when a copy hapen to the instancieded object
		//creating a deep copy to copie not the shallow object, but the values inside the object(ex.: m_Buffer)
		m_Buffer = new char[m_Size + 1];
		memcpy(m_Buffer, other.m_Buffer, m_Size + 1);
	}
	~String() {
		delete[] m_Buffer;
	}

	char& operator[](unsigned int index) {
		return m_Buffer[index];
	}

	friend std::ostream& operator<<(std::ostream& stream, const String& string); //friend can access the private members of a class

};

std::ostream& operator<<(std::ostream& stream, const String& string) {
	stream << string.m_Buffer;
	return stream;
}
