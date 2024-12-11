from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import PontoTuristico, TipoBarco, Barco, Viagem, Cliente
from .serializers import (
    PontoTuristicoSerializer,
    TipoBarcoSerializer,
    BarcoSerializer,
    ViagemSerializer,
    ClienteSerializer
)

class PontoTuristicoViewSet(ModelViewSet):
    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer

class TipoBarcoViewSet(ModelViewSet):
    queryset = TipoBarco.objects.all()
    serializer_class = TipoBarcoSerializer

class BarcoViewSet(ModelViewSet):
    queryset = Barco.objects.all()
    serializer_class = BarcoSerializer

class ViagemViewSet(ModelViewSet):
    queryset = Viagem.objects.all()
    serializer_class = ViagemSerializer

    @action(detail=True, methods=['get'])
    def viagens_disponiveis(self, request, pk=None):
        ponto_turistico = self.get_object()
        viagens = Viagem.objects.filter(ponto_turistico=ponto_turistico, is_active=True)
        serializer = self.get_serializer(viagens, many=True)
        return Response(serializer.data)

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
