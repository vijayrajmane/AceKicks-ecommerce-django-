
    document.addEventListener('DOMContentLoaded',() => {

        document.querySelector('#addToCart').onclick = () =>{
            let request = new XMLHttpRequest();
            let productID = document.querySelector('#addToCart').dataset.id;
            var e = document.getElementById("size");
            var size = e.options[e.selectedIndex].value;
            console.log(productID);
            console.log(size);
            
            if(size === ''){
                alert('Select the shoe size')
            }
            else{
                let data = new FormData();
                data.append('productID', productID);
                data.append('size', size);
                request.open('POST', '/addItem');
                request.send(data)
    
                request.onload = ()=>{
                let data = JSON.parse(request.responseText);
                if(data.success){
                    console.log(data.success)
                    location.reload();
                    }
                else{
                    window.location = "http://127.0.0.1:8000"
                    alert('Login/Register to order')
                    
                    }
                }
            }
            
        }
    });
    




 

