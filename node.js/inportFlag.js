const getFlagValue = require('./ex/Flag')

console.log(`hi, ${getFlagValue('--name')}. ${getFlagValue('--greeting')}`)