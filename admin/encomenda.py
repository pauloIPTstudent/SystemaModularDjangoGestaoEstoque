from django.contrib import admin
from ..models.encomenda import Encomenda

@admin.register(Encomenda)
class EncomendaAdmin(admin.ModelAdmin):
    list_display = ("id", "data_criacao", "data_entrega", "estado", "total_bruto", "total_desconto", "total_liquido", "observacoes", "usuario_id")
    search_fields = ("id", "usuario_id")
    list_filter = ("estado",)
    fieldsets = (
        ("Informações Básicas", {
            'fields': ('data_criacao', 'data_entrega', 'estado', 'total_bruto', 'total_desconto', 'total_liquido', 'observacoes', 'usuario_id')
        }),
    )  