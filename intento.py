from apps.classifications.clases.clasificaciones import UsoTerapeutico, FormaAdministracion, Clasificacion
from apps.medicines.clases.medicamentos import Medicamento
import json

if __name__ == '__main__':
    ad = FormaAdministracion('Oral')
    us = UsoTerapeutico('Aliviar')
    me = Medicamento('Ibuprofeno')
    cla = Clasificacion(me)
    cla.agregar_forma_administracion(ad)
    cla.agregar_forma_administracion(ad)
    cla.agregar_uso_terapeeutico(us)
    print('ahhh')
    print(me)

    interar = str(cla)
    
    print(interar)
    