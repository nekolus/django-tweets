from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

from posts import views

urlpatterns = patterns('',
                        url(r'^$', views.index, name='index'),
                        url(r'^new/', views.new, name='new'),
                        url(r'^logout/$', views.logout_view, name='logout'),
                        
)