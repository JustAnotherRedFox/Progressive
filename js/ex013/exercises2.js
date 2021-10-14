let gastosFamiliares = {
    receitas: [400, 2333, 435.3, 335.66],
    despesas:[2223, 22.33, 3435.32]
}

function sum(array) {
    let total = 0;

    for(let value of array) {
        total += value
    }

    return total
}

function calcule() {
    const calculateReceitas = sum(gastosFamiliares.receitas)
    const calculateDespesas = sum(gastosFamiliares.despesas)

    const total = calculateReceitas - calculateDespesas

    const saldopossitive = total >= 0

    let msg = 'saldo negativo'

    if (saldopossitive) {
        msg = 'saldo positivo'
    }

    console.log(`voce tem um ${msg} de: R$${total.toFixed(2).replace('-', '')}`)
}

calcule()
