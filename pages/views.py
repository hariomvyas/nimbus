from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


class TermsPageView(TemplateView):
    template_name = 'pages/terms.html'


class PrivacyPolicyPageView(TemplateView):
    template_name = 'pages/privacypolicy.html'


class ServiceView(TemplateView):
    template_name = 'services/services.html'
