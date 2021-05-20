from rest_framework import serializers

from npo_law.models import NPOLaw


class NPOLawSerializer(serializers.ModelSerializer):
    class Meta:
        model = NPOLaw
        fields = ('id',
                  'title',
                  'description',
                  'created_date',
                  'file')


class NPOLawFavoriteSerializer(serializers.ModelSerializer):
    npolaw = NPOLawSerializer(many=False, read_only=True)
    npolaw_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = NPOLawSerializer
        fields = '__all__'