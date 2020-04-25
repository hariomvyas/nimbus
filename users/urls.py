from django.urls import path

from .views import SignupPageView, ProfilePageView, profile

urlpatterns = [
    path('signup/', SignupPageView.as_view(), name='signup'),
]
