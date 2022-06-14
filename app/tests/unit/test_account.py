import uuid

import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_get_all_account(create_account, unauthenticated_client):
    create_account()
    url = reverse("account_list_create")
    response = unauthenticated_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data["results"]) == 1


@pytest.mark.django_db
@pytest.mark.parametrize(
    "balance, status_code",
    [
        pytest.param(None, 400, marks=pytest.mark.bad_request),
        pytest.param(
            2000,
            201,
            marks=pytest.mark.success_request,
        ),
    ],
)
def test_add_account(balance, status_code, unauthenticated_client):
    url = reverse("account_list_create")
    data = {
        "balance": balance,
    }
    response = unauthenticated_client.post(url, data, format="json")
    print(response.data)
    assert response.status_code == status_code


@pytest.mark.django_db
def test_get_account_details(unauthenticated_client, create_account):
    account = create_account()
    url = reverse("account_detail", kwargs={"account_id": account.pk})
    response = unauthenticated_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert uuid.UUID(response.data["account_id"]) == account.pk
    assert response.data["balance"] == account.balance
