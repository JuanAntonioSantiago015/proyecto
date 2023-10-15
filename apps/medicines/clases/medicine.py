class Medicamento:
    def __init__(self, id=None, medicine_name=None,description=None,brand=None, cost_price=None, sale_price=None,quantity_stock=None,presentatio_type=None,expiration_date=None,type_adminstrationform=None,type_therepeuticuse=None,medication_code=None,supplier=None):
        self.datos = {
            'id':id,
            'medicine_name':medicine_name,
            'description':description,
            'brand':brand,
            'cost_price':cost_price,
            'sale_price':sale_price,
            'quantity_stock':quantity_stock,
            'presentation_type':presentatio_type,
            'expiration_date':expiration_date,
            'type_adminstrationform':type_adminstrationform,
            'type_therepeuticuse':type_therepeuticuse,
            'medication_code':medication_code,
            'supplier':supplier
        }


    def __str__(self):       
        return '{}'.format(self.datos)





    