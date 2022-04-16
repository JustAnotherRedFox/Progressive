#include <iostream>
using namespace std;

int main() {
	int secretNumber = 7;
	int guess;
	int tryCount = 5;
	bool outOfTry = false;
	
	while (guess != 7 && !outOfTry) {
		
		if (tryCount <= 0) {
			outOfTry = true;
			cout << "Game Over,\nUnfortunely you run out trys" << endl;
			
		} else {
			cout << "\nenter your guess:\n>> ";
			cin >> guess;
		
			if (guess != secretNumber) {
				tryCount--;
				if (tryCount > 0){
					cout << "Game Over,\nWhat a shame you guessed wrong" << endl;
					cout << "You only have left " << tryCount << " atempts" << endl;
				}
				
				
			}
			
		}
		
	}
	
	if (tryCount > 0 && guess == secretNumber) {
		cout << "Congratulation You Win!" << endl;
		
	}
	
	
	
	return 0;
}