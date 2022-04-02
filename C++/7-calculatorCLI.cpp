#include <iostream>
using namespace std;

int main() {
    double number1, number2, sum, sub, divi, multi;

    cout << "enter the first number: \n>> ";
    cin >> number1;

    cout << "enter the second number: \n>> ";
    cin >> number2;

    sum = number1 + number2;
    sub = number1 - number2;
    divi = number1 / number2;
    multi = number1 * number2;

    cout << number1 << " + " << number2 << " = " << sum << endl;
    cout << number1 << " - " << number2 << " = " << sub << endl;
    cout << number1 << " / " << number2 << " = " << divi << endl;
    cout << number1 << " * " << number2 << " = " << multi << endl;

    return 0;
}