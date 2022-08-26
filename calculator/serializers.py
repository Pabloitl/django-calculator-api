from rest_framework import serializers
from rest_framework.serializers import Serializer

class BinaryFloatSerializer(Serializer):
    first = serializers.FloatField()
    second = serializers.FloatField()
