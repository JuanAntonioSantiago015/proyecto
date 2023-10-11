const url = 'http://127.0.0.1:8000/ubicacion/api-v1/historial_inventario/'

const ap = document.getElementById('description')

fetch(url).then(function(response){
    return response.json()
}).then(function (data){
    console.log(data)
    console.log(dato.medicine_id.medicine_name)
    data.forEach(function(dato) {
        ap.innerText=dato.medicine_id
        
    });
})


