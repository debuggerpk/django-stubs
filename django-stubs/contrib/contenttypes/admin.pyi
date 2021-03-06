from django.db.models.base import Model
from typing import Any, List, Type

class GenericInlineModelAdminChecks:
    def _check_exclude_of_parent_model(
        self, obj: GenericTabularInline, parent_model: Type[Model]
    ) -> List[Any]: ...
    def _check_relation(
        self, obj: GenericTabularInline, parent_model: Type[Model]
    ) -> List[Any]: ...
