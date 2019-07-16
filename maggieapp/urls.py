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

from maggieapp.views import UsersViewSet, login_by_username, send_code_by_email, login_by_email, CatDiseaseView, \
    MedicineView, DogDiseaseView

urlpatterns = [
    path('token/', login_by_username),
    path('emailToken/', login_by_email),
    path('emailCode/<str:email>/', send_code_by_email),
]

router = DefaultRouter()
router.register('users', UsersViewSet)
router.register('catDisease', CatDiseaseView)
router.register('dogDisease', DogDiseaseView)
router.register('medicine', MedicineView)
urlpatterns += router.urls
