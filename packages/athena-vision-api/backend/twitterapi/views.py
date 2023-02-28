from rest_framework.response import Response
from rest_framework.views import APIView

from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.helpers import complete_social_login

from django.views import View
from django.shortcuts import redirect

from os import getenv
from dotenv import load_dotenv
load_dotenv()


class TwitterLoginView(View):
    def get(self, request):
        # Create the Twitter OAuth2 adapter
        client = OAuth2Client(
            consumer_key=getenv("T_API_KEY"),
            consumer_secret=getenv("T_API_KEY_SECRET"),
            access_token_method='POST',
            access_token_url='https://api.twitter.com/oauth/access_token',
            callback_url='http://localhost:8000/accounts/twitter/login/callback/',
            scope=['read'],
            request=request
        )
        # redirect_url = client.get_redirect_url()
        # Redirect the user to the Twitter OAuth2 login page
        return redirect("redirect")


class TwitterRedirectView(APIView):
    def get(self, request):
        # Complete the social login process
        adapter = TwitterOAuthAdapter(request)
        client = OAuth2Client(consumer_key=getenv("T_API_KEY"),
                              consumer_secret=getenv("T_API_KEY_SECRET"),
                              access_token_method='POST',
                              access_token_url='https://api.twitter.com/oauth/access_token',
                              callback_url='http://localhost:8000/accounts/twitter/login/callback/',
                              scope=['read'],
                              request=request)
        token = client.get_access_token()
        login = complete_social_login(request, token)
        return Response({
            "token": token,
            "login": login
        })
