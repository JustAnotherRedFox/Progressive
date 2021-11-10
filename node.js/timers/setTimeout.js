//setTimeout ira rodar uma funcao depois de x milisegundos
const timeOut = 3000
const finished = () => console.log('done!')

setTimeout(finished, timeOut)
//por ser assincrono o fonished ira ser executado depois do timeOut, e nao ira atrasar ou blockear a execucao do codigo abaixo
let timer = setTimeout(finished, timeOut)
clearTimeout(timer)

console.log('show')