document.addEventListener('DOMContentLoaded', ()=>{
    document.querySelector('#brand').onclick = ()=>{
        document.getElementById( 'brandMenu' ).scrollIntoView();
    }
    document.querySelector('#category').onclick = ()=>{
        document.getElementById( 'categoryMenu' ).scrollIntoView();
    }
});