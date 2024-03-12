from enum import Enum


class MobileType(Enum):
    IOS = "iOS"
    ANDROID = "Android"

    def __str__(self) -> str:
        return str(self.value)
