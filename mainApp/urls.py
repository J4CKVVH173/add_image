from django.conf.urls import url
from mainApp.views import index
from .views import Test
urlpatterns = [
    url(r'^$', index),
    url(r'test/$', Test.as_view()),
]
