import uuid
from django.db import models

class Encomenda(models.Model):
    class Estado(models.TextChoices):
        PENDENTE = 'P', 'Pendente'
        EM_ANDAMENTO = 'A', 'Em Andamento'
        CONCLUIDA = 'C', 'Concluída'
        CANCELADA = 'X', 'Cancelada'
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_entrega = models.DateTimeField(null=True, blank=True)
    estado = models.CharField(max_length=1, choices=Estado.choices, default=Estado.PENDENTE)
    total_bruto = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_desconto = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_liquido = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    obeservacoes = models.TextField(blank=True, null=True)
    usuario_id = models.UUIDField(null=True, blank=True)  # ID do usuário que criou a encomenda
    
    def __str__(self):
        return f"Encomenda {self.id} - Produto {self.produto_id}"