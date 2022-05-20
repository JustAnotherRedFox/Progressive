#include <iostream>
using namespace std;

class Book {
	public:
		string title;
		int pages;
		string author;
		
		Book() {
			title = "no title";
			author = "no author";
			pages = 0;
		}
		
		Book(string arTitle, string arAuthor, int arPages) { //creating an constructor(that is a special funcition that will be called when we call the class)
			//cout << "the name of the book is " << title << endl; //this line will be executed whenever the function is called
			//we can also use the contructor to inicialize the object: 
			title = arTitle;
			author = arAuthor;
			pages = arPages;
			
		}
	
};

int main() {
	Book adventure_book("Life of Pi", "Yann Martel", 400); //using the contructor tho incialize the object and shortened the code
	Book action_book;
	/*
	Book adventure_book("life of pi");
	adventure_book.title = "life of pi";
	adventure_book.pages = 400;
	adventure_book.author = "Yann Martel";
	*/
	
	cout << adventure_book.author << endl;
	cout << action_book.title << endl;
	
	return 0;
}