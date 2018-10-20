from django.db import models
from enum import Enum

class Item(models.Model):

    class ItemStatus(Enum):
        want = "0"
        want_and_have = "1"
        recommend = "2"

    name = models.TextField()
    status = models.CharField(max_length=2, choices=[(i.name, i.value) for i in ItemStatus])
