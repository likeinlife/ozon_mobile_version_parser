from typing import Any


class BaseError(Exception): ...


class IncorrectRequestType(BaseError):
    def __init__(self, request: Any, *args):
        self.message = (
            f"Incorrect request type: {type(request)}. Expected SeleniumRequest."
        )
        super().__init__(self.message, *args)
