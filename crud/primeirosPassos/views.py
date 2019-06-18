from django.shortcuts import render
from .models import Pessoa
# Create your views here.


def listar_registros(request):
    p = Pessoa.objects.all()
    return render(request, 'lista.html', {'pessoa': p})
