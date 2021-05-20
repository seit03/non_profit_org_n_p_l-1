from rest_framework import serializers

from npo_publication.models import Publication


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ('id',
                  'title',
                  'description',
                  'created_date',
                  'file')


class PublicationFavoriteSerializer(serializers.ModelSerializer):
    publication = PublicationSerializer(many=False, read_only=True)
    publication_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = PublicationSerializer
        fields = '__all__'