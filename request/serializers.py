from rest_framework import serializers
from request.models import Data


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ('title', 'created_date', 'url', 'hd_url', 'media_type', 'explanation', 'concepts')
