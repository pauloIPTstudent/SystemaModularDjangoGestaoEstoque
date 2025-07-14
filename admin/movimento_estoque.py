from django.contrib import admin
from ..models.movimento_estoque import MovimentoEstoque

@admin.register(MovimentoEstoque)
class MovimentoEstoqueAdmin(admin.ModelAdmin):
    list_display = ("id", "produto_servico", "quantidade", "tipo_movimento", "data_movimento", "usuario_id")
    search_fields = ("produto_servico", "usuario_id")
    list_filter = ("tipo_movimento", "data_movimento")
    fieldsets = (
        ("Informações do Movimento", {
            'fields': ('produto_servico', 'quantidade', 'tipo_movimento', 'data_movimento', 'usuario_id')
        }),
    )
    readonly_fields = ("id",)
    ordering = ("-data_movimento",)  # Ordenar por data do movimento, do mais recente para o mais antigo
    list_per_page = 20  # Exibir 20 registros por página
    search_help_text = "Pesquisar por ID do produto ou usuário."
    list_select_related = True  # Otimiza consultas relacionadas, se aplicável
    actions = ['mark_as_processed']  # Exemplo de ação personalizada

    