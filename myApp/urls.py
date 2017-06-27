from django.conf.urls import url, include
from . import views
from django.views.generic import TemplateView
from myApp.views import AboutView

urlpatterns = [
    url(r'^helloo/(?P<iddhanraj>\d+)/$', views.hello),
    url(r'^Login/$', views.login,name='Login'),
    url(r'^connection/$', AboutView.as_view()),
]