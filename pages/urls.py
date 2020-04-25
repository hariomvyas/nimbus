from django.urls import path
from .views import HomePageView, AboutPageView, TermsPageView, PrivacyPolicyPageView, ServiceView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('terms&condition/', TermsPageView.as_view(), name='terms&condition'),
    path('privacypolicy/', PrivacyPolicyPageView.as_view(), name='privacypolicy'),
    path('services/', ServiceView.as_view(), name='services'),

]
