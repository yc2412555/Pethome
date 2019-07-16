from rest_framework import serializers, status
from rest_framework.response import Response

from common.models import DogVari, DogPhoto, CatPhoto, Dynamic, User, Tag, Photo, Comment, CatVari, Collection, Nice


class DogPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DogPhoto
        fields = ('dp_id', 'dp_path')


class DogVariesSerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField()

    @staticmethod
    def get_photos(dogvari):
        queryset = DogPhoto.objects.filter(dogvari=dogvari)
        return DogPhotoSerializer(queryset, many=True).data


    class Meta:
        model = DogVari
        fields = '__all__'



class CatPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatPhoto
        fields = ('cp_id', 'path')


class CatVariesSerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField()

    @staticmethod
    def get_photos(catvari):
        queryset = CatPhoto.objects.filter(catvari=catvari)
        return CatPhotoSerializer(queryset, many=True).data

    class Meta:
        model = CatVari
        fields = '__all__'


class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("u_id", 'u_name', 'icon')


class TagSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('t_id', 't_content')


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = ('p_id', 'p_path')


class CommentSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('c_id', 'c_content')


class CommentsCreateViewSet(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('c_content',)


class DynamicsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dynamic
        fields = ('is_public',)


# class DynamicsCollectSerializer(serializers.ModelSerializer):
#     user = serializers.SerializerMethodField()
#     tags = serializers.SerializerMethodField()
#     path = serializers.SerializerMethodField()
#
#     @staticmethod
#     def get_user(dynamic):
#         return UserSimpleSerializer(dynamic.user).data
#
#     @staticmethod
#     def get_tags(dynamic):
#         return TagSimpleSerializer(dynamic.tags, many=True).data
#
#     @staticmethod
#     def get_path(dynamic):
#         queryset = Photo.objects.filter(d=dynamic)
#         return PhotoSerializer(queryset, many=True).data
#
#     class Meta:
#         model = Dynamic
#         fields = '__all__'


class DynamicsSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    path = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    nice = serializers.SerializerMethodField()


    @staticmethod
    def get_user(dynamic):
        return UserSimpleSerializer(dynamic.user).data

    @staticmethod
    def get_tags(dynamic):
        return TagSimpleSerializer(dynamic.tags, many=True).data

    @staticmethod
    def get_path(dynamic):
        queryset = Photo.objects.filter(d=dynamic)
        return PhotoSerializer(queryset, many=True).data

    @staticmethod
    def get_comments(dynamic):
        queryset = Comment.objects.filter(dynamic=dynamic)
        return CommentSimpleSerializer(queryset, many=True).data

    def get_nice(self, dynamic):
        queryset = Nice.objects.filter(status=1, dynamic=dynamic)
        return NiceSerializer(queryset, many=True).data

    class Meta:
        model = Dynamic
        exclude = ('status', 'is_public')


class DynamicSimpleSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    @staticmethod
    def get_user(dynamic):
        return UserSimpleSerializer(dynamic.user).data

    class Meta:
        model = Dynamic
        fields = ('d_id', 'text_content', 'user')


class CommentsSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    dynamic = serializers.SerializerMethodField()

    def get_user(self, comment):
        return UserSimpleSerializer(comment.user).data

    def get_dynamic(self, comment):
        return DynamicSimpleSerializer(comment.dynamic).data


    class Meta:
        model = Comment
        exclude = ('status', )


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('t_id', 't_content')


class CollectionSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    dynamic = serializers.SerializerMethodField()

    def get_user(self, collection):
        return UserSimpleSerializer(collection.user).data

    def get_dynamic(self, collection):
        queryset = Dynamic.objects.filter(status=1, is_public=1, d_id=collection.dynamic.d_id).first()
        if queryset is None:
            data = {"detail": "该动态已删除或者设为私密"}
            return data
        return DynamicsSerializer(queryset).data

    class Meta:
        model = Collection
        fields = ('col_id', 'user', 'dynamic')


class NiceSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, nice):
        return UserSimpleSerializer(nice.user).data

    class Meta:
        model = Nice
        fields = ('n_id', 'user')


class NiceSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Nice
        exclude = ('status',)


class NicePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Nice
        fields = ()


