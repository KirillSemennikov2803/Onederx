from jsonschema import validate, ValidationError

from rest_framework.response import Response


def validate_response(body, schema):
    try:
        validate(instance=body, schema=schema)
    except ValidationError:
        return reject_response()
    return get_success_response(body)


def reject_response():
    return get_error_response(400)


def server_error_response():
    return get_error_response(500)


def get_success_response(body):
    return Response(body, status=200, content_type="application/json")


def get_error_response(status_code):
    return Response(status=status_code, content_type="application/json")
