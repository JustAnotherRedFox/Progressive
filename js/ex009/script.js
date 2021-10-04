function calculate() {
    let number_start = document.getElementById('number_start') //window.document.querySelector('input#number_start');
    let number_end = window.document.getElementById('number_end');
    let number_difference = window.document.getElementById('number_difference');
    let result_response = window.document.getElementById('response');

    if (number_start.value.length == 0 || number_end.value.length == 0 || number_difference.value.length == 0 ) {
        alert('[ERROR] missing data')
        result_response.innerHTML = 'impossivel contar!'
    }    
    else {  
            result_response.innerHTML = 'calculando...<br>'
            let first_term = Number.parseInt(number_start.value)
            let end_term = Number.parseInt(number_end.value)
            let commom_difference = Number.parseInt(number_difference.value)
            
            if (commom_difference <= 0) {
                alert('invalid value, razao set to 1')
                commom_difference = 1
            }

            if (first_term < end_term) {
                for (let count = first_term; count <= end_term; count += commom_difference) {
                    result_response.innerHTML += `${count} ➝`
                }
            }
            else {
                for(let count = first_term; count >= end_term; count -= commom_difference) {
                    result_response.innerHTML += `${count} ➝`
                }
            }
            
            result_response.innerHTML += 'fim'

            }

        

    }
