from typing import Any, Dict, Optional, Union

from django.core.management import BaseCommand
from django.core.management.base import CommandParser


class Command(BaseCommand):
    stderr: django.core.management.base.OutputWrapper
    stdout: django.core.management.base.OutputWrapper
    style: django.core.management.color.Style
    help: str = ...
    requires_system_checks: bool = ...
    shells: Any = ...
    def add_arguments(self, parser: CommandParser) -> None: ...
    def ipython(self, options: Dict[str, Optional[Union[int, str]]]) -> Any: ...
    def bpython(self, options: Dict[str, Optional[Union[int, str]]]) -> Any: ...
    def python(self, options: Any) -> None: ...
    def handle(self, **options: Any) -> None: ...
