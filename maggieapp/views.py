import uuid
from django.core.cache import caches
from django.db.transaction import atomic
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from common.models import User, UserToken, CatDisease, Medicine, DogDisease
from maggieapp.serializers import UserBasicSerializer, UserPostSerializer, \
    CatDiseaseSimpleSerializer, CatDiseaseDetailSerializer, MedicineSerializer, DogDiseaseSimpleSerializer, \
    DogDiseaseDetailSerializer, UserUpdateSerializer
from maggieapp.utils import to_md5_hex, USERNAME_PATTERN, \
    PASSWORD_PATTERN, normalize_space, send_active_email, EMAIL_PATTERN, gen_email_code


@api_view(['POST'])
def login_by_email(request):
    email = request.data.get('email', None)
    email_code_from_request = request.data.get('email_code', None)
    if email and email_code_from_request:
        if EMAIL_PATTERN.fullmatch(email):
            email_from_caches = caches['default'].get(email)
            if email_code_from_request == email_from_caches:
                user = User.objects.filter(email=email).first()
                if user:
                    token = f'{uuid.uuid1()}'
                    UserToken.objects.update_or_create(
                        user=user, defaults={'token': token}
                    )
                    with atomic():
                        # 更新用户最近登录时间
                        cur_time = timezone.now()
                        if not user.lastvisit or (cur_time - user.lastvisit).days >= 7:  # 如果用户第一次或者登录日期超过7天
                            user.lastvisit = cur_time
                            user.save()
                    data = {'u_id': user.u_id, 'u_name': user.u_name, 'icon': user.icon, 'sign': user.sign}
                    hint = {'code': 10001, 'message': '用户登录成功', 'token': token, 'data': data}
                else:
                    hint = {'code': 10004, 'meassge': '邮箱账号不存在'}
            else:
                hint = {'code': 10003, 'meassge': '验证码错误'}
        else:
            hint = {'code': 10002, 'meassge': '邮箱格式不正确'}
    else:
        hint = {'code': 10002, 'meassge':'邮箱格式不正确'}
    return Response(hint)


@api_view(['GET'])
def send_code_by_email(request, email):
    if EMAIL_PATTERN.fullmatch(email):
        if caches['default'].get(email):
            data = {'code': 30001, 'message': '请不要在60秒以内重复发送邮箱验证码'}
        else:
            email_code = gen_email_code()
            send_active_email.delay((email,), email_code)
            caches['default'].set(email, email_code, timeout=60)
            data = {'code': 30000, 'message': '验证码已发送到您的邮箱'}
    else:
        data = {'code': 30002, 'message': '请提供有效的邮箱账号'}
    return Response(data)


@api_view(['POST'])
def login_by_username(request):
    username = request.data.get('username', None)
    password = request.data.get('password', None)
    if normalize_space(username) and normalize_space(password):
        username_valid = USERNAME_PATTERN.fullmatch(username)
        password_valid = PASSWORD_PATTERN.fullmatch(password)
        if username_valid and password_valid:
            password = to_md5_hex(password)
            user = User.objects.filter(u_name=username, u_password=password).first()
            if user:
                # 创建或更新令牌
                token = f'{uuid.uuid1()}'
                UserToken.objects.update_or_create(
                    user=user, defaults={'token': token}
                )
                with atomic():
                    # 更新用户最近登录时间
                    cur_time =timezone.now()
                    if not user.lastvisit or(cur_time - user.lastvisit).days >= 7: #如果用户第一次或者登录日期超过7天
                        user.lastvisit = cur_time
                        user.save()
                data = {'u_id': user.u_id, 'u_name': user.u_name, 'icon': user.icon, 'sign': user.sign}
                hint = {'code': 10001, 'message': '登录成功', 'token': token, 'data': data}
            else:
                hint = {'code': 10002, 'message': '用户名或密码错误'}
        else:
            hint = {'code': 10002, 'message': '用户名或密码错误'}
    else:
        hint = {'code': 10002, 'message': '用户名或密码错误'}
    return Response(hint)


class UsersViewSet(ModelViewSet):
    """用户注册"""
    queryset = User.objects.all()
    serializer_class = UserBasicSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return UserPostSerializer
        if self.action == 'update':
            return UserUpdateSerializer
        return self.serializer_class

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['u_password'] = to_md5_hex(serializer.validated_data['u_password'])
        user = User.objects.create(**serializer.validated_data)
        # role = Role.objects.get(r_id=1)
        # UserRole.objects.create(user=user, role=role)
        data = {'code': 201, 'message':"注册成功"}
        return Response(data, status=status.HTTP_201_CREATED)


class CatDiseaseView(ModelViewSet):
    """猫猫健康"""
    queryset = CatDisease.objects.all()
    serializer_class = CatDiseaseSimpleSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CatDiseaseDetailSerializer
        return self.serializer_class


class MedicineView(ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer


class DogDiseaseView(ModelViewSet):
    queryset = DogDisease.objects.all()
    serializer_class = DogDiseaseSimpleSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return DogDiseaseDetailSerializer
        return self.serializer_class


