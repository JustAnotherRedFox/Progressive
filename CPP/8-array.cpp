#include <iostream>
using namespace std;

int main() {
    int numberArray[] = {1, 4, 22, 2, 233}; //declaring a array
    int inputArray[20]; //declaring an array to be fullfill later

    inputArray[2] = 33; //fullfiling an empty array
    cout << inputArray[2] << endl;

    numberArray[0] = 88; //modifing a element in a array
    cout << numberArray[0] << endl; //acessing the elements in a array

    return 0;
}