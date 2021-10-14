

function transformDegree(degree) {
    const celsiusExist = degree.toUpperCase().includes('C')
    const fahrenheitExist = degree.toUpperCase().includes('F')

    //error Flux
    if(!celsiusExist && !fahrenheitExist) {
        throw new Error('Degree not indentified')
    }

    //ideal Flux, F -> C
    let newDegree = Number(degree.toUpperCase().replace('F', ''));
    let formula = (fahrenheit) => (fahrenheit - 32) * 5/9
    let degreeSign = 'C'

    //alternative Flux, C -> F
    if(celsiusExist) {
        newDegree = Number(degree.toUpperCase().replace('C', ''))
        formula = celsius => celsius * 9/5 + 32
        degreeSign = 'F'
    }

    return formula(newDegree) + degreeSign
}

try {
    console.log(transformDegree('50F'))
} catch (error) {
    console.log(error.message)
}
