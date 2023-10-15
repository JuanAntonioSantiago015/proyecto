
# CONSULTA 
__parametro = '''
M.id AS 'id', 
M.medicine_name AS 'NOMBRE DEL MEDICAMENTO', 
M.description AS 'DESCRIPCION DEL MEDICAMENTO',
H.brand AS 'MARCA',
H.cost_price AS 'PRECIO DE COSTO',
HI.sale_price AS 'PRECIO DE VENTA',
HI.quantity_stock AS 'CANTIDAD',
P.presentation_type AS 'TIPO DE PRESENTACION',
H.expiration_date AS 'FECHA DE VENCIMIENTO',
FA.type_adminstrationform AS 'FORMA DE ADMINISTRACION', 
UT.type_therepeuticuse AS 'USO TERAPEUTICO',
H.medication_code AS 'CODIGO DE MEDICAMENTO',
CONCAT(PR.first_name,' ', IF(PR.last_name != 'NULL', PR.last_name, '') )AS 'NOMBRE DEL PROVEEDOR'

'''

__inner = '''
FROM medicines_medicamento M 
INNER JOIN classifications_clasificacion C ON M.id = C.medicine_id_id
INNER JOIN classifications_formaadministracion FA on FA.id = C.formadministration_id_id
INNER JOIN classifications_usoterapeutico UT on UT.id = C.therepeuticuse_id_id
INNER JOIN medicines_historialmedicamento H on M.id = H.medicine_id_id
INNER JOIN presentations_presentacion P on P.id = H.presentation_id_id
INNER JOIN locations_historialinvetario HI on M.id = HI.medicine_id_id
INNER JOIN suppliers_proveedor PR on PR.id = H.supplier_id_id
'''

listado_completo_medicamentos = 'SELECT '+__parametro+__inner+';'


listado_medicamento_existencia = 'SELECT '+__parametro+__inner+' WHERE HI.quantity_stock !=0'+';'


listado_medicamento_vencido = 'SELECT'+ __parametro +__inner + 'WHERE H.expiration_date < CURDATE();'
