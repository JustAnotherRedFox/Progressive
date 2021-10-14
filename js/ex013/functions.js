function createPhrases() {
    console.log('frase motivaciona1')
    console.log('frase motivaciona2')  //criando funcoes
    console.log('frase motivaciona3')
}

//funcoes dentro de variaveis
const sum = function(n1, n2/*parameters/parametros*/){ //function expression, anonymous/ funcao anonima
    total = n1 + n2 //e possivel definir uma variavel sem uma palavra chave, mas nao e recomendado
    return total
}

//sum(5, 6) //arguments /argumento

let number1 = 23
let number2 = 22

console.log(`o numero 1 e ${number1}`)
console.log(`o numero 1 e ${number2}`)
console.log(`a soma vale ${sum(number1, number2)}`)

//function hoisting

sayMyName()

function sayMyName() {
    console.log('jonh')
}

//arrow function

const SayMyName = (name) => {
    console.log(name)
}

SayMyName('jong')

//callback function

function say_my_name(name) {
    console.log('antes da execucao')
    name()
    console.log('depois da execucao')
}
say_my_name(
    () => {
        console.log('callback')
    }
)

//function() construction

// expressao 'new'
// cria um novo object
// 'this' keyword

function Person(name) {    //recomendado usar nomes captalizados para funcoes construtoras
    this.name = name
    this.walk = function() {
        return this.name + "walking"
    }
}
/*
const person = {      a maneira padrao
    nome: "john",
}
*/
const john = new Person("john")
const mik = new Person("mik")         //uma maneira mais pratica para adicionar objects
console.log(jonh)
console.log(mik.walk())

//prototype
//prototype-based language
//prototype chain
//__proto__

console.log("qwerty".__proto__)

//type conversion(typecasting) vs type coersion
//alteracao de um tipo de dado para autro

console.log('3' + 4)// o 4 ira sofrer uma coersion para string
console.log(Number('5') + 4)//o 5 ira sofrer uma conversion para number

//manipulacao de dados
let string = "423"
let number = 2323
let word = "good afternoon"
let phrase = "the one who fight monsters, be careful to not become a monster"

console.log(Number(string))//transformando uma dado do tipo string em um numerico
console.log(String(number))//transformando um dado numerico em uma string
console.log(word.length)//contando os caracteres de uma string
console.log(String(number).length)//contando os digitos de um numero

number = 232.355466

console.log(number.toFixed(2))//"conserta" o numero definindo o numero de casas decimais convertendo o numero em string
console.log(number.toFixed(2).replace(".", ","))//converte o dubstitue o ponto para virgula
console.log(word.toUpperCase())//converte a string em uppercase ou maiuscula
console.log(word.toLowerCase())//converte a string em lowercase ou minuscula

let phraseArray = phrase.split(' ')//separa a string pelos spacos
console.log(phraseArray)
let phraseUnderscore = phraseArray.join("_")//junta a string separada usando underscore
console.log(phraseUnderscore)

console.log(phrase.includes("MONSTERS"))//verifica se a palavra especificada esta presente na string

let rArray = new Array('2', '43', '4')//criando um array com constructor
console.log(rArray)

console.log([
    "dsf",
    {type: "array"},
    function() { return "end"}  //arrays permitem quebras de linhas e todos os tipos de dados
].length)//contando elementos de um array

let string = "manipulacoao"
console.log(Array.from(string))//transforma uma string em um array

let tech = ['html', 'css', 'js']

console.log(tech.push('node.js'))//adiciona um item no fim do array
console.log(tech.unshift('SQL'))//adiciona um item no inicio do array
console.log(tech.pop())//remove um elemento do fim do array
console.log(tech.shift())//remove um elemento do inicio do array
console.log(tech.slice(1, 3))//ira selecionar elementos especificos do array apartir a (1) possicao e ate o (3) numero de elementos
console.log(tech.splice(1, 2))//remover 1 ou mais elementos em qualquer posicao do array
console.log(tech.indexOf('css'))//seleciona o incice de um elemento