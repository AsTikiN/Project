from django.urls import path
from . import views
urlpatterns = [
    path('', views.index ),
    path('photoes', views.photoes_list)
]
