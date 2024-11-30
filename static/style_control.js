// Modified from https://99gifshop.neocities.org/theme-control.js

// This will called when the site is loaded
document.addEventListener("DOMContentLoaded", function (event) {
	const mediaQuery = window.matchMedia("(prefers-color-scheme: dark)")
	if (localStorage.getItem('theme') === 'dark' || 'light')
		changeTheme(localStorage.getItem('theme'))
	else {
		if (mediaQuery.matches)
			changeTheme('dark')
		else
			changeTheme('light')
	} // Add listener for real time user colour scheme preference change
	mediaQuery.addListener(e => {
		if (e.matches)
			changeTheme('dark')
		else
			changeTheme('light')
	})
});

function toggleTheme() {
	if (document.documentElement.getAttribute('data-theme') === 'dark')
		changeTheme('light')
	else
		changeTheme('dark')

}

function toggleFont() {
	changeFont(localStorage.getItem("font-mode") === "main" ? "readable" : "main");
}

function changeTheme(theme) {
	document.documentElement.setAttribute('data-theme', theme);
	localStorage.setItem('theme', theme);
	// Refresh font
	changeFont(localStorage.getItem("font-mode"))
}

function changeFont(mode) {
	localStorage.setItem("font-mode", mode);

	setTagFont("body", mode);
	setTagFont("button", mode);

	for (const tag of ["h1", "h2", "h3", "h4", "h5", "h6"]) {
		setTagFont(tag, mode === "main" ? "big" : "readable");
	}
}

function setTagFont(tag, fontFamily) {
	for (const elem of document.getElementsByTagName(tag)) {
		elem.style.fontFamily = fontFamily;
	}
}