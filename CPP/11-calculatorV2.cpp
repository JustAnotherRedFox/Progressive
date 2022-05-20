#include <iostream>
#include <cctype>

using namespace std;

int main() {
    char operation;
    double number1, number2, result;

    cout << "Enter a Number :\n>> ";
    cin >> number1;

    cout << "Enter the Second Number:\n>> ";
    cin >> number2;

    cout << "Choose the operation to be made:\n";
    cout << "[+] to Sum\n";
    cout << "[-] to Subtract\n";
    cout << "[*] to Multiplie\n";
    cout << "[/] to divide\n>> ";
    cin >> operation;

    operation = toupper(operation); //convert one the 1st character to upper case
    if (operation == '+') {
        result = number1 + number2;

    } else if (operation == '-') {
        result = number1 - number2;

    } else if (operation == '*') {
        result = number1 * number2;

    } else if (operation == '/') {
        result = number1 / number2;

    } else {
        cout << "you insert an invalid number or operation, please choose again." << endl;
    }

    cout << number1 << " " << operation << " " << number2 << " = " << result << endl;

    return 0;
}