from typing import Any, Callable, Dict, Optional, Union

from django.core.cache.backends.base import BaseCache


class FileBasedCache(BaseCache):
    default_timeout: int
    key_func: Callable
    key_prefix: str
    version: int
    cache_suffix: str = ...
    def __init__(
        self,
        dir: str,
        params: Dict[str, Union[Callable, Dict[str, int], int, str]],
    ) -> None: ...
    def add(
        self,
        key: str,
        value: Union[Dict[str, int], bytes, int, str],
        timeout: Any = ...,
        version: Optional[int] = ...,
    ) -> bool: ...
    def get(
        self,
        key: str,
        default: Optional[Union[int, str]] = ...,
        version: Optional[int] = ...,
    ) -> Optional[str]: ...
    def set(
        self,
        key: str,
        value: Any,
        timeout: Any = ...,
        version: Optional[int] = ...,
    ) -> None: ...
    def touch(
        self, key: str, timeout: Any = ..., version: None = ...
    ) -> bool: ...
    def delete(self, key: str, version: Optional[int] = ...) -> None: ...
    def has_key(self, key: str, version: Optional[int] = ...) -> bool: ...
    def clear(self) -> None: ...
