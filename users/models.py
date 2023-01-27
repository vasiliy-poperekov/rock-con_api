from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    is_group_singer = models.BooleanField(default=False)
    is_place = models.BooleanField(default=False)

    def __str__(self):
        return self.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class GroupSinger(models.Model):
    user = models.OneToOneField(User, related_name="user_group_singer", on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    genres = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    profile_photo = models.ImageField(upload_to='images/', blank=True, null=True)
    image1 = models.ImageField(upload_to='images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='images/', blank=True, null=True)
    concerts = models.ManyToManyField("concert.Concert", related_name="group_concert", blank=True, null=True)
    social_networks = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "group_singer"
        verbose_name = "Группа/Исполнитель"
        verbose_name_plural = "Группы/Исполнители"

    def __str__(self):
        return self.user.username


class Place(models.Model):
    user = models.OneToOneField(User, related_name="user_place", on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=128, blank=True, null=True)
    phone_number = models.CharField(max_length=16, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    profile_photo = models.ImageField(upload_to='images', blank=True, null=True)
    image1 = models.ImageField(upload_to='images', blank=True, null=True)
    image2 = models.ImageField(upload_to='images', blank=True, null=True)
    image3 = models.ImageField(upload_to='images', blank=True, null=True)
    concerts = models.ManyToManyField("concert.Concert", related_name="place_concert", blank=True, null=True)
    social_networks = models.TextField(blank=True, null=True)
    place_type = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        db_table = 'place'
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.user.username
