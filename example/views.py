#from django.shortcuts import render
from rest_framework import viewsets, filters
import django_filters

from .models import OpenWilson, CloseWilson
from .serializer import OpenWilsonSerializer, CloseWilsonSerializer


class OpenWilsonViewSet(viewsets.ModelViewSet):
    queryset = OpenWilson.objects.all()
    serializer_class = OpenWilsonSerializer


class CloseWilsonViewSet(viewsets.ModelViewSet):
    queryset = CloseWilson.objects.all()
    serializer_class = CloseWilsonSerializer
