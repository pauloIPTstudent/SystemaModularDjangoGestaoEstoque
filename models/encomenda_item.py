import uuid
from django.db import models

class EncomendaItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    encomenda_id = models.UUIDField(null=True, blank=True)  # ID da encomenda
    produto_id = models.UUIDField(null=True, blank=True)  # ID do produto
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    desconto = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    taxa_iva = models.DecimalField(max_digits=5, decimal_places=2)
    total_linha = models.DecimalField(max_digits=10, decimal_places=2)
    usuario_id = models.UUIDField(null=True, blank=True)  # ID do usuário que criou a encomenda

    def __str__(self):
        return f"Item {self.id} - Encomenda {self.encomenda_id} - Produto {self.produto_id}"