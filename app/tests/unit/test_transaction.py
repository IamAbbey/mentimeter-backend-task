import uuid

import pytest
from django.urls import reverse
from rest_framework import status

from apps.account.models import Account


@pytest.mark.django_db
def test_get_all_transaction(create_transaction, unauthenticated_client):
    create_transaction()
    url = reverse("transaction_list_create")
    response = unauthenticated_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data["results"]) == 1


@pytest.mark.django_db
@pytest.mark.parametrize(
    "amount, valid_account_id, status_code",
    [
        pytest.param(None, None, 400, marks=pytest.mark.bad_request),
        pytest.param(10, False, 400, marks=pytest.mark.bad_request),
        pytest.param(
            2000,
            True,
            201,
            marks=pytest.mark.success_request,
        ),
    ],
)
def test_add_transaction(
    amount, valid_account_id, status_code, create_account, unauthenticated_client
):
    data = {"amount": amount}

    if valid_account_id:
        prev_account = create_account()
        data["account_id"] = prev_account.account_id

    url = reverse("transaction_list_create")
    response = unauthenticated_client.post(url, data, format="json")
    assert response.status_code == status_code
    if valid_account_id:
        account = Account.objects.get(pk=prev_account.account_id)
        assert account.balance == prev_account.balance + amount


@pytest.mark.django_db
def test_get_transaction_details(unauthenticated_client, create_transaction):
    transaction = create_transaction()
    url = reverse("transaction_detail", kwargs={"transaction_id": transaction.pk})
    response = unauthenticated_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert uuid.UUID(response.data["transaction_id"]) == transaction.pk
    assert response.data["amount"] == transaction.amount
