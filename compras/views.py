from django.shortcuts import render, HttpResponseRedirect
from .models import Produtos
from .forms import *


def index(request):
    bForm = BuscaForm(request.POST or None)

    if(bForm.is_valid()):
        if bForm.cleaned_data.get('produto') == "Todos":
            products = Produtos.objects.all()
            return render(request, "list_prod.html", {'products' : products})
        else:
            products = Produtos.objects.all().filter(nome = bForm.cleaned_data.get('produto'))
            return render(request, "list_prod.html", {'products' : products})

    return render(request, "index.html", {'form':bForm})

def inserir(request):
    produtoForm = ProdutoForm(request.POST or None)

    if(produtoForm.is_valid()):
        produtoForm.save()
        return HttpResponseRedirect('/')

    return render(request, "cad_prod.html", {'form': produtoForm})

def editar(request, id):
    p = Produtos.objects.get(id=id)
    produtoForm = ProdutoForm(request.POST or None, instance = p)

    if(produtoForm.is_valid()):
        produtoForm.save()
        return HttpResponseRedirect('/')

    return render(request, "cad_prod.html", {'form': produtoForm, 'p': p})

def delete(request, id):
    produto = Produtos.objects.get(id=id)
    produto.delete()

    return HttpResponseRedirect('/')