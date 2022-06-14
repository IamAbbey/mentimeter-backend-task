from rest_framework import serializers

from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"

        read_only_fields = (
            "transaction_id",
            "created_at",
        )

        extra_kwargs = {
            "account_id": {
                "error_messages": {
                    "required": "Account must be supplied.",
                    "does_not_exist": "Account not found.",
                    "null": "Account must be supplied.",
                }
            },
        }
