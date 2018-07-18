from django.conf.urls import url
from register import views

urlpatterns = [
    url(r'^$', views.Login.as_view())
]