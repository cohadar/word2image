from rest_framework import serializers
from .models import Word2image


class word2imageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Word2image
        fields = '__all__'
