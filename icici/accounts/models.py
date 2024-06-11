from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    aadhar_no = models.CharField(max_length=12, unique=True)
    phone = models.CharField(max_length=10)
    account_number = models.PositiveIntegerField(unique=True)

    def save(self, *args, **kwargs):
        if not self.account_number:
            last_customer = Customer.objects.all().order_by('account_number').last()
            if last_customer:
                self.account_number = last_customer.account_number + 1
            else:
                self.account_number = 8000
        super(Customer, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.account_number}"
