from django.urls import path
from .views import TwitterLoginView, TwitterRedirectView

urlpatterns = [
    path('twitter/', TwitterLoginView.as_view(), name="login"),
    path('twitter/redirect', TwitterRedirectView.as_view(), name="redirect")
]
