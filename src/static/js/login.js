document.addEventListener('DOMContentLoaded',()=>{
    document.querySelector('#loginUser').onclick = ()=>{
        document.querySelector('#login').style.display = '';
        document.querySelector('#register').style.display = 'none';
        document.querySelector('#shoeType').style.display = 'none';
        document.getElementById( 'login' ).scrollIntoView();

        
    }  
    
    if(document.querySelector('#loginForm')){

        document.querySelector('#loginForm').onsubmit = ()=>{

            let request = new XMLHttpRequest();
            let loginForm = document.querySelector('#loginForm');
            let data = new FormData(loginForm);

            request.open('POST', '/login');
            request.send(data)  
            request.onload = ()=>{
                let data = JSON.parse(request.responseText);
                console.log(data.success.value)
                if(data.success){
                    
                    location.reload();
                    document.getElementById( 'top' ).scrollIntoView();
                }
                else{
                    window.stop();
                    alert('Invalid username or password');
                }
            }
            return false;
        }
    }
    
    
});