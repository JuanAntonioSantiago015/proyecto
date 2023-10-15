from django.db import connection
from .consulta import listado_completo_medicamentos, listado_medicamento_existencia, listado_medicamento_vencido






def listar():
    medicamento_list=[]

    with connection.cursor() as cursor:
        cursor.execute(listado_completo_medicamentos)    
        resultados = cursor.fetchall()
        for resul in resultados:
            medicamentos ={
                'id':resul[0],
                'medicine_name':resul[1],
                'description':resul[2],
                'brand':resul[3],
                'cost_price':resul[4],
                'sale_price':resul[5],
                'quantity_stock':resul[6],
                'presentation_type':resul[7],
                'expiration_date':resul[8],
                'type_adminstrationform':resul[9],
                'type_therepeuticuse':resul[10],
                'medication_code':resul[11],
                'supplier':resul[12]


            }
            medicamento_list.append(medicamentos)
    return medicamento_list
        
def existencia():
    medicamento_existencia = []

    with connection.cursor() as cursor:
        cursor.execute(listado_medicamento_existencia)    
        resultados = cursor.fetchall()
        for resul in resultados:        
            medicamentos ={
                'id':resul[0],
                'medicine_name':resul[1],
                'description':resul[2],
                'brand':resul[3],
                'cost_price':resul[4],
                'sale_price':resul[5],
                'quantity_stock':resul[6],
                'presentation_type':resul[7],
                'expiration_date':resul[8],
                'type_adminstrationform':resul[9],
                'type_therepeuticuse':resul[10],
                'medication_code':resul[11],
                'supplier':resul[12]


            }
            medicamento_existencia.append(medicamentos)
    return medicamento_existencia

def vencidos():
    medicamento_vencido = []

    with connection.cursor() as cursor:
        cursor.execute(listado_medicamento_vencido)    
        resultados = cursor.fetchall()
        
        
        for resul in resultados:     
                
            medicamentos ={
                'id':resul[0],
                'medicine_name':resul[1],
                'description':resul[2],
                'brand':resul[3],
                'cost_price':resul[4],
                'sale_price':resul[5],
                'quantity_stock':resul[6],
                'presentation_type':resul[7],
                'expiration_date':resul[8],
                'type_adminstrationform':resul[9],
                'type_therepeuticuse':resul[10],
                'medication_code':resul[11],
                'supplier':resul[12]


            }
            medicamento_vencido.append(medicamentos)
    return medicamento_vencido

