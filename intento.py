from apps.classifications.clases.clasificaciones import UsoTerapeutico, FormaAdministracion, Clasificacion
from apps.medicines.clases.medicamentos import Medicamento
import json

if __name__ == '__main__':
    
    me = Medicamento(1,'Ibuprofeno')
    """ 
    
    ad = FormaAdministracion('Oral')
    us = UsoTerapeutico('Aliviar')
    cla = Clasificacion(me)
    cla.agregar_forma_administracion(ad)
    cla.agregar_forma_administracion(ad)
    cla.agregar_uso_terapeeutico(us)
    """
    
    print('ahhh')


    
    print(me.contadorRegistro)
    