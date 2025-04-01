from django.shortcuts import render
from .models import Produto

def home(request):
    produtos = Produto.objects.all()
    return render(request, 'mix/home.html', {'produtos': produtos})

def detalhe_produto(request, pk):
    produto = Produto.objects.get(pk=pk)
    return render(request, 'mix/detalhe_produto.html', {'produto': produto})
