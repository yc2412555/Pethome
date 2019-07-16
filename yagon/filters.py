import django_filters
from django.db.models import Q

from common.models import Dynamic, Comment


# class DynamicsFilter(django_filters.FilterSet):
#     class Meta:
#         model = Dynamic
#         fields = ('user',)


class CommentsFilter(django_filters.FilterSet):
    d_id = django_filters.NumberFilter(method='get_d_id', label='请输入动态id')
    c_id = django_filters.NumberFilter(method='get_c_id', label='请输入评论id')
    # u_id = django_filters.NumberFilter(method='get_u_id', label='请输入用户id')


    def get_d_id(self, queryset, name, value):
        return queryset.filter(dynamic=value)

    def get_c_id(self, queryset, name, value):
        return queryset.filter(com_c=value)

    # def get_u_id(self, queryset, name, value):
    #     return queryset.filter(user=value)

    class Meta:
        model = Comment
        fields = ('d_id', 'c_id')

