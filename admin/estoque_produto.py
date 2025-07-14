from django.contrib import admin
from ..models.estoque_produto import EstoqueProduto

@admin.register(EstoqueProduto)
class EstoqueProdutoAdmin(admin.ModelAdmin):
    list_display = ("id", "produto_id", "quantidade_estoque", "local_armazenamento", "ativo", "data_criacao")
    search_fields = ("produto_id",)
    list_filter = ("data_criacao", "ativo")
    fieldsets = (
        ("Informações do Produto", {
            'fields': ('produto_id', 'quantidade_estoque', 'minimo_estoque', 'local_armazenamento', 'ativo', 'data_criacao')
        }),    
    )
    readonly_fields = ("id",)  # ID é gerado automaticamente e não deve ser editável
    ordering = ("data_criacao",)  # Ordenar por data de criacao, do mais recente para o mais antigo
    list_per_page = 20  # Exibir 20 registros por página
    search_help_text = "Pesquisar por ID do produto ou outros campos relevantes."
    list_select_related = True  # Otimiza consultas relacionadas, se aplicável
    actions = ['mark_as_processed']  # Exemplo de ação personalizada