from django.conf.urls import url
from . import views


urlpatterns=[
    url('^$', views.index, name = 'index'),
    url(r'^myprofile$',views.profile,name='myprofile'),
]