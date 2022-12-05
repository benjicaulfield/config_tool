from rest_framework import serializers
from .models import Unit, Topic, Content
from django.db import models 

class UnitSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Unit
        fields = '__all__'

class TopicSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Topic
        fields = '__all__'

class ContentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Content
        fields = '__all__'

