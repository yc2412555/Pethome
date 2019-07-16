from django.shortcuts import render

# Create your views here.
from rest_framework import status

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from common.models import *
from myapi.auths import CustomAuthentication
from myapi.serializers import *


class UserFlowingView(ModelViewSet):
    """查看我的关注"""
    # queryset = UserFlowing.objects.all().prefetch_related('userid')
    queryset = UserFlowing.objects.all()
    serializer_class = UserFlowingSeralizer
    authentication_classes = (CustomAuthentication,)

    def get_queryset(self):
        if self.request.query_params.get('token'):
            queryset = self.queryset.filter(userid=self.request.user.u_id)
            return queryset

    def create(self, request, *args, **kwargs):
        following_id = self.request.query_params.get('u_id')
        userid = self.request.user.u_id
        if following_id:
            user_following = UserFlowing() #关注表
            user_follower = UserFollower() #粉丝表
            user_follower.follower_id = following_id #粉丝表的粉丝id
            user_follower.userid = userid
            user_follower.save()
            user_following.following_id =following_id
            user_following.userid = userid
            user_following.status = 1
            user_following.save()
            data = {'detail':'关注成功'}
            return Response(status=status.HTTP_200_OK,data=data)
        else:
            data = {'detail': '请提供有效的关注对象'}
            return Response(status=status.HTTP_403_FORBIDDEN,data=data)

    def destroy(self, request, *args, **kwargs):
        # following_id = self.request.query_params.get('u_id')
        # userid = self.request.user.u_id
        # if following_id and userid:
        #     user_following = UserFlowing()
        #     user_following.status = 0
        #     user_following.save()
        instance = self.get_object()
        instance.status = 0
        instance.save()
        followingid = instance.following_id #删除的关注用户id
        user_flower = UserFollower.objects.filter(userid=followingid).first()
        user_flower.status = 0
        user_flower.save()
        data = {'detail':'删除成功'}
        return Response(status=status.HTTP_200_OK,data=data)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            self.serializer_class = UserFlowingDetailSeralizer
        # elif self.action == 'post':
        #     self.serializer_class = UserFlowingPostSeralizer
        return self.serializer_class

class UserFollowerView(ListAPIView):
    """查看我的粉丝"""
    queryset = UserFollower.objects.all()
    serializer_class = UserFollowerSerilizer
    authentication_classes = (CustomAuthentication,)

    def get_queryset(self):
        userid = self.request.user.u_id
        queryset = self.queryset.filter(userid=userid)
        return queryset


