function loading() {
    var mensage = window.document.getElementById('mensage');
    var photo = window.document.getElementById('photo');
    var time = new Date();
    var nowhours = time.getHours();
    var nowminutes = time.getMinutes();
    
    
    //nowtime = '5'
    mensage.innerHTML = `now is ${nowhours}:${nowminutes} o'clock`;

    if (nowtime >= 0 && nowtime < 12) {
        //morning
        photo.src = 'pictures/morning.png'
        document.bory.style.background = '#1b5761'
    }

    else if (nowtime >= 12 && nowtime <= 18) {
        //everning
        photo.src = 'pictures/everning.png'
        document.body.style.background = '#c3472e' 
    }

    else {
        //night
        photo.src = 'pictures/nightfall.png'
        document.body.style.background = '#313540'
    }
}


