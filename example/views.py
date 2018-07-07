#from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.decorators import action
import django_filters
from rest_framework.response import Response

from .models import OpenWilson, CloseWilson
from .serializer import OpenWilsonSerializer, CloseWilsonSerializer
from .serializer import ResultOpenWilsonSerializer, ResultCloseWilsonSerializer


class Result(object):
    def __init__(self, *args, **kwargs):
        self.result_code = kwargs.get('result_code')
        self.error_code = kwargs.get('error_code')
        self.total_num = kwargs.get('total_num')
        self.info = kwargs.get('info')


class OpenWilsonViewSet(viewsets.ModelViewSet):
    queryset = OpenWilson.objects.all()
    serializer_class = OpenWilsonSerializer
    filter_fields = ('item_id', )


class CloseWilsonViewSet(viewsets.ModelViewSet):
    queryset = CloseWilson.objects.all()
    serializer_class = CloseWilsonSerializer
    filter_fields = ('item_id', )


class ResultViewSet(viewsets.ViewSet):
    pass


class ResultOpenWilsonViewSet(ResultViewSet):
    def list(self, request):
        try:
            queryset = OpenWilsonViewSet.as_view({'get': 'list'})(request._request).data
            self.result = Result(result_code=0, error_code=0, total_num=len(queryset), info=queryset)
            #raise Exception

        except:
            self.result = Result(result_code=-1, error_code=10, total_num=0, info=None)

        serializer = ResultOpenWilsonSerializer(self.result)
        return Response(serializer.data)


class ResultCloseWilsonViewSet(ResultViewSet):
    def list(self, request):
        try:
            queryset = info=CloseWilsonViewSet.as_view({'get': 'list'})(request._request).data
            self.result = Result(result_code=0, error_code=0, total_num=len(queryset), info=queryset)

        except:
            self.result = Result(result_code=-1, error_code=10, total_num=0, info=None)

        serializer = ResultCloseWilsonSerializer(self.result)
        return Response(serializer.data)
