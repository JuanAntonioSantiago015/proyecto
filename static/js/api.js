const url = 'http://127.0.0.1:8000/medicamentos/api/historial-medicamento/'


fetch(url).then(function(response){
    return response.json()
}).then(function (data){
    console.log(data)
    
    data.forEach((dato) => {
        console.log(dato.medicine_id.medicine_name)


    });
})


