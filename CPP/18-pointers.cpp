#include <iostream>
using namespace std;

int main() {

    int age = 19; //creating and assing an value to a variable
    int *pAge = &age; // creating an variable to store a pointer, the name has to have: 1 - asterisk, 2 - lowercase 'p' 3 - capitalize name

    double weigth = 55.2;
    double *pWeight = &weigth;

    string name = "john";
    string *pName = &name;

    cout << &age << endl; //print the physical memory address or pointer of the variable
    cout << &weigth << endl; // print the weight variable pointer
    cout << &name << endl;

    cout << pAge << endl; // print the variable that store the age pointer
    cout << *pAge << endl;// dereferencing a pointer/ grab the value that is storage inside the address

    return 0;
}