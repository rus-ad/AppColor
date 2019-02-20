from django.conf.urls import url
from .views import IndexView, ResView


urlpatterns = [
    url(r'^color/$', IndexView, name='index'),
    url(r'^color/result/$', ResView, name='result'),
]
