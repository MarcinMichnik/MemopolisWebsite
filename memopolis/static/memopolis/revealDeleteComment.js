function revealDeleteComment(counter){
    const initialButton = document.getElementsByClassName('to-be-veiled')[counter-1];
    const deleteComment = document.getElementsByClassName('veiled-delete-comment')[counter-1];

    console.log(initialButton);
    console.log(deleteComment);

    initialButton.classList.add('veil');
    deleteComment.classList.remove('veil');
}
