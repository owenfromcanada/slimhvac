from django.conf.urls import url
from hvac import views

urlpatterns = [
    url(r'^$', views.start_page, name='start'),
    url(r'^thermostat/new$', views.new_thermostat, name='new_thermostat'),
    url(r'^thermostat/add$', views.add_thermostat, name='add_thermostat'),
]