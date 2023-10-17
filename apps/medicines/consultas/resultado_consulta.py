# Conecction
from django.db import connection
import json

# CONSULTAS
from .consulta import LISTADOMEDICAMENTO, LISTADOCLASIFICACION, LISTADOHISTORIALMEDICAMENTO, LISTADOHISTORIALINVENTARIO

# CLASES
from ..clases.medicamentos import Medicamento, HistorialMedicamento
from apps.classifications.clases.clasificaciones import UsoTerapeutico, FormaAdministracion, Clasificacion
from apps.locations.clases.ubicaciones import Ubicacion, Seccion, HistorialInventario
from apps.suppliers.clases.proveedores import Proveedor
from apps.presentations.clases.presentaciones import Presentacion

# RECURSOS
from .recurso import clasifications,historial_medicamento, inventory

def listar():
    listado_general = []
    consulta_listado_medicamento = LISTADOMEDICAMENTO+';'
    
    consulta_listado_historial_medicamento = LISTADOHISTORIALMEDICAMENTO+' WHERE H.medicine_id_id = %s'+';'
    consulta_listado_historial_inventario = LISTADOHISTORIALINVENTARIO+' WHERE HI.medicine_id_id = %s'+';'
    

    with connection.cursor() as cursor:
        medicamento_list = []
        cursor.execute(consulta_listado_medicamento)
        resultado = cursor.fetchall()
        

        for medicamento in resultado:
            medi = Medicamento(medicamento[0],medicamento[1],medicamento[2],medicamento[3])
            medicamento_list.append(medi)
        
        for medicina in medicamento_list:
            consulta_listado_clasificacion = LISTADOCLASIFICACION+' WHERE C.medicine_id_id = {}'.format(medicina.id)+';'
            cursor.execute(consulta_listado_clasificacion)
            resultado = cursor.fetchmany()
            
            clasificacion = clasifications(resultado,medicina)
            print(clasificacion)  

            cursor.execute(consulta_listado_historial_medicamento, str(medicina.id))
            resultado = cursor.fetchall()
            
            historialM= historial_medicamento(resultado,medicina)

            cursor.execute(consulta_listado_historial_inventario, str(medicina.id))
            resultado = cursor.fetchall()

            historialI = inventory(resultado,medicina)

            medicamento_dic = {
                'medicines':medicina.diccionario,
                'clasificacion':clasificacion,
                'historial_medicamento':historialM,
                'historial_inventario':historialI
            }

            listado_general.append(medicamento_dic)
    #return listado_general

            