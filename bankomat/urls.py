from django.urls import path
from .views import CheckAPIView, CashOutAPIView
# from .views import post


urlpatterns = [
    path('check/', CheckAPIView.as_view(), name="check"),
    path('cash-out/', CashOutAPIView.as_view(), name="cash-out")
]
