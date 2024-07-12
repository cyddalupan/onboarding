from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging

# Set up logging
logger = logging.getLogger(__name__)

class ActionsGPTWebhook(APIView):
    def post(self, request, format=None):
        # Log the received request data
        logger.info(f"Received data: {request.data}")

        # Assume the incoming JSON has a key "user_input"
        user_input = request.data.get("user_input", "Hello")

        # Process the input or perform actions here
        response_message = f"Echo: {user_input}"

        # Construct the response for ActionsGPT
        response_data = {"responses": [{"message": response_message}]}

        # Log the response data
        logger.info(f"Response data: {response_data}")

        return Response(response_data, status=status.HTTP_200_OK)

