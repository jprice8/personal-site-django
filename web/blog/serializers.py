from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = '__all__'
