document.getElementById("Mensajeria").onsubmit = function(e){
    e.preventDefault();
    const liItem = document.createElement('li');
    liItem.innerHTML = document.getElementById("mensaje").value;
    document.getElementById("publicar_mensajes").appendChild(liItem);
}