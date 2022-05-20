#include <iostream>
using namespace std;

int main() {
    int count = 1;

    while(count <= 5) {
        cout << count << endl;
        count++;

    }

    count = 6;

    do {
        cout << count << endl;
        count++;

    } while(count <= 6);

    return 0;
}