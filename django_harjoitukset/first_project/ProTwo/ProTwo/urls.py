from django.conf.urls import url, include
from django.contrib import admin
from appTwo import views
#3 rivi ei toimi

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('appTwo.urls')),


]
