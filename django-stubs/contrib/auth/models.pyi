from typing import Any, List, Optional, Set, Tuple, Type, Union

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models.manager import EmptyManager

from .validators import UnicodeUsernameValidator


def update_last_login(
    sender: Type[AbstractBaseUser], user: AbstractBaseUser, **kwargs: Any
) -> None: ...

class PermissionManager(models.Manager):
    creation_counter: int
    model: None
    name: None
    use_in_migrations: bool = ...
    def get_by_natural_key(
        self, codename: str, app_label: str, model: str
    ) -> Permission: ...

class Permission(models.Model):
    content_type_id: int
    id: int
    name: str = ...
    content_type: Any = ...
    codename: str = ...
    objects: Any = ...
    class Meta:
        verbose_name: Any = ...
        verbose_name_plural: Any = ...
        unique_together: Any = ...
        ordering: Any = ...
    def natural_key(self) -> Tuple[str, str, str]: ...

class GroupManager(models.Manager):
    creation_counter: int
    model: None
    name: None
    use_in_migrations: bool = ...
    def get_by_natural_key(self, name: str) -> Group: ...

class Group(models.Model):
    id: None
    name: str = ...
    permissions: Any = ...
    objects: Any = ...
    class Meta:
        verbose_name: Any = ...
        verbose_name_plural: Any = ...
    def natural_key(self): ...

class UserManager(BaseUserManager):
    creation_counter: int
    model: None
    name: None
    use_in_migrations: bool = ...
    def create_user(
        self,
        username: str,
        email: Optional[str] = ...,
        password: Optional[str] = ...,
        **extra_fields: Any
    ) -> AbstractUser: ...
    def create_superuser(
        self,
        username: str,
        email: Optional[str],
        password: Optional[str],
        **extra_fields: Any
    ) -> AbstractBaseUser: ...

class PermissionsMixin(models.Model):
    is_superuser: Any = ...
    groups: Any = ...
    user_permissions: Any = ...
    class Meta:
        abstract: bool = ...
    def get_group_permissions(self, obj: None = ...) -> Set[str]: ...
    def get_all_permissions(self, obj: Optional[str] = ...) -> Set[str]: ...
    def has_perm(
        self, perm: Union[Tuple[str, Any], str], obj: Optional[str] = ...
    ) -> bool: ...
    def has_perms(
        self, perm_list: Union[List[str], Set[str], Tuple[str]], obj: None = ...
    ) -> bool: ...
    def has_module_perms(self, app_label: str) -> bool: ...

class AbstractUser(AbstractBaseUser, PermissionsMixin):
    is_superuser: bool
    last_login: None
    password: str
    username_validator: Any = ...
    username: str = ...
    first_name: str = ...
    last_name: str = ...
    email: str = ...
    is_staff: bool = ...
    is_active: bool = ...
    date_joined: datetime.datetime = ...
    objects: Any = ...
    EMAIL_FIELD: str = ...
    USERNAME_FIELD: str = ...
    REQUIRED_FIELDS: Any = ...
    class Meta:
        verbose_name: Any = ...
        verbose_name_plural: Any = ...
        abstract: bool = ...
    def clean(self) -> None: ...
    def get_full_name(self) -> str: ...
    def get_short_name(self) -> str: ...
    def email_user(
        self, subject: str, message: str, from_email: str = ..., **kwargs: Any
    ) -> None: ...

class User(AbstractUser):
    date_joined: datetime.datetime
    email: str
    first_name: str
    id: None
    is_active: bool
    is_staff: bool
    is_superuser: bool
    last_login: None
    last_name: str
    password: str
    username: str
    class Meta(AbstractUser.Meta):
        swappable: str = ...

class AnonymousUser:
    id: Any = ...
    pk: Any = ...
    username: str = ...
    is_staff: bool = ...
    is_active: bool = ...
    is_superuser: bool = ...
    def __eq__(self, other: Union[AnonymousUser, User]) -> bool: ...
    def __hash__(self) -> int: ...
    def save(self) -> Any: ...
    def delete(self) -> Any: ...
    def set_password(self, raw_password: str) -> Any: ...
    def check_password(self, raw_password: str) -> Any: ...
    @property
    def groups(self) -> EmptyManager: ...
    @property
    def user_permissions(self) -> EmptyManager: ...
    def get_group_permissions(self, obj: None = ...) -> Set[Any]: ...
    def get_all_permissions(self, obj: Any = ...) -> Set[str]: ...
    def has_perm(self, perm: str, obj: None = ...) -> bool: ...
    def has_perms(
        self, perm_list: Union[List[str], Tuple[str]], obj: None = ...
    ) -> bool: ...
    def has_module_perms(self, module: str) -> bool: ...
    @property
    def is_anonymous(self) -> bool: ...
    @property
    def is_authenticated(self) -> bool: ...
    def get_username(self) -> str: ...
