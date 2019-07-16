from django.contrib.auth.models import AnonymousUser
from django.db import transaction
from django.db.transaction import atomic
from django.http import JsonResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from yagon.auths import CustomAuthentication, DynamicsAuthentication
from common.models import DogVari, CatVari, Dynamic, Comment, Tag, DynamicTag, Photo, Collection, Nice
from yagon.filters import  CommentsFilter
from yagon.serializers import DogVariesSerializer, CatVariesSerializer, DynamicsSerializer, TagsSerializer, \
    CommentsSerializer, DynamicsUpdateSerializer, CommentsCreateViewSet, CollectionSerializer, NiceSimpleSerializer, \
    NicePostSerializer


class DogVariesviewSet(ModelViewSet):
    '''狗狗种类视图类'''
    queryset = DogVari.objects.all().order_by('-dog_vari_name')#通过‘dog_vari_name’排序
    serializer_class = DogVariesSerializer
    pagination_class = None     #不分页


class CatVariesviewSet(ModelViewSet):
    '''猫猫种类视图类'''
    queryset = CatVari.objects.all()
    serializer_class = CatVariesSerializer
    pagination_class = None

class DynamicsViewSet(ModelViewSet):
    '''动态视图类'''
    # queryset: 筛选动态里公开的的动态
    # 当status为0时，动态不可查看。（被删除）
    queryset = Dynamic.objects.filter(status=1, is_public=1)
    serializer_class = DynamicsSerializer
    # filter_backends = (DjangoFilterBackend,)
    #     # filter_class = DynamicsFilter
    authentication_classes = (DynamicsAuthentication,)

    def get_queryset(self):
        '''获取查询集'''
        # 如果是你匿名用户，返回当前查询集
        #如果是通过认证的用户，返回该用户的相关的查询集
        if isinstance(self.request.user, AnonymousUser):
            return self.queryset
        return Dynamic.objects.filter(user=self.request.user, status=1)

    def destroy(self, request, *args, **kwargs):
        '''重构删除方法'''

        #用户点击删除，更改动态的status属性为0。
        instance = self.get_object()
        instance.status = 0
        instance.save()
        return Response(status=status.HTTP_200_OK, data={"detail": "删除成功！"})

    def update(self, request, *args, **kwargs):
        '''更改动态'''
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        message = {"detail":"修改成功！"}
        return Response(status=status.HTTP_200_OK,data=message)


    def get_serializer_class(self):
        '''根据不同的action，执行不同的序列化类'''
        if self.action == 'update':
            return DynamicsUpdateSerializer
        else:
            return self.serializer_class


class CommentsViewSet(ModelViewSet):
    '''评论的视图类'''
    queryset = Comment.objects.filter(status=1)
    serializer_class = CommentsSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = CommentsFilter
    authentication_classes = (CustomAuthentication,)

    def get_queryset(self):
        '''匿名用户'''
        if isinstance(self.request.user, AnonymousUser):
            return self.queryset
        return self.queryset.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'create':
            return CommentsCreateViewSet
        return self.serializer_class

    def create(self, request, *args, **kwargs):
        '''新增回复'''
        #需要查询参数d_id, c_id，并且需要消息体data携带c_tontent
        d_id = self.request.query_params.get('d_id')
        c_id = self.request.query_params.get('c_id')
        c_content = self.request.data.get('c_content')
        #如果从查询参数中获取d_id（需要回复的动态id）
        if d_id:
            #从数据库去获取与该动态id匹配并且公开的动态实例
            dynamic = Dynamic.objects.filter(d_id=d_id, status=1, is_public=1).first()
            if dynamic:
                # 如果实例存在，则添加回复
                Comment.objects.create(dynamic=dynamic, c_content=c_content, user=self.request.user)
                data = {"detail": '回复成功！'}
                return Response(status=status.HTTP_200_OK, data=data)
            else:
                #如果实例不存在， 返回404，并提示
                data = {"detail": "动态已删除或设为私密。"}
                return Response(status=status.HTTP_404_NOT_FOUND, data=data)

        #如果查询参数中拿不到d_id，就尝试去拿c_id（要回复的评论id）
        elif c_id:
            #如果拿到c_id，则在数据库匹配实例
            com_c = Comment.objects.filter(c_id=c_id, status=1).first()
            if com_c:
                # 如果实例存在，则新增评论，并提示
                Comment.objects.create(com_c=com_c, c_content=c_content, user=self.request.user)
                data = {"detail": '回复成功！'}
                return Response(status=status.HTTP_200_OK, data=data)
            #如果实例不存在，返回404，并提示
            else:
                data = {"detail": "评论已删除"}
                return Response(status=status.HTTP_404_NOT_FOUND, data=data)
        else:
            #如果既没有d_id, 也没有c_id，则返回403， 并提示
            data = {"detail": '请提供有效的回复信息！'}
            return Response(status=status.HTTP_400_BAD_REQUEST, data=data)

    def destroy(self, request, *args, **kwargs):
        '''重构删除函数'''
        instance = self.get_object()
        instance.status = 0
        instance.save()
        return Response(status=status.HTTP_200_OK, data={"detail": "删除成功！"})


class TagsViewSet(ModelViewSet):
    '''标签试图类'''
    queryset = Tag.objects.all()
    serializer_class = TagsSerializer
    pagination_class = None


class CollectionViewSet(ModelViewSet):
    '''动态收藏试图类'''
    queryset = Collection.objects.filter(status=1).only('status')
    serializer_class = CollectionSerializer
    # pagination_class = None
    authentication_classes = (CustomAuthentication,)#指定认证类

    def get_queryset(self):
        if isinstance(self.request.user, AnonymousUser):
            return self.queryset
            # list1 = []
            # return list1
        return self.queryset.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        # 新增收藏
        d_id = self.request.query_params.get('d_id')
        if d_id:
            dynamic = Dynamic.objects.filter(d_id=d_id, status=1, is_public=1).first()
            if dynamic:
                Collection.objects.create(dynamic=dynamic, user=self.request.user)
                data = {"detail": '收藏成功！'}
                return Response(status=status.HTTP_200_OK, data=data)
            else:
                data = {"detail": "动态不存在或设为私密。"}
                return Response(status=status.HTTP_404_NOT_FOUND, data=data)
        else:
            data = {"detail": '请提供有效收藏信息！'}
            return Response(status=status.HTTP_400_BAD_REQUEST, data=data)

    def destroy(self, request, *args, **kwargs):
        '''删除收藏'''
        instance = self.get_object()
        instance.status = 0
        instance.save()
        return Response(status=status.HTTP_200_OK, data={"detail": "删除成功！"})


class NiceViewSet(ModelViewSet):
    queryset = Nice.objects.filter(status=1)
    serializer_class = NiceSimpleSerializer
    # pagination_class = None
    authentication_classes = (CustomAuthentication,)

    def get_serializer_class(self):
        if self.action == 'POST':
            return NicePostSerializer
        else:
            return self.serializer_class

    def create(self, request, *args, **kwargs):
        '''点赞'''
        d_id = self.request.query_params.get('d_id')
        c_id = self.request.query_params.get('c_id')
        if d_id:
            dynamic = Dynamic.objects.filter(d_id=d_id).first()
            if dynamic:
                Nice.objects.create(dynamic=dynamic, user=self.request.user)
                data = {"detail": '点赞成功！'}
                return Response(status=status.HTTP_200_OK, data=data)
            else:
                data = {"detail": "未找到。"}
                return Response(status=status.HTTP_404_NOT_FOUND, data=data)
        elif c_id:
            comment = Comment.objects.filter(c_id=c_id).first()
            if comment:
                Nice.objects.create(comment=comment, user=self.request.user)
                data = {"detail": '点赞成功！'}
                return Response(status=status.HTTP_200_OK, data=data)
            else:
                data = {"detail": "未找到。"}
                return Response(status=status.HTTP_404_NOT_FOUND, data=data)
        else:
            data = {"detail": '请提供有效的点赞信息！'}
            return Response(status=status.HTTP_400_BAD_REQUEST, data=data)

    def destroy(self, request, *args, **kwargs):
        '''取消点赞'''
        instance = self.get_object()
        instance.status = 0
        instance.save()
        return Response(status=status.HTTP_200_OK, data={"detail": "取消点赞成功！"})




def get_comment(request, comment_id):
    if request.method == 'GET':
        queryset = Comment.objects.filter(c_id=comment_id).order_by('-c_time')
        comment_list = []
        comment_serializer = {}
        for comment in queryset:
            user = comment.user
            u_name = user.u_name
            c_content = comment.c_content
            c_counts = comment.c_counts
            comment_serializer['u_name'] = u_name
            comment_serializer['c_content'] = c_content
            comment_serializer['c_counts'] = c_counts
            comment_list.append(comment_serializer)
        data = {'code': 200, 'comments': comment_list}
        return JsonResponse(data)


@api_view(['POST'])
@authentication_classes((CustomAuthentication,))
@csrf_exempt
def pub_dynamic(request):
    '''发布动态'''
    if request.method == 'POST':
        user = request.user
        if user:
            #事务
            dynamic = Dynamic()
            # 此处省略对text_content，is_public的验证
            text_content = request.data.get('text_content')
            is_public = request.data.get('is_public')
            dynamic.text_content = text_content
            dynamic.is_public = is_public
            dynamic.user = user
            dynamic.save()
            t_id_list = request.data.get('t_id')
            path_list = request.data.get('path')
            if type(t_id_list) == list and len(t_id_list) > 0:
                for tagid in t_id_list:
                    tag = Tag.objects.filter(t_id=tagid).first()
                    if tag:
                        dynamic_tag = DynamicTag()
                        dynamic_tag.dynamic = dynamic
                        dynamic_tag.tag = tag
                        dynamic_tag.save()
                    else:
                        transaction.rollback()
                if type(path_list) == list and len(path_list) > 0:
                    for path in path_list:
                        #此处暂未对图片地址进行判断
                        photo = Photo()
                        photo.d = dynamic
                        photo.p_path = path
                        photo.save()
                        transaction.commit()
                        data = {"code": 200, "detail": '发布成功！'}
            else:
                transaction.rollback()
        else:
            data = {"code": 403, "detail": '请提供有效的身份验证'}
        return JsonResponse(data)














