//events modules 
const { inherits} = require('util')
const {EventEmitter} = require('events')

function char(name) {
    this.name = name
}

inherits(char, EventEmitter)

const dio = new char('dio');
dio.on('hey!', () => console.log(`but it was me ${dio.name}!`))

console.log('i was specting something interesting')
dio.emit('hey!')
