from uuid import uuid4

from django.db import models


# Create your models here.
class Account(models.Model):

    account_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    balance = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"

    def __str__(self):
        return self.account_id
