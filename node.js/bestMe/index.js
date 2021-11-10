const questions = [
	'what i do learn today?',
	'what make me upset?',
	'what can i do to make things better?',
	'what make me happier?',
	'how many people i help today?'
]

const ask = (index = 0) => {
	process.stdout.write("\n\n" + questions[index] + " > ")
}

ask()

const answers = []

process.stdin.on("data", data => {
	answers.push( data.toString().trim())
	if (answers.length < questions.length) {
		ask(answers.length)
	} else {
		process.exit()
	}
	
})

process.on('exit' , () => {
	console.log(`
	 ok!

	 what u learn today is:
	 ${answers[0]}

	 what make u upset is:
	 ${answers[1]}

	 what you can do to make things better is:
	 ${answers[2]}

	 what make u happy is:
	 ${answers[3]}

	 you help ${answers[4]} people today!

	 come back tomorrow!
	`)
})