


from django.db import models
from alumni.models import Alumni

class Donation(models.Model):
    donor = models.ForeignKey(Alumni, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    message = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=20, default='Pending')  # Simulated status

    def __str__(self):
        return f"{self.donor.email} donated ₹{self.amount} ({self.payment_status})"