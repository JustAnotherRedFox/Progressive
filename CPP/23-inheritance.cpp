#include <iostream>
using namespace std;

class Chef {
    public:
        void makeChicken() {
            cout << "the chef makes chicken" << endl;
        }
        void makeSalad() {
            cout << "the chef makes salas" << endl;
        }
        void makeSpecialDish() {
            cout << "the chef makes BBC ribs" << endl;
        }

};

class ItalianChef : public Chef {
    public:
        void makePasta() {
            cout << "the Italian chef makes pasta" << endl;
        }
        void makeSpecialDish() {
            cout << "the chef makes Spaghetti carbonara" << endl;
        }

};

int main() {
    Chef ordinaryChef;
    ordinaryChef.makeChicken();
    ordinaryChef.makeSpecialDish();

    ItalianChef skilledChef;
    skilledChef.makeChicken();
    skilledChef.makePasta();
    skilledChef.makeSpecialDish();

    return 0;
}