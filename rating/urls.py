from django.conf.urls import url
from . import views


urlpatterns=[
    url('^$', views.index, name = 'index'),
    url(r'^myprofile$',views.profile,name='myprofile'),
    url(r'^profile/edit$',views.edit_profile,name='edit'),
    url(r'^project/new$', views.new_project, name='post'),
    url(r'^project/(?P<project_id>[0-9])$',views.project,name='project'),
]