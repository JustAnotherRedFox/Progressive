const {EventEmitter} = require('events')

const ev = new EventEmitter()

//listening events
ev.on('something' ,(msg) => {
    console.log("i'm linstening,", msg)
})

//listening events only once
ev.once('something', (msg) => {
    console.log("i listed,", msg)
})

//emiting events
ev.emit('something', 'here')
ev.emit('something', 'there')
ev.emit('something', 'outhere')

