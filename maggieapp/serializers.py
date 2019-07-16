from django.core.cache import caches
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from common.models import User, Role, UserRole, CatDisease, Medicine, DogDisease
from maggieapp.utils import USERNAME_PATTERN, EMAIL_PATTERN, TEL_PATTERN, to_md5_hex, PASSWORD_PATTERN


class UserBasicSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('u_id', 'u_name', 'roles')


class UserPostSerializer(serializers.ModelSerializer):

    @staticmethod
    def validate_u_name(u_name):
        if not USERNAME_PATTERN.fullmatch(u_name):
            raise ValidationError('用户名格式不正确')
        username_from_db = User.objects.filter(u_name=u_name)
        if username_from_db:
            raise ValidationError('用户名已存在！')
        return u_name

    @staticmethod
    def validate_u_password(u_password):
        if not PASSWORD_PATTERN.fullmatch(u_password):
            raise ValidationError('密码错误')
        return u_password

    @staticmethod
    def validate_tel(tel):
        if not TEL_PATTERN.fullmatch(tel):
            raise ValidationError('手机号格式不正确')
        tel_from_db = User.objects.filter(tel=tel)
        if tel_from_db:
            raise ValidationError('手机号已存在！')
        return tel

    @staticmethod
    def validate_email(email):
        if not EMAIL_PATTERN.fullmatch(email):
            raise ValidationError('邮箱账号格式不正确')
        email_from_db = User.objects.filter(email=email)
        if email_from_db:
            raise ValidationError('邮箱账号已存在！')
        return email

    class Meta:
        model = User
        fields = ('u_name', 'u_password', 'tel', 'email', 'sex')


class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude =('password',)


class CatDiseaseSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = CatDisease
        fields = '__all__'


class MedicineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medicine
        fields = ('m_id', 'm_name','m_function' ,'m_explain', 'date', 'addr', 'manufacturer','price','qua_date')


class CatDiseaseDetailSerializer(serializers.ModelSerializer):
    medicine =serializers.SerializerMethodField()

    @staticmethod
    def get_medicine(catdisease):
        return MedicineSerializer(catdisease.medicine_set, many=True).data

    class Meta:
        model = CatDisease
        fields = ('cat_dis_id', 'dis_name', 'performace', 'medicine')


class DogDiseaseSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = DogDisease
        fields = '__all__'


class DogDiseaseDetailSerializer(serializers.ModelSerializer):
    medicine = serializers.SerializerMethodField()

    @staticmethod
    def get_medicine(dogdisease):
        return MedicineSerializer(dogdisease.medicine_set, many=True).data

    class Meta:
        model = DogDisease
        fields = ('dog_dis_id', 'dis_name', 'dis_code', 'performace', 'medicine')