import pytest
from rest_framework.test import APIClient

from apps.account.models import Account
from apps.transaction.models import Transaction


@pytest.fixture(scope="function")
def unauthenticated_client():
    return APIClient()


@pytest.fixture(scope="function")
def create_account(db):
    def create(*args, **kwargs):

        return Account.objects.create(balance=kwargs.get("balance", 1000))

    return create


@pytest.fixture(scope="function")
def create_transaction(db, create_account):
    def create(*args, **kwargs):
        return Transaction.objects.create(
            account_id=create_account(), amount=kwargs.get("amount", 10)
        )

    return create
