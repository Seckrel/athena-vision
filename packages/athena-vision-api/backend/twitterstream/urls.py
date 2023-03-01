from django.urls import path
from .views import Home

app_name = "twitter_stream"

urlpatterns = [
    path('', Home, name="home"),
]
