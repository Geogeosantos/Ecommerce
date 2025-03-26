from django.shortcuts import render, get_object_or_404

from produtos.models import camisa, calca

def index(request):
    return render(request, 'produtos/index.html')

def t_shirts(request):
    camisas = camisa.objects.all()
    total_camisas = camisas.count()
    return render(request, 'produtos/camisas.html', {'camisas': camisas, 'total_camisas': total_camisas})

def jeans(request):
    calcas = calca.objects.all()

    return render(request, 'produtos/jeans.html')

def produto_camisa(request, produto_id):
    produto = get_object_or_404(camisa, id=produto_id)
    return render(request, 'produtos/produto.html', {'produto': produto})

def checkout(request):
    return render(request, 'produtos/checkout.html')

def login(request):
    return render(request, 'produtos/login.html')