import uuid 
from django.db import models

class MovimentoEstoque(models.Model):
    class TipoMovimento(models.TextChoices):
        ENTRADA = 'Entrada'
        SAIDA = 'Saida'
    
    class Origem(models.TextChoices):
        COMPRA = 'Compra'
        VENDA = 'Venda'
        AJUSTE = 'Ajuste'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    produto_servico = models.UUIDField(null=True, blank=True)  # ID do produto ou serviço
    tipo_movimento = models.CharField(max_length=20, choices=TipoMovimento.choices)
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    data_movimento = models.DateTimeField(auto_now_add=True)
    origem = models.CharField(max_length=20, choices=Origem.choices)
    origem_id = models.UUIDField(null=True, blank=True)  # ID da origem do movimento
    observacoes = models.TextField(null=True, blank=True)
    usuario_id = models.UUIDField(null=True, blank=True)  # ID do usuário que registrou o movimento

    def __str__(self):
        return f"{self.tipo_movimento} - {self.produto_servico.nome_do_produto} ({self.quantidade})"