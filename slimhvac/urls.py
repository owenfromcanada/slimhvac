from django.conf.urls import url
from hvac import views

urlpatterns = [
    url(r'^$', views.start_page, name='start'),
]