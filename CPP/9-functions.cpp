#include <iostream>
using namespace std;

void greatings() { // a function is a block of code that can be 'called' multiple times
    cout << "hello, whoever is seen this!" << endl;
}

void multipleParameters(string name, int age) { //a function can receive multiple parameters
    cout << name << " you are " << age << " years old?" << endl;
}

double cube(double num) { // a function with return (double)
    double result = num * num * num;
    return result;
}

void functionWithVariable(string firstName); //to use a function that is after the main function we need to 'declare' it first, before the main function

int main() {
    string firstName; //calling a function
    double answer;

    greatings();
    multipleParameters("john", 19); //calling a function with parameters

    cout << "what is your name?\n>>";
    cin >> firstName;

    functionWithVariable(firstName); //calling a function with variables

    answer = cube(3.1); //calling and storing in a varible the return of the function
    cout << answer << endl;

    return 0;
}

void functionWithVariable(string firstName) {
    cout << "your name is: " << firstName << "?" << endl;
}