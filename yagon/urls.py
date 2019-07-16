"""fangtx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rest_framework.routers import DefaultRouter

from yagon.views import DogVariesviewSet, CatVariesviewSet, DynamicsViewSet, pub_dynamic, TagsViewSet, \
    CommentsViewSet, CollectionViewSet, NiceViewSet

urlpatterns = [
    # path('mobile_code/<str:tel>/', send_code_by_sms),
    # path('token/', login_by_username),
    # path('comment/<int:comment_id>/', get_comment),
    path('dynamic/publishment/', pub_dynamic),
]

router = DefaultRouter()
router.register('dogsVaries', DogVariesviewSet)
router.register('catsVaries', CatVariesviewSet)
router.register('dynamics', DynamicsViewSet)
router.register('comments', CommentsViewSet)
router.register('tags', TagsViewSet)
router.register('collections', CollectionViewSet)
router.register('pride', NiceViewSet)



urlpatterns += router.urls
