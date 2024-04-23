from django.urls import path
# from django.conf.urls import url
from . import views
from django.urls import re_path
app_name = 'sentiment_or_emotion'

urlpatterns = [
    re_path(r'^$', views.choose_sentiment_or_emotion, name="choose_sentiment_or_emotion"),
]