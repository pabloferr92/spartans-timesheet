from django.db import models

class Categoria(models.Model):
    categoria_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=5000, blank=True, null=True)
    criado_por = models.CharField(max_length=100)
    data_criacao = models.DateTimeField()
    atualizado_por = models.CharField(max_length=100)
    data_ultima_atualizacao = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'categoria'

    def __str__(self):
        return self.nome