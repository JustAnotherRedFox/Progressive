#include <iostream>
using namespace std;

int main() {
    string phrase = "is a new and beautiful day outhere?";
    cout << phrase.length() << endl; //show the number of character in the string
    cout << phrase[0] << endl;
    phrase[34] = '!';
    cout << phrase;
    cout << phrase.find("day", 0); //search the initiate index number of a string or character specified("day"), starting from the specified index("0")
    cout << phrase.substr(13, 9); //will 'grab' the specified idexes of strig 

    return 0;
}