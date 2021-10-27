const element = document.getElementsByTagName('h1')

element.InnerText = " hello"

console.log(element)

const div = document.createElement('div')
div.innerText = "hello there"

const body = document.querySelector('body')
const header = body.querySelector('header')

body.insertBefore(div, header.nextSibling)

