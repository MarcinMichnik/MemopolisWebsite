
const title = document.querySelector('label.requiredField');

if (title.innerText=='Title*') {
    title.innerText = 'Tytuł*';
}

else if (title.innerText=='Content*'){
    title.innerText = 'Tekst*';
}



const img = document.querySelectorAll('label.requiredField')[1];
if (img.innerText = 'Image*') {
    img.innerText = 'Obrazek*';
}

const tags = document.querySelectorAll('label.requiredField')[2];
if (tags.innerText = 'Tags*') {
    tags.innerText = 'Tagi*';
}
