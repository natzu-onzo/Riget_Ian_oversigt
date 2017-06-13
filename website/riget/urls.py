from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views


from . import views

app_name = 'riget'
urlpatterns = [
    url(r'^$', auth_views.login, name='login'),
#    url(r'^$', views.loginView.as_view(), name='login'),
    url(r'out/$', auth_views.logout, name ='logout'),
    url(r'home/$', views.homeView.as_view(), name='home'),
    url(r'fet/$', views.fetView.as_view(), name='fet'),
    url(r'fet/nyrecord/$',views.nyfetrecordView.as_view(), name='nyfetrecord'),
    url(r'fet/nyperson/$',views.nyfetpersonView.as_view(), name='nyfetperson'),
    url(r'pib/$', views.pibView.as_view(), name='pib'),
    url(r'viewpatient/(?P<CPR>\d+)/$', views.fetpatientView.as_view(), name='fetview'),
    url(r'fet/change/(?P<CPR>\d+)/$', views.changefetpatientView.as_view(), name='fetchang'),
    url(r'fet/rchange/(?P<CPR>\d+)/$', views.nyfetrecordView.as_view(), name='fetrchange'),
]
