from typing import (
    Dict,
    Union,
)
from uuid import UUID


def get_converter(raw_converter: str) -> object: ...


def get_converters() -> Dict[str, object]: ...


class IntConverter:
    def to_python(self, value: str) -> int: ...
    def to_url(self, value: Union[str, int]) -> str: ...


class StringConverter:
    def to_python(self, value: str) -> str: ...
    def to_url(self, value: Union[str, UUID, int]) -> Union[str, UUID, int]: ...