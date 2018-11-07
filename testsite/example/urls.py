from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.example, name='example'),
    url(r'^/your-name/$', views.get_name, name='your-name'),
]
