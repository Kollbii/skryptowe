/**
 * In style.css added class:
 * .unsetting {
 *  all: revert;
 * }
 * :)
 */

document.getElementById('del').onclick = function () {
    ELEMENTS = document.querySelectorAll('header,h1,h2,aside,nav,main,footer,li,blockquote,p,form,input');
    ELEMENTS.forEach(elem => {
        elem.classList.add('unsetting');
        elem.classList.remove('azure');
    });
}

document.getElementById('set').onclick = function () {
    ELEMENTS = document.querySelectorAll('header,h1,h2,aside,nav,main,footer,li,blockquote,p,form,input');
    ELEMENTS.forEach(elem => {
        elem.classList.remove('unsetting');
        elem.classList.add('azure');
    });
    azureElem = document.querySelectorAll('li, h1, p, input, h2, blockquote');
    azureElem.forEach(elem => {
        elem.classList.remove('azure');
    });
}