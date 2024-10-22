from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
# Create your models here.
class User(AbstractUser):
    mobile_number = models.CharField(max_length=13)

# stores the name of the bill and total amount.
class Expense(models.Model):
    name = models.CharField(max_length=200)
    total_bill = models.DecimalField(decimal_places=2,max_digits=12)
    # allowing users to choose split method
    class BillingMethod(models.TextChoices):
        exact = "EX","exact"
        equal = "EQ","equal"
        percentage = "PE","percentage"

    billing_method =models.CharField(max_length=2,choices=BillingMethod,default=BillingMethod.equal)

    def __str__(self):
        return self.name
# each user is associated with a expense and how much he owes.
class OwnedBy(models.Model):
    expense = models.ForeignKey(Expense,on_delete=models.CASCADE,related_name="owned_by",null=True,blank=True)
    username = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name="owes_to")
    owes = models.CharField(max_length=20)


    def __str__(self):
        return self.expense.name