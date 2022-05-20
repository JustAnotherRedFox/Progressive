#include <iostream>
using namespace std;

string GetWeekDay(int dayNumber) {
    string dayName;

    switch(dayNumber) {
        case 0:
            dayName = "sunday/domingo";
            break;
        
        case 1:
            dayName = "monday/segunda";
            break;

        case 2:
            dayName = "tuesday/terca";
            break;

        case 3:
            dayName = "wednesday/quarta";
            break;

        case 4:
            dayName = "thursday/quinta";
            break;

        case 5:
            dayName = "friday/sexta";
            break; 

        case 6:
            dayName = "saturday/sabado";
            break;

        default:
            dayName = "day Number Invalid";
            break;

    }

    return dayName;
}

int main() {

    cout << GetWeekDay(0);
    return 0;
}