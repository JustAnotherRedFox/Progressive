#include <iostream>
#include <thread>

void functionThread0(char symbol) {
    for(int c; c < 200; c++) {
        std::cout << symbol;
    }
}

void functionThread1(char symbol) {
    for(int c; c < 200; c++) {
        std::cout << symbol;
    }
}

int main() {
    char symb0 = '0';
    char symb1 = '1';
    std::thread workerThread0(functionThread0, '1');
    std::thread workerThread1(functionThread1, '0');

    return 0;
}