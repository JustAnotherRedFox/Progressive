#include <iostream>
using namespace std;

int getGreater(int num1, int num2, int num3) {
    int result;

    if (num1 >= num2 && num1 >= num3) {
        result = num1;

    } else if (num2 >= num1 && num2 >= num3) {
        result = num2;

    } else {
        result = num3;
    }

    return result;
}

int main() {
    bool isMale = true;
    bool isTall = true;

    if (isMale && isTall) { //if the both conditions is true, this block will be executed, '&&' means 'and', '||' means 'or', '!' means 'not'
        cout << "you are a Tall male" << endl;

    } else if (isMale && !isTall) { //if the above condition is false and this condition is true, this block will be executed
        cout << "you are a short male" << endl;

    } else if (!isMale && isTall) { //if the above condition is false and this condition is true, this block will be executed
        cout << "you are tall, but aren't a male" << endl;

    } else { //if all the above conditions is false, this block will be executed 
        cout << "you aren't a tall nor male" << endl;

    }

    cout << "the greatest number is: " << getGreater(2, 2, 3) << endl;
    
    return 0;
}