from exception import ResponseException


class Functions:


    @classmethod
    def validate_params(cls, data):
        for k, v in data.items():
            if not getattr(data, k):
                raise ResponseException('', 400, 'No valid parameters sent')
