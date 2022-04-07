#include <iostream>
#include <cctype>

using namespace std;

int main() {
    char menu;
    double number1, number2;

    cout << "Enter a Number :\n>> ";
    cin >> number1;

    cout << "Enter the Second Number:\n>> ";
    cin >> number2;

    cout << "Choose the operation to be made:\n";
    cout << "[+] to Sum\n";
    cout << "[-] to Subtract\n";
    cout << "[*] to Multiplie\n";
    cout << "[/] to divide\n>> ";
    cin >> menu;

    menu = toupper(menu); //convert one the 1st character to upper case
    if (menu == '+') {
        cout << number1 << " + " << number2 << " = " << number1 + number2 << endl;

    } else if (menu == '-') {
        cout << number1 << " - " << number2 << " = " << number1 - number2 << endl;

    } else if (menu == '*') {
        cout << number1 << " x " << number2 << " = " << number1 * number2 << endl;

    } else if (menu == '/') {
        cout << number1 << " / " << number2 << " = " << number1 / number2 << endl;

    } else {
        cout << "you insert an invalid number or operator, please choose again." << endl;
    }



    return 0;
}