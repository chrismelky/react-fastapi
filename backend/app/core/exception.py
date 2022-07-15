from typing import Any, List


class CustomBadRequestException(Exception):
    def __init__(self, message: str, errors: List[Any]  = []):
        self.message = message
        self.errors = errors
        self.status_code = 400