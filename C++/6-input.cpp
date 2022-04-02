#include <iostream>
using namespace std;

int main() {
    int age; // declaring a variable
    string name;

    cout << "enter your age.\n>> ";
    cin >> age; // receive a user input for numbers(float and intergen) and characters(char) data types

    cout << "enter your name.\n>> ";
    getline(cin, name); // receive a user input for lines of strings(string) as names or phrases

    //obs: cout(c out) stand for console output
    //obs: cin(c in) stand for console input

    cout << "you are " << name << endl;
    cout << " and you are " << age << " years old";
    
    return 0;
}