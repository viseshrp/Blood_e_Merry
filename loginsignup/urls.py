from django.conf.urls import url
from django.contrib.auth.views import login, logout

from . import views

app_name = 'loginsignup'
urlpatterns = [
    # ex: /home/
    url(r'^$', views.home, name='home'),
    # ex: /home/signup/
    url(r'^signup/$', views.signup, name='signup'),
    # ex: /home/confirmation/
    url(r'^confirmation/$', views.confirmation, name='confirmation'),
    # ex: /home/login/
    url(r'^login/$', login, {'template_name': 'loginsignup/login.html'}, name='login'),
    # ex: /home/logout/
    url(r'^logout/$', logout, {'template_name': 'loginsignup/logout.html'}, name='logout'),
]
