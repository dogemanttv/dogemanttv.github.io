// ==UserScript==
// @name        movie-web autoplay
// @namespace   Violentmonkey Scripts
// @match       *://movie-web.app/*
// @grant       none
// @version     1.0
// @author      dogeman@nullsoftware.dev
// @description 11/24/2023, 1:47:13 AM
// ==/UserScript==
function dostuff() {
	document.getElementsByClassName("flex items-center justify-center rounded-full bg-denim-600 bg-opacity-0 transition-colors duration-100  p-2 sm:px-4 group-hover:bg-opacity-50 group-active:bg-denim-500 group-active:bg-opacity-100")[1].click()
    i = 0
    var final = 0;
    var finalfound = false;
    Array.from(document.getElementsByClassName("p-5 relative h-full overflow-y-auto bg-ash-300")[0].children[0].children).forEach(function (element) {
        console.log(element)
        if ((final + 1) == i && finalfound == true && i != document.getElementsByClassName("p-5 relative h-full overflow-y-auto bg-ash-300")[0].children[0].children.length) {
            element.click()
        }
        try {
            if (element.attributes[0].nodeValue.split("outline-denim-")[1] == "700") {
                console.log(i)
                final = i
                finalfound = true;
            }
        }
        catch {
        }
        i += 1
    });
}
function domorestuff() {
document.getElementsByClassName("z-0 h-full w-full")[0].onended = (event) => {
setTimeout(dostuff, 2000)
};
}
setTimeout(domorestuff, 5000)
