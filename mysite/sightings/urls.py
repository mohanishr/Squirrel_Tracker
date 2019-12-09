
from django.urls import path, re_path
from . import views

urlpatterns = [
            path('', views.index, name='index'),
            path('add/', views.add, name='add'),
            re_path(r'(?P<usid>[0-9]+[A-Z]-[A-Z]{2}-[0-9]{4}-[0-9]{2})/$', views.sqid, name='usid'),]
