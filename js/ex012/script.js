let number = document.querySelector('input#number')
let list = document.querySelector('select#list')
let response = document.querySelector('div#response')
let valors = []

function isNumber(n) {
    if (Number(n) >= 1 && Number(n) <= 100) {
        return true
    } else {
        return false
    }
}
 
function inList(n, l) {
    if (l.indexOf(Number(n)) != -1) {
        return true
    } else {
        return false
    }
} 

function add_number() {
    if (isNumber(number.value) && !inList(number.value, valors)) {
        valors.push(Number(number.value))
        let item = document.createElement('option')
        item.text = `valor ${number.value} adicionado`
        list.appendChild(item)
        
    } else {
        window.alert('value invalid or already in list');
    }

    number.value = ''
    number.focus() //automatiza o processo de apagar o numero e click
}

function calcule() {
    if (valors.length == 0) {
        window.alert('insert a value first')
    } else {
        let total = valors.length
        let maior = valors[0]
        let menor = valors[0]
        let soma = 0
        let media = 0
        for (let c in valors) {
            soma += valors[c]

            if (valors[c] < menor) 
                menor = valors[c]
            
            if (valors[c] > maior)
                maior = valors[c]
        }
        media = soma / total

        response.innerHTML = ''
        response.innerHTML += `Ao todo ${total} valores foram adicionados</br>`
        response.innerHTML += `O menor valor adicionado foi ${menor}</br>`
        response.innerHTML += `O maior valor adicionado foi ${maior}</br>`
        response.innerHTML += `A soma de todos os valores foi ${soma}</br>`
        response.innerHTML += `A media de todos os valores foi ${media}</br>`
    }
}
    
