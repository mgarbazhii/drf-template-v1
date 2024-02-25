from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    print('Это обработчик исключений')
    return Response({'detail': str(exc)}, status=status.HTTP_400_BAD_REQUEST)
