#include <iostream>
using namespace std;

//2Dimencional array is an array with an array in it

int main() {
    int numberGrid[3/*number total of elements*/][2/*number of element of the array inside the array*/] = {
        {2/*index 0*/, 5/*index 1*/}, //index 0
        {4/*index 0*/, 1/*index 1*/}, //index 1
        {3/*index 0*/, 6/*index 1*/}  //index 2

        
    };

    cout << numberGrid[1][0];
    return 0;
}