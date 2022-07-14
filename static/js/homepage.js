document.getElementById("Publicar").onsubmit = function(e){
    e.preventDefault();
    fetch('/agregar/message', {
        method : 'POST',
        body: JSON.stringify({
            'message': document.getElementById('mensaje').value,
            'control': document.getElementById('control').value
        }),
        headers : {
            'Content-Type' : 'application/json'
        },
    }).then(function(response){
        return response.json()
    }).then(function(jsonResponse){
        console.log(jsonResponse)
        if(jsonResponse['error'] === false){
            alert("Mensaje agregado")
            const liItem = document.createElement('li')
            liItem.innerHTML = jsonResponse['mensaje'] + " " + jsonResponse["topic"]
            document.getElementById("publicar_mensajes").appendChild(liItem)
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