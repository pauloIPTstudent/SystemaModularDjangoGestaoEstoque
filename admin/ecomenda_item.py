from django.contrib import admin
from ..models.encomenda_item import EncomendaItem

@admin.register(EncomendaItem)
class EncomendaItemAdmin(admin.ModelAdmin): 
    list_display = ("id", "encomenda_id", "produto_id", "quantidade", "preco_unitario", "desconto", "taxa_iva", "total_linha", "usuario_id")
    search_fields = ("encomenda_id", "produto_id")
    list_filter = ("encomenda_id", "produto_id")
    fieldsets = (
        ("Informações do Item da Encomenda", {
            'fields': ('encomenda_id', 'produto_id', 'quantidade', 'preco_unitario', 'desconto', 'taxa_iva', 'total_linha', 'usuario_id')
        }),
    )
    readonly_fields = ("id",)
    ordering = ("-encomenda_id",)  # Ordenar por ID da encomenda, do mais recente para o mais antigo
    list_per_page = 20  # Exibir 20 registros por página
    search_help_text = "Pesquisar por ID da encomenda ou ID do produto."
    list_select_related = True  # Otimiza consultas relacionadas, se aplicável
    actions = ['mark_as_processed']  # Exemplo de ação personalizada