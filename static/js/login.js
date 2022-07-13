document.getElementById("login").onsubmit = function(e){
    e.preventDefault();
    fetch('/authenticate/login', {
        method : 'POST',
        body: JSON.stringify({
            'username': document.getElementById('username').value,
            'password': document.getElementById('password').value,
            'control' : document.getElementById('control').value
        }),
        headers : {
            'Content-Type' : 'application/json'
        },
    }).then(function(response){
        return response.json()
    }).then(function(jsonResponse){
        console.log(jsonResponse)
        if(jsonResponse['error'] === false){
            window.location.replace('/homepage/'+jsonResponse['type'])
            document.getElementById("error").className='hidden'
        }else{
            document.getElementById("error").className=''
            document.getElementById("error").innerHTML = jsonResponse['error_message']
        }
    }).catch(function(error) {
        console.log(error)
        document.getElementById("error").className=''
    });
}