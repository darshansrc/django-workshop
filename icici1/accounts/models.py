from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    aadhar_no = models.CharField(max_length=12, unique=True)
    phone = models.CharField(max_length=10)
    account_number = models.PositiveIntegerField(unique=True)

    def save(self, *args, **kwargs):
        if not self.account_number:
            last_customer = Customer.objects.order_by('-account_number').first()
            self.account_number = 8000 if not last_customer else last_customer.account_number + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
