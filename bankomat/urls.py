from django.urls import path
from .views import CheckAPIView
# from .views import post


urlpatterns = [
    path('check/', CheckAPIView.as_view(), name="check")
    # path('check/', post, name="check")
]