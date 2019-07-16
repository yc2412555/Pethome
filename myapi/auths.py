import jwt
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from PetHome.settings import SECRET_KEY
from common.models import User, UserToken


class CustomAuthentication(BaseAuthentication):

    def authenticate(self, request):
        token = request.query_params.get('token')
        if token:
            try:
                # result = jwt.decode(token, SECRET_KEY, algorithm='HS256')
                # user = User.objects.get(u_id=result['data']['userid'])
                userT = UserToken.objects.filter(token=token).only('token').first()
                user=userT.user
                return user, token
            except Exception:
                raise AuthenticationFailed('....')
        raise AuthenticationFailed('请提供有效的身份认证标识')