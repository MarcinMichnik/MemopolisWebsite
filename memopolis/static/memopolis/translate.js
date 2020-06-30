
const title = document.querySelector('label.requiredField');

if (title.innerText=='Title*') {
    title.innerText = 'Tytuł*';
}

else if (title.innerText=='Content*'){
    title.innerText = 'Tekst*';
}



const second = document.querySelectorAll('label.requiredField')[1];
if (second.innerText == 'Image*') {
    second.innerText = 'Obrazek*';
}
else if (second.innerText == 'Tags*') {
    second.innerText = 'Tagi*';
}

const third = document.querySelectorAll('label.requiredField')[2];
if (third.innerText == 'Tags*') {
    third.innerText = 'Tagi*';
}
