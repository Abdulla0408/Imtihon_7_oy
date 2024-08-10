from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Xodimlar(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=250)
    age = models.IntegerField()
    lavozim = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.first_name


class Davomat(models.Model):
    xodim = models.ForeignKey(Xodimlar, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.xodim.first_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username



