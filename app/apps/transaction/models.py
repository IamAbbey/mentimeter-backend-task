from uuid import uuid4

from django.db import models

from apps.account.models import Account


# Create your models here.
class Transaction(models.Model):

    transaction_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"

    def __str__(self):
        return self.transaction_id
