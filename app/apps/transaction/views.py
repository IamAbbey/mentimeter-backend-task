from django.db.models import F
from rest_framework import generics, status
from rest_framework.response import Response

from apps.common.utils import CustomPageNumberPagination

from .models import Transaction
from .serializers import TransactionSerializer


# Create your views here.
class TransactionListCreateView(generics.ListCreateAPIView):
    """
    Create transaction endpoint
    """

    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    pagination_class = CustomPageNumberPagination
    swagger_tags = ["Transaction"]

    def perform_create(self, serializer):
        transaction = serializer.save()
        account = transaction.account_id
        account.balance = F("balance") + transaction.amount
        transaction.account_id.save()

    def create(self, request, *args, **kwargs):
        response = super().create(request)
        return Response(response.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        """
        GET verb, to return all transactions
        """
        queryset = self.get_queryset()
        serializer = TransactionSerializer(queryset, many=True)
        page = self.paginate_queryset(serializer.data)
        return Response(
            self.get_paginated_response(page).data,
            status=status.HTTP_200_OK,
        )


class TransactionDetailView(generics.RetrieveAPIView):
    """
    Retrieve endpoint
    """

    serializer_class = TransactionSerializer
    lookup_url_kwarg = "transaction_id"
    lookup_field = "transaction_id"
    queryset = Transaction.objects.all()
    swagger_tags = ["Transaction"]

    def get(self, request, *args, **kwargs):
        response = super().get(request)
        return Response(response.data, status=status.HTTP_200_OK)
