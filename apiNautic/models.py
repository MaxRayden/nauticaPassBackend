from django.db import models

class ModelBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class PontoTuristico(ModelBase):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    localizacao = models.CharField(max_length=255)
    imagem = models.ImageField(upload_to='pontos_turisticos/', blank=True, null=True)

    def __str__(self):
        return self.nome

class TipoBarco(ModelBase):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Barco(ModelBase):
    nome = models.CharField(max_length=255)
    capacidade = models.PositiveIntegerField()
    tipo = models.ForeignKey(TipoBarco, on_delete=models.CASCADE, related_name='barcos')
    imagem = models.ImageField(upload_to='barcos/', blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.tipo.nome})"

class Viagem(ModelBase):
    barco = models.ForeignKey(Barco, on_delete=models.CASCADE, related_name='viagens')
    ponto_turistico = models.ForeignKey(PontoTuristico, on_delete=models.CASCADE, related_name='viagens')
    data_partida = models.DateTimeField()
    data_chegada = models.DateTimeField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.barco.nome} - {self.ponto_turistico.nome} ({self.data_partida} -> {self.data_chegada})"

class Cliente(ModelBase):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    cpf = models.CharField(max_length=11, unique=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nome
