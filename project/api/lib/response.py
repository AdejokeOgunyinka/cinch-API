from rest_framework.response import Response as DRFResponse


class InvalidResponse(Exception):
    pass

class Response:
    def __new__(cls, data=None, errors=None, *args, **kwargs):
        payload = cls.format(data, errors)
        return DRFResponse(payload, *args, **kwargs)

    @classmethod
    def format(cls, data=None, errors=None):
        data = data if type(data) == dict and len(data) else None
        errors = errors if type(errors) == dict and len(errors) else None

        message = 'success' if data and not errors else 'failure'

        if errors and '_others' not in errors:
            errors['_others'] = []

        if not data and not errors: raise InvalidResponse()

        return dict(
            message=message,
            data=data,
            errors=errors,
        )
