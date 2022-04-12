from django.urls import path
from petstagramFinal.accounts.signals import *
from petstagramFinal.accounts.views import profile_view, sign_up, SignInView, sign_out

urlpatterns = [
    path('profile/<int:pk>', profile_view, name='profile view'),
    path('signup/', sign_up, name='sign up'),
    path('signin/', SignInView.as_view(), name='sign in'),
    path('signout/', sign_out, name='sign out'),
]
