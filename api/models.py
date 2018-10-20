from django.db import models
from enum import Enum


class User(models.Model):
    male_number = models.IntegerField()
    female_number = models.IntegerField()
    children_number = models.IntegerField()
    baby_number = models.IntegerField()
    old_number = models.IntegerField()
    disease = models.TextField()


class Item(models.Model):

    class ItemStatus(Enum):
        want = "0"
        want_and_have = "1"
        recommend = "2"

    name = models.TextField()
    status = models.CharField(max_length=2, choices=[(i.value, i.name) for i in ItemStatus])
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="item")
