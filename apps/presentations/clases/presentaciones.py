import json

class Presentacion:
    contador = 0
    def __init__(self, presentation_type):
        Presentacion.contador+=1
        self._id = Presentacion.contador
        self._presentation_type = presentation_type
        self._presentation_dic = {}

    @property
    def id(self):
        return self._id
    
    @property
    def tipo_presentacion(self):
        return self._presentation_type
    
    @property
    def diccionario(self):
        self._presentation_dic['id']=self.id
        self._presentation_dic['presentation_type']=self.tipo_presentacion
        return self._presentation_dic
    
    def __str__(self):
        return json.dumps(self.diccionario)
    