function factor(n) {
    let fact = 1
    for (let count = n; count > 1; count++) {
        fact += count
    }
    return fact
}

console.log(factor(5))