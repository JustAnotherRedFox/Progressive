//expresoes e operadores

/*
- expresions
- operators
    binary
    unary
    ternary
*/
let number = 1

console.log(number + 1)//operador binario
console.log(++number)//operador unario
console.log(true ? 'work' : 'fail')//operador ternario

/*
new
cria um novo objeto
*/

let name = new String('john')
name.surName = "santos"   //adicionado o elemento surName: "santos" ao objeto name
let age = new Number(44)
console.log(name.surName)

/*
operadores unarios
    *typeof
    *delete
*/
const person = {
    name: 'jong',
    age: 33
}

delete person.age  //ira deletar o elemento age do objeto person
console.log(person)

/*
operadores ternarios
condition ? value1 : value2
*/

let pao = true
queijo = true
const niceBreakFast = pao && queijo ? 'cafe top' : 'cafe ruin'
console.log(niceBreakFast)

console.log('a' == 'a')//comparison
console.log('a' + 'a')//concatenation

/*
       -FALSY-
false
0
-0
""
null
undefined
NaN

       -TRUTHY
true
{}
[]
1
3.23
"0"
"false"
-1
Infinity
-Infinity
*/

/*operator precedence
    *grouping                  ()
    *negacao e incremento      ! ++ --
    *multiplicacao e divisao   * /
    *adicao e subtracao        + -
    *relacional                < <= > >=
    *igualdade                 == != === !==
    *AND                       &&
    *OR                        ||
    *condicional               ? :
    *assignment                = += -= *=
*/

//control flow

console.log('lavar copo')        //estrutura sequencial 

console.log('servir o copo')

let temperature = 36.9;
let highTemperature = temperature >= 37.3;
let mediumTemperature = temperature < 37.2 && temperature >= 36.6;
let health = temperature <= 36.5;

if (health) {
    console.log('saudavel')
} else if (highTemperature) {
    console.log('high fever')
} else if (mediumTemperature) {
    console.log('initial fever')
}

//estrutura de repetucao
//for
for (let i = 0; i < 100; i++) {
    console.log(i)
    if (i === 50) {
        break; //para a execucao do loo[]
    }
}

for (let i = 0; i < 10; i++) {
    if (i === 1 || i === 5) {
        continue; //pula a execucao de lupe atual
    }
    console.log(i)
}

//while
let init = 0;
while (init < 10) {
    console.log(init)
    init++;
}

//for...of
let name = 'john';
let names = ['john', 'poul', 'peter']

for (let name of names) {        //ira pegar cada nome dentro de names
    console.log(name)      
}

//for...in
let person = {
    name: 'john',
    age: 23,
    weight: 42.4
}

for(let property in person) {
    console.log(property)
    console.log(person[property])
}