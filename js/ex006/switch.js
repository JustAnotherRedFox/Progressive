var nowtime = new Date();
var weekday = nowtime.getDay();

/*
0 - sunday
1 - monday
2 - tuesday
3 - wednesday
4 - thursday
5 - friday
6 - saturday
*/

switch(weekday) {
    case 0:
        console.log("is sunday")
        break
    case 1:
        console.log("is monday")
        break
    case 2:
        console.log("is tuesday")
        break
    case 3:
        console.log("is wednesday")
        break
    case 4:
        console.log("is thursday")
        break
    case 5:
        console.log("is friday")
        break
    case 6:
        console.log("is saturday")
        break
    default:
        console.log("[error], invalid day")
        break
}