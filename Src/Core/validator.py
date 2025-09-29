class argument_exception(Exception):
    def __init__(self, message: str):
        super().__init__(message)

class operation_exception(Exception):
    def __init__(self, message: str):
        super().__init__(message)

class error_proxy:
    def __init__(self, exception: Exception):
        self.exception = exception

    def __str__(self):
        return str(self.exception)

class validator:
    @staticmethod
    def validate(value, expected_type, max_length: int = None):
        if not isinstance(value, expected_type):
            raise argument_exception(f"Ожидался тип {expected_type.__name__}, получен {type(value).__name__}")
        if max_length is not None:
            if expected_type == str and len(value) > max_length:
                raise argument_exception(f"Длина строки превышает {max_length} символов")
            if expected_type == int and len(str(value)) != max_length:
                raise argument_exception(f"Число должно содержать ровно {max_length} цифр")