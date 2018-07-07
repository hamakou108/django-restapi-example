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


class ResultSerializer(serializers.Serializer):
    result_code = serializers.IntegerField()
    error_code = serializers.IntegerField()
    total_num = serializers.IntegerField()
    info = serializers.Serializer


class ResultOpenWilsonSerializer(ResultSerializer):
    info = OpenWilsonSerializer(many=True)


class ResultCloseWilsonSerializer(ResultSerializer):
    info = CloseWilsonSerializer(many=True)
