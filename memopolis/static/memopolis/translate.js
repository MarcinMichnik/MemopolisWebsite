const title = document.querySelector('label.requiredField');
console.log("K");

const img = document.querySelectorAll('label.requiredField')[4];
img.innerText = 'Obrazek*';

if (title.innerText=='Title*') {
    title.innerText = 'Tytuł*';
    console.log('y22y');
}


if (title.innerText=='Content*'){
    title.innerText = 'Tekst*';
    console.log('yy');
}
