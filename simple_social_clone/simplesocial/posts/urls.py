from django.conf.urls import url
from django import views

app_name = 'posts'

urlpatterns = [
    url(r'^$',views.PostList.as_view(), name='all'),
    url(r'new/$',views.CreatePost.as_view(),name='create'),
    url(r'by/(?P<username>[-\w]+)',views.UserPosts.as_view(),name='for_user'),
    url(r'by/(?P<username>[-\w]+)/(?<pk>\d+)/$',views.PostsDetail.as_view(),name='single'),
    url(r'delete/(?<pk>\d+)/$',views.DeletePost.as_view(),name='delete')
]

#  File "C:\Users\juhani.jokitulppo\Desktop\simple_social_clone\simplesocial\posts\urls.py", line 7, in <module>
#    url(r'^$',views.PostList.as_view(),name='all'),
#AttributeError: module 'django.views' has no attribute 'PostList'
