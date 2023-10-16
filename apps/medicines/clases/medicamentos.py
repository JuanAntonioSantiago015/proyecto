import json


class Medicamento:
  contador=0

  def __init__(self,medicine_name,description=None, creation_date=None):
      Medicamento.contador+=1
      self._id = Medicamento.contador
      self._medicine_name = medicine_name
      self._description = description
      self._creation_date = creation_date


  @property
  def id(self):
      return self._id

  @property
  def medicine_name(self):
      return self._medicine_name

  @property
  def description(self):
      return self._description

  @property
  def creation_date(self):
      return self._creation_date
  

  def __str__(self):      
      medicamento_dic = {
          'id':self.id,
          'medicine_name':self.medicine_name,
          'description':self.description,
          'creation_date':self.creation_date
      }
      return json.dumps(medicamento_dic)


