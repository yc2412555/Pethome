from django.urls import path

from demopet.views import DomeDogView, DomeCatView

urlpatterns = [
    path('domesticate_dog/', DomeDogView.as_view()),
    path('domesticate_cat/',DomeCatView.as_view()),
]