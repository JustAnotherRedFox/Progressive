#pragma once
using std::string;

//function declaration
void ternary();
void newKeyword();

//class declaration
class Entity {
private:
	string m_Name;

public:
	Entity() : m_Name("unknown") {}
	Entity(const string& name) : m_Name(name) {}

	const string& GetName() const { return m_Name; }

};

struct Vector2 {
	float x, y;

	Vector2(float X, float Y) : x(X), y(Y) {}

	Vector2 Add(const Vector2& other) const {
		return Vector2(x + other.x, y + other.y);
	}

	Vector2 operator+(const Vector2& other) const {
		return Add(other);
	}

	Vector2 Multiply(const Vector2& other) const {
		return Vector2(x * other.x, y * other.y);
	}

	Vector2 operator*(const Vector2& other) const {
		return Multiply(other);
	}

	bool operator==(const Vector2& other) const {
		return x == other.x && y == other.y;
	}

	bool operator!=(const Vector2& other) const {
		return x != other.x && y != other.y;
	}
};