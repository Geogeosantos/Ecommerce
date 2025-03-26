from django.contrib import admin

from produtos.models import camisa, calca

class camisaAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'cor', 'tamanho', 'preco')
    list_display_links = ('nome', 'id')
    search_fields = ('nome', 'cor', 'tamanho', 'preco')
    list_per_page = 10
    list_filter = ('nome', 'cor', 'tamanho', 'preco')

class calcaAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'cor', 'tamanho', 'preco')
    list_display_links = ('nome', 'id')
    search_fields = ('nome', 'cor', 'tamanho', 'preco')
    list_per_page = 10
    list_filter = ('nome', 'cor', 'tamanho', 'preco')

admin.site.register(camisa, camisaAdmin)
admin.site.register(calca, calcaAdmin)
