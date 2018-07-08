from rest_framework import serializers

from .models import OpenWilson, CloseWilson


class OpenWilsonSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenWilson
        fields = ('item_id', 'open_date', 'status')


class CloseWilsonSerializer(serializers.ModelSerializer):
    class Meta:
        model = CloseWilson
        fields = ('item_id', 'close_date')


class OpenCloseWilsonSerializer(serializers.Serializer):
    item_id = serializers.CharField(max_length=8)
    open_date = serializers.DateTimeField()
    status = serializers.CharField(max_length=100)
    close_date = serializers.DateTimeField()


class ResultSerializer(serializers.Serializer):
    result_code = serializers.IntegerField()
    error_code = serializers.IntegerField()
    total_num = serializers.IntegerField()
    item_id = serializers.CharField(max_length=8)
    info = serializers.Serializer


class ResultOpenWilsonSerializer(ResultSerializer):
    info = OpenWilsonSerializer(many=True)


class ResultCloseWilsonSerializer(ResultSerializer):
    info = CloseWilsonSerializer(many=True)


class ResultWilsonSerializer(ResultSerializer):
    info = OpenCloseWilsonSerializer(many=True)
