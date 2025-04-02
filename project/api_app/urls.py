
from django.urls import path
from .views import fetch_hackernews_api_data
urlpatterns = [
    path('fetch_hacker_news/',fetch_hackernews_api_data,name='fetch_hacker_news' ),
]
