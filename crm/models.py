from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20,null=True,blank=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    
    # Gym-specific fields
    MEMBERSHIP_CHOICES = [
        ('basic', 'Basic'),
        ('premium', 'Premium'),
        ('vip', 'VIP'),
    ]
    membership_type = models.CharField(max_length=10, choices=MEMBERSHIP_CHOICES, default='basic')
    membership_start_date = models.DateField(null=True, blank=True)
    membership_end_date = models.DateField(null=True, blank=True)
    is_active_member = models.BooleanField(default=True)
    emergency_contact = models.CharField(max_length=100, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
