import json


class Medicamento:
  contador=0

  def __init__(self,id,medicine_name,description=None, creation_date=None):
      Medicamento.contador+=1
      self._contador = Medicamento.contador
      self._id = id
      self._medicine_name = medicine_name
      self._description = description
      self._creation_date = creation_date
      self._medicamento_dic = {}

  @property
  def id(self):
      return self._id
  
  @property
  def contadorRegistro(self):
      return self._contador

  @property
  def medicine_name(self):
      return self._medicine_name

  @property
  def description(self):
      return self._description

  @property
  def creation_date(self):
      return self._creation_date
  
  @property
  def diccionario(self):
      self._medicamento_dic['id'] = self.id
      self._medicamento_dic['medicine_name'] =self.medicine_name
      self._medicamento_dic['description'] = self.description
      self._medicamento_dic['creation_date']=self.creation_date

      return self._medicamento_dic
      
  

  def __str__(self): 
      return json.dumps(self.diccionario)


class HistorialMedicamento:
    contador = 0
    def __init__(self, id,medicine_id, supplier_id,presentation_id, cost_price=None, brand=None, medication_code=None, expiration_date=None):
        HistorialMedicamento.contador+=1
        self._contador = HistorialMedicamento.contador
        self._id = id
        self._medicine_id = medicine_id

        if supplier_id is None:
            supplier_id = []
        self._supplier_id = supplier_id

        if presentation_id is None:
            presentation_id = []
        self._presentation_id = presentation_id

        self._cost_price = cost_price
        self._brand = brand
        self._medication_code = medication_code
        self._expiration_date = expiration_date
        self._historial_dic = {}
    
    @property
    def contadorRegistro(self):
        return self._contador
    
    @property
    def id(self):
        return self._id
    
    @property
    def medicine_id(self):
        return self._medicine_id.diccionario
    
    @property
    def suppliers(self):
        list_suppliers = []
        for p in self._presentation_id:
            proveedor ={
                'id':p.id,
                'full_name':p.full_name,
                'company':p.company,
                'telephone':p.telephone,
                'email':p.email
            }
            list_suppliers.append(proveedor)
        return list_suppliers
    
    @property
    def presentations(self):
        list_presentation = []
        for p in self._presentation_id:
            presentacion = {
                'id':p.id,
                'presentation_type':p.presentation_type
            }
            list_presentation.append(presentacion)
        return list_presentation
    
    @property
    def brand(self):
        return self._brand
    
    @property
    def medication_code(self):
        return self._medication_code
    
    @property
    def expiration_date(self):
        return self._expiration_date
    
    @property
    def diccionario(self):
        self._historial_dic['id']=self.id
        self._historial_dic['medicine_id']=self.medicine_id
        self._historial_dic['supplier_id']=self.suppliers
        self._historial_dic['presentation_id']=self.presentations
        self._historial_dic['brand']=self.brand
        self._historial_dic['medication_code']=self.medication_code
        self._historial_dic['expiration_date'] = self.expiration_date
    
    def agregar_proveedores(self,element):
        self._supplier_id.append(element)
    
    def agregar_presentaciones(self,element):
        self._presentation_id.append(element)
    
    def __str__(self):
        return json.dumps(self.diccionario)