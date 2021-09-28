var nowtime = new Date();
var time = nowtime.getHours();

console.log(`now is exact ${time} horas`);

if (time < 12) {
    console.log("good morning");

} else if (time <= 18) {
    console.log("good afternoon");

} else {
    console.log("good night");
}