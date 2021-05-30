from rest_framework import serializers

from .models import Card

class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = ['scheme','type','brand','prepaid','country','number','name','url','phone','city']