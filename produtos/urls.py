from django.urls import path
from produtos.views import index, t_shirts, jeans, checkout, login, produto_camisa

urlpatterns = [
    path('', index, name='index'),
    path('t_shirts/', t_shirts, name='t_shirts'),
    path('jeans/', jeans, name='jeans'),
    path('checkout/', checkout, name='checkout'),
    path('login/', login, name='login'),
    path('produto/<int:produto_id>', produto_camisa, name='produto')
]