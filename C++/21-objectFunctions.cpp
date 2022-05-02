#include <iostream>
using namespace std;

class Student {
    public:
        string name;
        string major;
        double gpa;

        Student(string aName, string aMajor, double aGpa) {
            name = aName;
            major = aMajor;
            gpa = aGpa;

        }

        string hasHonors(){
            if(gpa >= 5.0){
                return "does has honors";
            }
            return "doesn't has honors";
        }

};

int main() {
    Student studentA("jin", "Art", 2.6);
    Student studentB("melisa", "Bussiness", 20.0);

    cout << studentA.name << endl;
    cout << studentA.hasHonors() << endl;
    
    for(int c = 0; c <= 20; c++){
        cout << "-";
        if (c == 20){
            cout << endl;
        }
    }

    cout << studentB.name << endl;
    cout << studentB.hasHonors(); //0 = false, 1 = true

    return 0;
}