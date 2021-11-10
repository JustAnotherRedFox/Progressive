console.log('something')

//globals
console.log(__filename)
console.log(__dirname)

//require
const path = require('path')
console.log(path.basename(__filename))

//exports
module.exports = "from my module"

//process
console.log(process)
console.log(process.argv)