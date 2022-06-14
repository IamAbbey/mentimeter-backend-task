from django.urls import reverse
from rest_framework import status


def test_ping(unauthenticated_client):
    url = reverse("ping")
    response = unauthenticated_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data["message"] == "pong"
