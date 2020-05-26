from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.go_to_homepage, name='cart_detail'),
]