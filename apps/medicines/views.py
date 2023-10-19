# URL
from django.shortcuts import render

# CODIGOS HTTP
from django.http import Http404


# DJANGO
from django.shortcuts import render


# CONSULTA
from .consultas.resultado_consulta import listar, existencia, vencidos


# MODEL
from .models import Medicamento, HistorialMedicamento
from apps.locations.models import HistorialInvetario, Ubicacion
from apps.classifications.models import Clasificacion, UsoTerapeutico, FormaAdministracion
from apps.suppliers.models import Proveedor
from apps.presentations.models import Presentacion
# PAGINACION
from .pagination import paginacion
from django.db.models import Q
from django.http import HttpResponse

import json


from datetime import datetime, date

fecha_actual = datetime.now()
fecha_actual_solo_fecha = fecha_actual.date()

# Create your views here.
def index(request):
    # OBTENER MEDICAMENTOS
    medicine_list = Medicamento.objects.all()

    # OBTENER UBICACIONES
    ubicacion_list = Ubicacion.objects.all()
    
    #OBTENER LA CLASIFICACION
    clasificacion_list = Clasificacion.objects.all()

    # OBTENER EL HISTORIAL DEL MEDICAMENTO
    historial_medico_list = HistorialMedicamento.objects.all()

    # OBTENER EL HISTORIAL DE INVENTARIO
    historial_inventario_list = HistorialInvetario.objects.all()
    
    
    # PAGINACION
    
    page_obj = paginacion(request,medicine_list)

    # TEMPLATE
    template_name = 'medicines/index.html' 

   
    
    contador = 0


    # CONEXTO
    context = {
        'title':'Medicamentos',
        'page_obj':page_obj,
        'medicamento_list':medicine_list,
        'ubicacion_list':ubicacion_list,
        'clasificacion_list':clasificacion_list,
        'historial_medico_list':historial_medico_list,
        'historial_inventario_list':historial_inventario_list,
        'contar':contador
    }
    
    return render(request,template_name, context)

def existence(request):
    # OBTENER MEDICAMENTOS
    medicine_list = Medicamento.objects.all()

     # OBTENER UBICACIONES
    ubicacion_list = Ubicacion.objects.all()

    # PAGINACION
    page_obj = paginacion(request,medicine_list)

    # TEMPLATE
    template_name = 'medicines/base/medicina_filtro.html' 
        

    # CONEXTO
    context = {
        'title':'Medicamentos Existentes',
        'page_obj':page_obj,
        
        'ubicacion_list':ubicacion_list,
    }
    return render(request,template_name, context)

def defeated(request):
    # OBTENER MEDICAMENTOS
    medicine_list = Medicamento.objects.all()

    # OBTENER UBICACIONES
    ubicacion_list = Ubicacion.objects.all()

    # PAGINACION
    page_obj = paginacion(request,medicine_list)

    # TEMPLATE
    template_name = 'medicines/base/medicina_filtro.html' 
    

    
    # CONEXTO
    context = {
        'title':'Medicamentos Vencidos',
        'page_obj':page_obj,

        'ubicacion_list':ubicacion_list,
    }
    return render(request,template_name, context)


def add(request):
    uso_terapeutico_list =UsoTerapeutico.objects.all()
    forma_administracion_list = FormaAdministracion.objects.all()
    proveedor_list = Proveedor.objects.all()
    presentacion_list = Presentacion.objects.all()
    context = {
        'uso_terapeutico_list': uso_terapeutico_list,
        'forma_administracion_list':forma_administracion_list,
        'proveedor_list':proveedor_list,
        'presentacion_list':presentacion_list,
        'title':'Registro de Medicamento'
    }

    if request.method == 'GET':
        medicina_name = request.GET.get('medicine_name')
        opciones_uso = request.GET.getlist('opciones_uso[]')
        opciones_forma = request.GET.getlist('opciones_forma[]')
        presentacion = request.GET.get('tipo_presentacion')
        proveedor = request.GET.get('proveedor_select')
        print(proveedor)
    return render(request, 'medicines/base/form.html', context)
    
    