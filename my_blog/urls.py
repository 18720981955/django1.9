"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#from django.conf.urls import patterns, url
#from django.conf.urls import url
#from django.contrib import admin
#
#urlpatterns = [
#    url(r'^admin/', admin.site.urls),
#]
from django.conf.urls import include,url
from django.contrib import admin
from article import views
urlpatterns = [
    #url(r'^$', 'my_blog.views.home'),
    #url(r'^$', 'article.views.home'),
    url(r'^admin/',include(admin.site.urls)),
    url(r'^$', views.home),
    url(r'^(?P<my_args>\d+)/$',views.detail, name='detail'),
    url(r'^test/$',views.test, name='test'),
]
