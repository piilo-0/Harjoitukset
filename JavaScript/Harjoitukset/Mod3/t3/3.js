'use strict';
const names = ['John', 'Paul', 'Jones'];

const target = document.getElementById("target");

let html = "";

// loop through array
for (let i = 0; i < names.length; i++) {
  html += `<li>${names[i]}</li>`;
}

// add to DOM using innerHTML
target.innerHTML = html;