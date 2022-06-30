from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='user/', default='profil.png')

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class Category(models.Model):
    created_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Word(models.Model):
    created_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    english = models.CharField(max_length=255)
    uzbek = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class KnowWord(models.Model):
    created_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    english = models.CharField(max_length=255)
    uzbek = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)


class General(models.Model):
    english = models.CharField(max_length=50)
    status = models.IntegerField(default=0, blank=True)


class Test(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    savollar_id = models.PositiveIntegerField(default=1)
    boshlanish_vaqt = models.DateTimeField(auto_now_add=True)
    tugash_vaqt = models.DateTimeField(default=0)
    umumiy_soni = models.PositiveIntegerField(default=10)
    topgan_soni = models.PositiveIntegerField(default=0)


class TestEnglish(models.Model):
    tartib = models.PositiveBigIntegerField(default=1)
    english = models.CharField(max_length=70)
    uzbek = models.CharField(max_length=70)
    topilgan = models.BooleanField(default=False)

    def __str__(self):
        return str(self.tartib)
