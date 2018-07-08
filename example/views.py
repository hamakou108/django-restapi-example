from abc import ABC, abstractmethod

#from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.decorators import action
import django_filters
from rest_framework.response import Response

from .models import OpenWilson, CloseWilson
from .serializer import OpenWilsonSerializer, CloseWilsonSerializer
from .serializer import ResultOpenWilsonSerializer, ResultCloseWilsonSerializer, ResultWilsonSerializer


class Result(object):
    def __init__(self, *args, **kwargs):
        self.result_code = kwargs.get('result_code')
        self.error_code = kwargs.get('error_code')
        self.total_num = kwargs.get('total_num')
        self.item_id = kwargs.get('item_id')
        self.info = kwargs.get('info')


class OpenWilsonViewSet(viewsets.ModelViewSet):
    queryset = OpenWilson.objects.all()
    serializer_class = OpenWilsonSerializer
    filter_fields = ('item_id', )


class CloseWilsonViewSet(viewsets.ModelViewSet):
    queryset = CloseWilson.objects.all()
    serializer_class = CloseWilsonSerializer
    filter_fields = ('item_id', )


class ResultViewSet(ABC, viewsets.ViewSet):
    @abstractmethod
    def getQueryset(self, request):
        pass

    @abstractmethod
    def getSerializer(self, result):
        pass

    def list(self, request):
        try:
            queryset = self.getQueryset(request)
            result = Result(result_code=0, error_code=0, total_num=len(queryset), item_id=request.GET.get('item_id'), info=queryset)
            #raise Exception

        except:
            result = Result(result_code=-1, error_code=10, total_num=0, item_id=request.GET.get('item_id'), info=None)

        serializer = self.getSerializer(result)
        return Response(serializer.data)


class ResultOpenWilsonViewSet(ResultViewSet):
    def getQueryset(self, request):
        return OpenWilsonViewSet.as_view({'get': 'list'})(request._request).data

    def getSerializer(self, result):
        return ResultOpenWilsonSerializer(result)


class ResultCloseWilsonViewSet(ResultViewSet):
    def getQueryset(self, request):
        return CloseWilsonViewSet.as_view({'get': 'list'})(request._request).data

    def getSerializer(self, result):
        return ResultCloseWilsonSerializer(result)


class ResultWilsonViewSet(ResultViewSet):
    def getQueryset(self, request):
        open_datas = OpenWilsonViewSet.as_view({'get': 'list'})(request._request).data
        close_datas = CloseWilsonViewSet.as_view({'get': 'list'})(request._request).data
        result_datas = []
        for open_data in open_datas:
            for close_data in close_datas:
                if open_data['item_id'] == close_data['item_id']:
                    result_datas.append({'item_id': open_data['item_id'], 'open_date': open_data['open_date'], 'status': open_data['status'], 'close_date': close_data['close_date'] })
        return result_datas

    def getSerializer(self, result):
        return ResultWilsonSerializer(result)
