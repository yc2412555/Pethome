from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from common.models import DogArticle, CatArticle
from demopet.serializers import DomeDogSimpleSerializer, DomeCatSimpleSerializer


class DomeDogView(ListAPIView):
    queryset = DogArticle.objects.all()
    serializer_class = DomeDogSimpleSerializer
    pagination_class = PageNumberPagination


class DomeCatView(ListAPIView):
    queryset = CatArticle.objects.all()
    serializer_class = DomeCatSimpleSerializer
    pagination_class = PageNumberPagination

