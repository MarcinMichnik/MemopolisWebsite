const initialButton = document.querySelector('#to-be-veiled');
const deleteComment = document.querySelector('#veiled-delete-comment');

function revealDeleteComment(){
    initialButton.classList.add('veil');
    deleteComment.classList.remove('veil');
}
