from rest_framework import serializers

from .models import Collection, WebTag


class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection
        fields = ('pk', 'title', 'description', 'created_at', 'modified_at')


class WebTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = WebTag
        fields = '__all__'
