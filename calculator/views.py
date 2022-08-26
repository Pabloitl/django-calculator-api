from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from calculator.serializers import BinaryFloatSerializer
from calculator.utils import ModulusOperation, Operation


def process_binary_operation(request, operation: Operation):
    serializer = BinaryFloatSerializer(data=request.data)

    if not serializer.is_valid():
        return HttpResponse(status=HTTP_400_BAD_REQUEST)

    return JsonResponse(
        data={
            "result": operation.apply(
                serializer.validated_data.pop("first"),
                serializer.validated_data.pop("second"),
            ),
        },
        status=HTTP_200_OK,
    )


@api_view(["POST"])
def modulus(request):
    return process_binary_operation(request, ModulusOperation)
