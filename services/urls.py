from django.urls import path
from .views import ServicesView, ServicesDetailView

urlpatterns = [
    path('', ServicesView.as_view(), name='services'),
    path('<int:pk>/', ServicesDetailView.as_view(), name='services-detail'),
]
