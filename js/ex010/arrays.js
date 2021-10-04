let auto = ['a', 'v', 'g', 't', 's']

auto.push('d') 
auto.sort()
console.log(`o vetor e ${auto}`)
console.log(`${auto}`)
console.log('') 

console.log('while')
let count = 0

while (count < auto.length) {
    console.log(`${auto[count]}`)
    count++
}

console.log('finished');
console.log('')
console.log('for')

for (let c = 0; c < auto.length; c++) {
    console.log(`${auto[c]}`)
}

console.log('finished')
console.log('')
console.log('for with in')

for (let c in auto) {
    console.log(`${auto[c]}`)
}

console.log('finish')

let comfirm = auto.indexOf('rr')
if (comfirm == -1) {
    console.log('valor nao encontrado')
}  
else {
    console.log(`o valor e ${comfirm}`)
}
