from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class PingView(APIView):
    """
    Healthcheck to make sure the service is running.
    """

    def get(self, request):
        return Response({"message": "pong"}, status=status.HTTP_200_OK)
