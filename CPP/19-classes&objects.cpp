#include <iostream>
using namespace std;

class Book { //creating a class(that is the template, blueprint or especification of a data type, of the 'book'), the name is usualy capitalized, only has to be defined once
    public:
        string title; //classes has atributes
        string author;
        int pages;
        string published;

};

int main() {
    Book book_horror; //creating an object/using the class(the class is the template, the object is the transformation of this "book" template in a actual "book"), once the "template" is done, can be create infinity number of objects from this "template"
    book_horror.title = "The Wolf Gift"; //assing an value to the atribute "title"
    book_horror.author = "Anne Rice";
    book_horror.pages = 551;
    book_horror.published = "February 14, 2012";

    Book book_scifi;
    book_scifi.title = "All You Need is Kill"; //assing an value to the atribute "title"
    book_scifi.author = "Hiroshi Sakurazaka";
    book_scifi.pages = 230;
    book_scifi.published = "December 18, 2004";

    cout << book_horror.title << endl; //print the title of the object "book_horror"
    cout << book_scifi.title;

    return 0;
}