document.addEventListener('DOMContentLoaded',()=>{

    document.querySelector('#RegisterUser').onclick = ()=>{
        document.querySelector('#register').style.display = '';
        document.querySelector('#login').style.display = 'none';
        document.querySelector('#shoeType').style.display = 'none';
        document.getElementById( 'register' ).scrollIntoView();

        
    }

    if(document.querySelector('#registerForm')){
        document.querySelector('#registerForm').onsubmit = ()=>{

            
            let registerForm = document.querySelector('#registerForm');
            if(registerForm.password.value === registerForm.password2.value){
                let request = new XMLHttpRequest();
                let data = new FormData(registerForm);

                request.open('POST', "/rregister");
                request.send(data)

                request.onload = ()=>{
                    let data = JSON.parse(request.responseText) 
                    if(data.response === 'success'){
                        
                        document.querySelector('#register').style.display = 'none';
                        document.querySelector('#login').style.display = '';
                        document.querySelector('#shoeType').style.display = 'none';
                        document.getElementById( 'login' ).scrollIntoView();
                    }
                    else{
                        alert('Enter all details')
                    }
                }
            }
            else{
                alert('Password not matching')
            }
            
            return false;
        }
    }
});