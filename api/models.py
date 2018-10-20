from django.db import models
from enum import Enum

class Item(models.Model):

    class ItemStatus(Enum):
        want = 0
        want_and_have = 1
        recommend = 2

    name = models.TextField()
    status = models.IntegerField(choices=[i.value for i in ItemStatus])
