from django.db.migrations import serializer

from npo_news.models import News


class NewsSerializer(serializer.ModelSerializer):
    class Meta:
        model = News
        fields = ('id',
                  'title',
                  'description',
                  'created_date',
                  'image',
                  'link')