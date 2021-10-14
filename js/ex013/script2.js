let Name //declaration or declaracao de variavel
Name = 'john' //assignment or atribuicao de valores
console.log(typeof Name) //leitura do valor

let age, isHuman //agrupamento de declaracao

age = 22
isHuman = true

console.log(Name, age, isHuman) //multiplos argumentos

let data = ['john', 33, true]
console.log(data)

let cadastro = {
    name: "john",      //defininddo um object
    age: 55,
    isHuman: false
}

console.log(`cadastro
nome: ${cadastro.name}
idade: ${cadastro.age}
isHuman: ${cadastro.isHuman}`)  //chamando o object

console.log(cadastro);

let animals = [
    'lion',
    'monkey',                  //definindo um array
    {
        name: 'felicy',
        race: 'cat',
        age: 3
    }
]

console.log(animals[0])         //chamando o array

console.log(animals[2])           //chamando um object dentro de um array

console.log(animals[2].race)    //chamando um valor de um object dentro de um array

