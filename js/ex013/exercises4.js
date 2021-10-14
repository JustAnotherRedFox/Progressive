const booksByCategory = [
    {
        category: 'riqueza',
        books: [
            {
                title: 'os segredos da mente milionaria',
                author: 'T. harv eker',
            },
            {
                title: 'o homem mais rico da babilonia',
                author: 'george S. clason',
            },
            {
                title: 'pai rico, pai pobre',
                author: 'robert T. kiyosaki e sharon L. lechter',
            },
        ],
    },
    {
        category: 'inteligencia emocional',
        books: [
            {
                title: 'voce e insubstituivel',
                author: 'augusto cury',
            },
            {
                title: 'ansiedade - como enfrentar o mal do seculo',
                author: 'augusto cury',
            },
            {
                title: 'os 7 habitos de pessoas altamente eficazes',
                author: 'stephen R. covey',
            },
        ],
    },
];


let totalCategories = booksByCategory.length;
console.log('total de categorias:', totalCategories)

for (let category of booksByCategory) {
    console.log('total de livros da categoria:', category.category)
    console.log(category.books.length)
}

function countAuthors() {
    let authors = [];

    for(let category of booksByCategory) {
        for(let book of category.books) {
            if(authors.indexOf(book.author) == -1) {
                authors.push(book.author)
            }
        }
    }

    console.log('total de autores:', authors.length)
}

countAuthors();

function booksOfAuthor(author) {
    let books = [];

    for(let category of booksByCategory) {
        for(let book of category.books) {
            if(book.author === author) {
                books.push(book.title)
            }
        }
    }

    console.log(`livros do autor ${author}: ${books.join(', ')}`)
}

booksOfAuthor('augusto cury');