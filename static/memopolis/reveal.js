function translate() {
    const title = document.querySelector('label.requiredField');

    if (title.innerText=='Title*') {
        title.innerText = 'Tytuł*';
    }
    if (title.innerText=='Content*'){
        title.innerText = 'Tekst*';
    }
    const img = document.querySelectorAll('label.requiredField')[4];
    img.innerText = 'Obrazek*';
}



const createComment = document.querySelector('.veil');
const plusButton = document.querySelector('.add-button');

if (plusButton.classList.contains('reveal')) {
    plusButton.classList.remove('reveal');
}

function reveal(){
    plusButton.classList.add('veil');
    createComment.classList.add('reveal');

    translate();
}
