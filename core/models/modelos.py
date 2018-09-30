from django.db import models


class Cliente(models.Model):
    cliente_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    criado_por = models.CharField(max_length=100)
    data_criacao = models.DateTimeField()
    atualizado_por = models.CharField(max_length=100)
    data_ultima_atualizacao = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'cliente'


class LancamentoHoras(models.Model):
    lancamento_horas_id = models.AutoField(primary_key=True)
    projeto = models.ForeignKey('Projeto', models.DO_NOTHING)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING)
    categoria = models.ForeignKey(Categoria, models.DO_NOTHING)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField(blank=True, null=True)
    descricao = models.CharField(max_length=5000, blank=True, null=True)
    criado_por = models.CharField(max_length=100)
    data_criacao = models.DateTimeField()
    atualizado_por = models.CharField(max_length=100)
    data_ultima_atualizacao = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'lancamento_horas'


class MembrosSquad(models.Model):
    membros_squad_id = models.AutoField(primary_key=True)
    squad = models.ForeignKey('Squad', models.DO_NOTHING)
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING)
    criado_por = models.CharField(max_length=100)
    data_criacao = models.DateTimeField()
    atualizado_por = models.CharField(max_length=100)
    data_ultima_atualizacao = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'membros_squad'


class Perfil(models.Model):
    perfil_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    criado_por = models.CharField(max_length=100)
    criado_em = models.DateTimeField()
    atualizado_por = models.CharField(max_length=100)
    data_ultima_atualizacao = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'perfil'


class Projeto(models.Model):
    projeto_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
    squad = models.ForeignKey('Squad', models.DO_NOTHING, blank=True, null=True)
    criado_por = models.CharField(max_length=100)
    data_criacao = models.DateTimeField()
    atualizado_por = models.CharField(max_length=100)
    data_ultima_atualizacao = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'projeto'


class Squad(models.Model):
    squad_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    administrador = models.ForeignKey('Usuario', models.DO_NOTHING)
    criado_por = models.CharField(max_length=100)
    data_criacao = models.DateTimeField()
    atualizado_por = models.CharField(max_length=100)
    data_ultima_atualizacao = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'squad'


class Usuario(models.Model):
    usuario_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=12, blank=True, null=True)
    email = models.CharField(max_length=100)
    perfil = models.ForeignKey(Perfil, models.DO_NOTHING)
    valor_hora = models.FloatField(blank=True, null=True)
    timezone = models.CharField(max_length=5)
    criado_por = models.CharField(max_length=100)
    data_criacao = models.DateTimeField()
    atualizado_por = models.CharField(max_length=100)
    data_ultima_atualizacao = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'usuario'
