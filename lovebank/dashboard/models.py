from django.db import models
from django.contrib.auth.admin import User


class Person(models.Model):
    ref = models.CharField(default="ffffffff", max_length=8)
    info = models.TextField(max_length=500)
    def __str__(self):
        return self.ref


class FriendsList(models.Model):
    person = models.ForeignKey(Person)
    def __str__(self):
        return self.id


class Account(models.Model):
    person = models.OneToOneField(Person)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    friendlist = models.OneToOneField(FriendsList)
    def __str__(self):
        return self.owner