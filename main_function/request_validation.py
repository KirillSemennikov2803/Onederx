from jsonschema import validate, ValidationError

from main_function.response_processing import reject_response


def validate_request(schema):
    def request_dec(func):
        def request_handler(self, request):
            try:
                validate(instance=request.data, schema=schema)
                return func(self, request)
            except ValidationError:
                return reject_response()

        return request_handler

    return request_dec
