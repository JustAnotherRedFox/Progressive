#include <iostream>

void ternary() {
	int speed = 2;
	int level = 3;

	if (level < 5) {
		speed = 5;
	}
	else {
		speed = 10;
	}

	speed = level < 5 ? 5 : 10; //same as the if statement above, is recomended to use wen there is no nest statement

	int rank = level > 10 ? 15 : // an exemple of a nested condition with ternary operator
			   level >  5 ? 10 :
					    	 5 ;

	std::cout << speed << std::endl;

}