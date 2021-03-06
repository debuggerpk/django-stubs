from typing import Any, Optional

from django.core.management.base import CommandParser, LabelCommand


class Command(LabelCommand):
    stderr: django.core.management.base.OutputWrapper
    stdout: django.core.management.base.OutputWrapper
    style: django.core.management.color.Style
    help: str = ...
    label: str = ...
    def add_arguments(self, parser: CommandParser) -> None: ...
    def handle_label(self, path: str, **options: Any) -> str: ...
