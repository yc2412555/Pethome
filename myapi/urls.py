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

from maggieapp.views import UsersViewSet, login_by_username, send_code_by_email
from myapi.views import *

urlpatterns = [
    # path('mobile_code/<str:tel>/', send_code_by_sms),
    path('mystars/',UserFollowerView.as_view())

]

router = DefaultRouter()
router.register('stars', UserFlowingView)

#?token=eb79ac1a-a22d-11e9-a54b-0027136a1c48

urlpatterns += router.urls
