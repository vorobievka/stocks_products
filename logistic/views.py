from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class CustomSearchFilter(SearchFilter):
    def get_search_fields(self, view, request):
        print('params: ', request.query_params)
        if request.query_params.get('search'):
            return['positions__product__title', 'positions__product__description']
        return super().get_search_fields(view, request)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description', ]


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = [DjangoFilterBackend, CustomSearchFilter]
    filterset_fields = ['products', ]

