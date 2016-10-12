from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^(?P<width>[0-9]+)/(?P<height>[0-9]+)/$', view=views.ImageAPIView.as_view(), name='get')
]
