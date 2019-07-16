from django.contrib.auth.models import AnonymousUser
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import BasePermission

from common.models import UserToken


# class CustomAuthentication(BaseAuthentication):
#
#     def authenticate(self, request):
#         token = request.query_params.get('token')
#         if token:
#             try:
#                 usertoken = UserToken.objects.filter(token=token).only('token').first()
#                 user = usertoken.user
#                 return user, token
#             except Exception:
#                 pass
#         raise AuthenticationFailed('请先登录！')


class AllowGetAuthentication(BaseAuthentication):

    def authenticate(self, request):
        if request.method == 'GET':
            return None, None


class AllowPostAuthentication(BaseAuthentication):

    def authenticate(self, request):
        if request.method == 'POST':
                return None, None


# class CustomAuthorization(BasePermission):
#
#     def has_permission(self, request, view):
#         if not request.user or isinstance(request.user, AnonymousUser):
#             return True
#         for role in request.user.roles.all():
#             for permission in role.permissions.all():
#                 if permission.method == request.method and \
#                         permission.url == request.path:
#                     return True
#         return False


class DynamicsAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.query_params.get('token')
        if token:
            try:
                usertoken = UserToken.objects.filter(token=token).only('token').first()
                if usertoken:
                    user = usertoken.user
                    return user, token
                else:
                    raise AuthenticationFailed('请提供有效的身份认证！')
            except Exception:
                raise AuthenticationFailed('请提供有效的身份认证！')
        else:
            if request.method == 'GET':
                return None
            else:
                raise AuthenticationFailed('请提供有效的身份认证！')


class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # 从查询参数获取token
        token = request.query_params.get('token')
        # 如果拿到
        if token:
            try:
                usertoken = UserToken.objects.get(token=token)
                if usertoken:
                    # 通过token拿到与之相关的唯一的user
                    user = usertoken.user
                    return user, token
                #未获取与token相应的usertoken对象，或者未获取到token，则返回403，并提示
                else:
                    raise AuthenticationFailed('请提供有效的身份认证！')
            except Exception:
                raise AuthenticationFailed('请提供有效的身份认证！')
        else:
            raise AuthenticationFailed('请提供有效的身份认证！')