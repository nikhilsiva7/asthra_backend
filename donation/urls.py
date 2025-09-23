from django.urls import path
from .views import (
    DonationListCreateView,
    DonationStatsView,
    SimulatePaymentView
)

urlpatterns = [
    path('donations/', DonationListCreateView.as_view(), name='donation-list-create'),
    path('donations/stats/', DonationStatsView.as_view(), name='donation-stats'),
    path('donations/simulate/<int:donation_id>/', SimulatePaymentView.as_view(), name='simulate-payment'),
]