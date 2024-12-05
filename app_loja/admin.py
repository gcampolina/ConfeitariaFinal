from django.contrib import admin
from .models import Produto, Pedido

admin.site.register(Produto)

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('segmento', 'massa', 'recheio', 'data_de_entrega', 'usuario')
    search_fields = ('segmento', 'massa', 'recheio', 'data_de_entrega', 'usuario__username')

admin.site.register(Pedido)