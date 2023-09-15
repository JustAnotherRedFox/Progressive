function toggleMode() {
	const html = document.documentElement;
	html.classList.toggle('light'); //if in classList exists 'light' class it's removed if doesn't exist is created

	const img = document.querySelector('#profile img'); //same selector of CSS 

	if (html.classList.contains('light')) {
		img.setAttribute('src', './assets/images/avatar-light.png');
		
	} else {
		img.setAttribute('src', './assets/images/avatar.png');
	}
}
