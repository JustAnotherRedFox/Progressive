var age = 64;

if (age < 16) {
    console.log("you're a minor, you can't vote");
}

else {
    if (age < 18 || age > 65) {
        console.log("voto opcional")
    } else {
        console.log("voto obrigatorio")
    }
}
