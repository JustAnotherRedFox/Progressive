
function getScore(nota) {
    let notaF = nota < 60  && nota >= 0;
    let notaD = nota >= 60 && nota <= 69;
    let notaC = nota >= 70 && nota <= 79;
    let notaB = nota >= 80 && nota <= 89;
    let notaA = nota >= 90 && nota <= 100;

    let score;

    if (notaF) {
        score = 'nota F'
    } else if (notaD) {
        score = 'notaD'
    } else if (notaC) {
        score = 'notaC'
    } else if (notaB) {
        score = 'notaB'
    } else if (notaA) {
        score = 'notaA'
    } else {
        score = 'notas maiores que 100 ou menores que 0 nao permitidas'
    }

    return score
}

console.log(getScore(55))