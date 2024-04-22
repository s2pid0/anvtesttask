from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, related_name="custom_user_profile", null=True, on_delete=models.CASCADE)
    first_name = models.TextField(null=True, blank=True)
    contact = models.TextField(null=True, blank=True)
    exp = models.TextField()
    is_customer = models.BooleanField(default=False) #заказчик или исполнитель, по умолчанию исполнитель



    def __str__(self):
        return str(self.user)