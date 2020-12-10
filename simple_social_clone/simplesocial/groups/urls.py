from django.conf.urls import url
from django import views

app_name ='groups '

urlpatterns = [
    url(r'^$',views.ListGroups.as_view(),name='all'),
    url(r'^new/$',views.CreateGroup.as_view(),name='create'),
    url(r'posts/in/(?P<slug>[-\w]+)/$',views.SingleGroup.as_view(),name='single'),
    url(r'join/(?p<slug>[-\w]+)/$',views.JoinGroup.as_view(),name='join'),
    url(r'leave/(?p<slug>[-\w]+)/$',views.JoinGroup.as_view(),name='leave'),
]
