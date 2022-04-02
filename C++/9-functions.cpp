#include <iostream>
using namespace std;

void greatings() { // a function is a block of code that can be 'called' multiple times
    cout << "hello, whoever is seen this!" << endl;
}

void multipleParameters(string name, int age) { //a function can receive multiple parameters
    cout << name << " you are " << age << " years old?" << endl;
}

void functionWithVariable(string firstName); //to use a function that is after the main function we need to 'declare' it first, before the main function

int main() {
    string firstName; //calling a function

    greatings();
    multipleParameters("john", 19); //calling a function with parameters

    cout << "what is your name?\n >>" << endl;
    cin >> firstName;

    functionWithVariable(firstName); //calling a function with variables

    return 0;
}

void functionWithVariable(string firstName) {
    cout << "your name is: " << firstName << " ?" << endl;
}