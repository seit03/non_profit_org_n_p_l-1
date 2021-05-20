from rest_framework import serializers
from npo_news.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id',
                  'title',
                  'description',
                  'created_date',
                  'image',
                  'link')


class NewsFavoriteSerializer(serializers.ModelSerializer):
    news = NewsSerializer(many=False, read_only=True)
    news_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = NewsSerializer
        fields = '__all__'