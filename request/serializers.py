from rest_framework import serializers
from request.models import Data


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ('title', 'date', 'url', 'hd_url', 'concepts', 'type', 'explanation',)
