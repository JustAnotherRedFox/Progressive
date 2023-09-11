function calculate() {
    let number_inp = document.querySelector('input#number')
    let tab = document.querySelector('select#tab')
    
    if (number_inp.value.length == 0) {
        alert('[ERROR] insert a value')
    }
    else {
        let number = Number(number_inp.value)

        if (number <= 0) {
            window.alert('[ERROR] invalid value, number set to 1')
            number = 1
        }
        tab.innerHTML = ''
        for(let count = 1; count <= 10; count++) {
            let item = document.createElement('option')
            item.text = `${number} x ${count} : ${number * count}`
            item.value = `tab${count}`
            tab.appendChild(item)
        }
    }
    
}