function validar(){
    cedula = parseInt(document.getElementById("ci").value);
    if (cedula <= 800000 ){
        respuesta = confirm("Rango invalido. \n ¿Enviar de todos modos?");
        return respuesta;
    }
}

function validar2(){
    cedula = parseInt(document.getElementById("ci").value);
     if (cedula <= 800000 ){
        alert("Es posible que la cedula no corresponda");
    }
}

