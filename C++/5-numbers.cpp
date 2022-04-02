#include <iostream> //to use i/o funcions
#include <cmath> //to use math functions

using namespace std;

int main() {
    int intergenNumber = 5;     //storing an intergen number
    double floatNumber = 3.1;   //storing an float number

    cout << intergenNumber / floatNumber << endl;       //division
    cout << intergenNumber + floatNumber << endl;       //sum
    cout << intergenNumber - floatNumber << endl;       //subtraction
    cout << intergenNumber * floatNumber << endl;       //multiplier
    cout << intergenNumber % intergenNumber << endl;    //modulo 

    cout << intergenNumber++ << endl;   //increment on 1
    cout << intergenNumber-- << endl;   //decrement on 1
    intergenNumber += 20;       //same as intergenNumber = intergenNumber + 20
    intergenNumber -= 20;       //same as intergenNumber = intergenNumber - 20
    intergenNumber /= 20;       //same as intergenNumber = intergenNumber / 20
    intergenNumber *= 20;       //same as intergenNumber = intergenNumber * 20
    cout << intergenNumber << endl;

    /*precedence order: 
    1- ()
    2- *, /, %
    3- +, -

    obs. math with intergen aways return an intergen. ex.: 10 / 3 == 3
    obs. math with float point aways return an float point. ex.: 1.0 + 6 == 7.0
    */

   //using cmath
   cout << pow(2, 6) << endl;   //power or 2^6
   cout << sqrt(9) << endl;     //square root
   cout << round(2.6) << endl;  //round a number
   cout << ceil(2.1) << endl;   //round a number up
   cout << floor(9.1) << endl;  //round a number down
   cout << fmax(2, 9) << endl;  //return the bigger number
   cout << fmin(2, 1) << endl;  //return the smaller number

    return 0;
}