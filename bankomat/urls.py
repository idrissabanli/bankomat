from django.urls import path
from .views import CheckAPIView


urlpatterns = [
    path('check/', CheckAPIView.as_view(), name="check")
]