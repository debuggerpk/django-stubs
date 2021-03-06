from typing import Any, Dict, List, Optional, Tuple, Type

from django.contrib.sites.managers import CurrentSiteManager
from django.db.models.base import Model
from django.db.models.query import QuerySet


class BaseManager:
    creation_counter: int = ...
    auto_created: bool = ...
    use_in_migrations: bool = ...
    def __new__(cls: Type[Manager], *args: Any, **kwargs: Any) -> Manager: ...
    model: Any = ...
    name: Any = ...
    def __init__(self) -> None: ...
    def deconstruct(self) -> Tuple[bool, str, None, Tuple, Dict[str, int]]: ...
    def check(self, **kwargs: Any) -> List[Any]: ...
    @classmethod
    def from_queryset(
        cls, queryset_class: Any, class_name: Optional[Any] = ...
    ): ...
    def contribute_to_class(self, model: Type[Model], name: str) -> None: ...
    def db_manager(
        self,
        using: Optional[str] = ...,
        hints: Optional[Dict[str, Model]] = ...,
    ) -> Manager: ...
    @property
    def db(self) -> str: ...
    def get_queryset(self) -> QuerySet: ...
    def all(self) -> QuerySet: ...
    def __eq__(self, other: Optional[CurrentSiteManager]) -> bool: ...
    def __hash__(self): ...

class Manager: ...

class ManagerDescriptor:
    manager: django.db.models.manager.Manager = ...
    def __init__(self, manager: Manager) -> None: ...
    def __get__(
        self, instance: Optional[Model], cls: Type[Model] = ...
    ) -> Manager: ...

class EmptyManager(Manager):
    creation_counter: int
    name: None
    model: Optional[Type[django.db.models.base.Model]] = ...
    def __init__(self, model: Type[Model]) -> None: ...
    def get_queryset(self) -> QuerySet: ...
