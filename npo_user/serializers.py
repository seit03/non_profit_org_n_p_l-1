from rest_framework import serializers
from npo_user.models import NPOUser


class NPOUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NPOUser
        fields = ('id',
                  'user_type',
                  'user_name',
                  'email',
                  'first_name',
                  'last_name',
                  'data_joined',
                  'is_active'
                  'is_staff',
                  'objects')