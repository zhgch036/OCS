from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.login,name='login'),
    url(r'^login_test/$', views.login_test,name='login_test'),
    url(r'^register_test',views.register_test,name='register_test'),
]