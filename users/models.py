from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    # username = models.EmailField(unique=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField()
    organization = models.CharField(max_length=250)
    username = models.CharField(max_length=250, unique=True)
    password = models.CharField(max_length=250)
    # password_confirmation = models.CharField(max_length=250)
    scientific_degree = models.CharField(max_length=250)
    anather_information = models.CharField(max_length=250)
    phone = models.CharField(max_length=13, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class PasswordResets(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    reset_code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = 'password_resets'
        unique_together = (('user', 'created_at'),)
        index_together = (('user', 'created_at'),)
        verbose_name = 'Password Reset'
        verbose_name_plural = 'Password Resets'



