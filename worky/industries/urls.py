from django.conf.urls import url
from industries import views

urlpatterns = [
    url(r'^$', views.list_category)
]