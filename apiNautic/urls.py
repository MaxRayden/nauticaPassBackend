from rest_framework.routers import DefaultRouter
from .views import PontoTuristicoViewSet, TipoBarcoViewSet, BarcoViewSet, ViagemViewSet, ClienteViewSet

router = DefaultRouter()
router.register(r'pontos-turisticos', PontoTuristicoViewSet, basename='ponto-turistico')
router.register(r'tipos-barco', TipoBarcoViewSet, basename='tipo-barco')
router.register(r'barcos', BarcoViewSet, basename='barco')
router.register(r'viagens', ViagemViewSet, basename='viagem')
router.register(r'clientes', ClienteViewSet, basename='cliente')  # Adicionando o ClienteViewSet

urlpatterns = router.urls
