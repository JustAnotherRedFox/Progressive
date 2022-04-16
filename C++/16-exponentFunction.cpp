#include <iostream>
using namespace std;

int power(int baseNum, int powNum) {
    int result = 1;

    for (int i = 0; i < powNum; i++){
        result = result * baseNum;

    }

    return result;
}

int main() {
    int powerNumber, baseNumber, answer;

    cout << "enter the number: \n>> ";
    cin >> baseNumber;

    cout << "enter the power number: \n>> ";
    cin >> powerNumber;

    answer = power(baseNumber, powerNumber);
    cout << "The result is: " << answer << endl;

    return 0;
}