from rest_framework import serializers
from .models import PontoTuristico, TipoBarco, Barco, Viagem, Cliente

class PontoTuristicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PontoTuristico
        fields = ['id', 'nome', 'descricao', 'localizacao', 'imagem', 'created_at', 'updated_at', 'is_active']

class TipoBarcoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoBarco
        fields = ['id', 'nome', 'created_at', 'updated_at', 'is_active']

class BarcoSerializer(serializers.ModelSerializer):
    tipo = TipoBarcoSerializer()

    class Meta:
        model = Barco
        fields = ['id', 'nome', 'capacidade', 'tipo', 'imagem', 'created_at', 'updated_at', 'is_active']

class ViagemSerializer(serializers.ModelSerializer):
    barco = BarcoSerializer()
    ponto_turistico = PontoTuristicoSerializer()

    class Meta:
        model = Viagem
        fields = ['id', 'barco', 'ponto_turistico', 'data_partida', 'data_chegada', 'preco', 'created_at', 'updated_at', 'is_active']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'email', 'telefone', 'cpf', 'endereco', 'created_at', 'updated_at', 'is_active']
