from rest_framework import serializers

from common.models import DogArticle


class DomeCatSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = DogArticle
        fields = ('article_id', 'article_title', 'article_pic', 'article_content')

class DomeDogSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = DogArticle
        fields = ('article_id', 'article_title', 'article_pic', 'article_content')