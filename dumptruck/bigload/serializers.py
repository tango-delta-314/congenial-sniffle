
from rest_framework import serializers
from bigload.models import Trash


class TrashSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trash
        fields = ['id', 'title', 'contents']
