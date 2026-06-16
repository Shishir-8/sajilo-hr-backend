from django.db import models
from accounts.models import User

class Employee(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    salary = models.FloatField()

    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)

    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username