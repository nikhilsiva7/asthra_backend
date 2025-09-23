from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Sum
from .models import Donation
from .serializers import DonationSerializer
from account.models import CustomUser  # your custom user model

class DonationListCreateView(generics.ListCreateAPIView):
    serializer_class = DonationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        donor_email = self.request.query_params.get('donor')
        if donor_email:
            return Donation.objects.filter(donor__email=donor_email).order_by('-timestamp')
        return Donation.objects.all().order_by('-timestamp')

    def perform_create(self, serializer):
        serializer.save(donor=self.request.user)

class DonationStatsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        total = Donation.objects.aggregate(total_amount=Sum('amount'))['total_amount'] or 0
        return Response({'total_donations': total})

class SimulatePaymentView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, donation_id):
        try:
            donation = Donation.objects.get(id=donation_id, donor=request.user)
            donation.payment_status = 'Success'
            donation.save()
            return Response({'message': 'Payment simulated successfully'}, status=status.HTTP_200_OK)
        except Donation.DoesNotExist:
            return Response({'error': 'Donation not found'}, status=status.HTTP_404_NOT_FOUND)