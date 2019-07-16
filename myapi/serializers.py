from rest_framework import serializers
from rest_framework.serializers import *

from common.models import *

class UserSimpeSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('u_name','tel','icon','sign','sex')

class UserFlowingSeralizer(ModelSerializer):
    """我的关注"""
    following_id = UserSimpeSerializer
    class Meta:
        model = UserFlowing
        fields = ('following_id',)

class UserFlowingDetailSeralizer(ModelSerializer):


    class Meta:
        model = UserFlowing
        fields = '__all__'



class CollectionSerilizer(ModelSerializer):

    class Meta:
        model = Collection
        fields = '__all__'

class CollectionDetailSerilizer(ModelSerializer):

    class Meta:
        model = Collection
        fields = '__all__'

class UserFollowerSerilizer(ModelSerializer):
    follower_id = serializers.SerializerMethodField()

    @staticmethod
    def get_follower_id(userfollower):
        queryset = User.objects.filter(u_id = userfollower.userid).first()
        return UserSimpeSerializer(queryset).data

    class Meta:
        model = UserFollower
        exclude = ('userid',)