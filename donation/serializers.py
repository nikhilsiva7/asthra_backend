from rest_framework import serializers
from .models import Donation

class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ['id', 'donor', 'amount', 'message', 'timestamp', 'payment_status']
        read_only_fields = ['id', 'timestamp', 'donor', 'payment_status']