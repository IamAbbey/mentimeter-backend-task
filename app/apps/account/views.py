from rest_framework import generics, status
from rest_framework.response import Response

from apps.common.utils import CustomPageNumberPagination

from .models import Account
from .serializers import AccountSerializer


# Create your views here.
class AccountListCreateView(generics.ListCreateAPIView):
    """
    Create account endpoint
    """

    serializer_class = AccountSerializer
    queryset = Account.objects.all()
    pagination_class = CustomPageNumberPagination
    swagger_tags = ["Account"]

    def create(self, request, *args, **kwargs):
        response = super().create(request)
        return Response(response.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        """
        GET verb, to return all accounts
        """
        queryset = self.get_queryset()
        serializer = AccountSerializer(queryset, many=True)
        page = self.paginate_queryset(serializer.data)
        return Response(
            self.get_paginated_response(page).data,
            status=status.HTTP_200_OK,
        )


class AccountDetailView(generics.RetrieveAPIView):
    """
    Retrieve endpoint
    """

    serializer_class = AccountSerializer
    lookup_url_kwarg = "account_id"
    lookup_field = "account_id"
    queryset = Account.objects.all()
    swagger_tags = ["Account"]

    def get(self, request, *args, **kwargs):
        response = super().get(request)
        return Response(response.data, status=status.HTTP_200_OK)
