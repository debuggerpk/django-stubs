from typing import Any


def autodiscover_modules(*args, **kwargs) -> None: ...


def import_string(dotted_path: str) -> object: ...


def module_dir(module: Any) -> str: ...


def module_has_submodule(package: Any, module_name: str) -> bool: ...