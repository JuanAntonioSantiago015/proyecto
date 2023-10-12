# URL
from django.shortcuts import render

# CODIGOS HTTP
from django.http import Http404


# MODEL
from .models import Medicamento, HistorialMedicamento

# Create your views here.
def index(request):
    template_name = 'medicines/index.html'
    context = {
        'title':'Medicamentos'
    }
    return render(request,template_name, context)