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

    first = serializer.validated_data.pop("first")
    second = serializer.validated_data.pop("second")
    result: float

    try:
        result = operation.apply(first, second)
    except Exception as e:
        return JsonResponse(
            data={
                "error": str(e),
            },
            status=HTTP_400_BAD_REQUEST,
        )

    return JsonResponse(
        data={
            "result": result,
        },
        status=HTTP_200_OK,
    )


@api_view(["POST"])
def modulus(request):
    return process_binary_operation(request, ModulusOperation)
