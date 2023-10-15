# URL
from django.shortcuts import render

# CODIGOS HTTP
from django.http import Http404


# DJANGO
from django.shortcuts import render


# CONSULTA
from .consultas.resultado_consulta import listar,existencia, vencidos


# MODEL
from .models import Medicamento, HistorialMedicamento
from apps.locations.models import HistorialInvetario, Ubicacion
from apps.classifications.models import Clasificacion

# PAGINACION
from .pagination import paginacion

# Create your views here.
def index(request):
    # OBTENER MEDICAMENTOS
    medicine_list = Medicamento.objects.all()

    # OBTENER UBICACIONES
    ubicacion_list = Ubicacion.objects.all()

    # PAGINACION
    
    page_obj = paginacion(request,medicine_list)

    # TEMPLATE
    template_name = 'medicines/index.html' 
    
    medicamento_list = listar()

    # CONEXTO
    context = {
        'title':'Medicamentos',
        'page_obj':page_obj,
        'medicamento_list':medicamento_list,
        'ubicacion_list':ubicacion_list
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
    template_name = 'medicines/index.html' 
        
    medicamento_existencia = existencia()
    # CONEXTO
    context = {
        'title':'Medicamentos Existentes',
        'page_obj':page_obj,
        'medicamento_list':medicamento_existencia,
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
    template_name = 'medicines/index.html' 
    
    medicamento_vencido = vencidos()
    
    # CONEXTO
    context = {
        'title':'Medicamentos Vencidos',
        'page_obj':page_obj,
        'medicamento_list':medicamento_vencido,
        'ubicacion_list':ubicacion_list,
    }
    return render(request,template_name, context)


def add(request):
    pass