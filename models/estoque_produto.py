import uuid
from django.db import models

class EstoqueProduto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    produto_id = models.ForeignKey('faturacao.ProdutoServico', on_delete=models.CASCADE)
    quantidade_estoque = models.PositiveIntegerField()
    minimo_estoque = models.PositiveIntegerField(default=0)
    local_armazenamento = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.produto.nome_do_produto} - {self.quantidade} unidades"
