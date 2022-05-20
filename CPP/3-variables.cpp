#include <iostream>
using namespace std;

int main() {
    //variables must be defined before the first utilization
    //every variable must have a data defined
    int number = 10; //the int data type store numbers or intergens, the variable doesn't need to be fullfilled imediatily
    string name = "john"; //the string data type store a string value
    char grade = 'F'; //capable of store one single character, and use '' not ""
    double Dnumber = 1.5; //capable of store decimal or floating point numbers
    bool isTrue = false; //store data of boolean type, like 'true' and 'false'

    cout << "> ";
    //to take a user input use 'cin' and store in a already defined variable
    cin >>  number;

    cout << "your typed number is: " << number;

    return 0;
}