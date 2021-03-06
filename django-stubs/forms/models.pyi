from collections import OrderedDict
from datetime import date, datetime
from decimal import Decimal
from typing import (Any, Callable, Dict, Iterator, List, Optional, Tuple, Type,
                    Union)
from unittest.mock import MagicMock
from uuid import UUID

from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.flatpages.forms import FlatpageForm
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db.models.base import Model
from django.db.models.manager import Manager
from django.db.models.query import QuerySet
from django.db.models.query_utils import Q
from django.forms.fields import CharField, ChoiceField, Field
from django.forms.forms import BaseForm, DeclarativeFieldsMetaclass
from django.forms.formsets import BaseFormSet
from django.forms.utils import ErrorList
from django.forms.widgets import Input, Widget
from django.http.request import QueryDict
from django.utils.datastructures import MultiValueDict

ALL_FIELDS: str

def model_to_dict(
    instance: Model,
    fields: Optional[Union[List[Union[Callable, str]], Tuple[str]]] = ...,
    exclude: Optional[Union[List[Union[Callable, str]], Tuple[str]]] = ...,
) -> Dict[str, Optional[Union[bool, date, float]]]: ...
def fields_for_model(
    model: Type[Model],
    fields: Optional[Union[List[Union[Callable, str]], Tuple]] = ...,
    exclude: Optional[Union[List[Union[Callable, str]], Tuple]] = ...,
    widgets: Optional[Union[Dict[str, Type[Input]], Dict[str, Widget]]] = ...,
    formfield_callback: Optional[Union[Callable, str]] = ...,
    localized_fields: Optional[Union[Tuple[str], str]] = ...,
    labels: Optional[Dict[str, str]] = ...,
    help_texts: Optional[Dict[str, str]] = ...,
    error_messages: Optional[Dict[str, Dict[str, str]]] = ...,
    field_classes: Optional[Dict[str, Type[CharField]]] = ...,
    *,
    apply_limit_choices_to: bool = ...
) -> OrderedDict: ...

class ModelFormOptions:
    model: Optional[Type[django.db.models.base.Model]] = ...
    fields: Optional[Union[List[Union[Callable, str]], Tuple, str]] = ...
    exclude: Optional[Union[List[Union[Callable, str]], Tuple, str]] = ...
    widgets: Optional[
        Union[
            Dict[str, Type[django.forms.widgets.Input]],
            Dict[str, django.forms.widgets.Widget],
        ]
    ] = ...
    localized_fields: Optional[Union[Tuple[str], str]] = ...
    labels: Optional[Dict[str, str]] = ...
    help_texts: Optional[Dict[str, str]] = ...
    error_messages: Optional[Dict[str, Dict[str, str]]] = ...
    field_classes: Optional[
        Dict[str, Type[django.forms.fields.CharField]]
    ] = ...
    def __init__(
        self,
        options: Optional[
            Type[
                Union[
                    UserChangeForm.Meta,
                    UserCreationForm.Meta,
                    FlatpageForm.Meta,
                ]
            ]
        ] = ...,
    ) -> None: ...

class ModelFormMetaclass(DeclarativeFieldsMetaclass):
    def __new__(
        mcs: Type[ModelFormMetaclass],
        name: str,
        bases: Tuple[Type[ModelForm]],
        attrs: OrderedDict,
    ) -> Type[ModelForm]: ...

class BaseModelForm(BaseForm):
    instance: Any = ...
    def __init__(
        self,
        data: Optional[
            Union[
                Dict[str, Optional[Union[List[int], datetime, int, str]]],
                Dict[str, Union[List[str], str]],
                Dict[str, Union[datetime, Decimal, int, str]],
                QueryDict,
            ]
        ] = ...,
        files: Optional[
            Union[Dict[str, SimpleUploadedFile], MultiValueDict]
        ] = ...,
        auto_id: Union[bool, str] = ...,
        prefix: None = ...,
        initial: Optional[Union[Dict[str, List[int]], Dict[str, int]]] = ...,
        error_class: Type[ErrorList] = ...,
        label_suffix: None = ...,
        empty_permitted: bool = ...,
        instance: Optional[Model] = ...,
        use_required_attribute: None = ...,
        renderer: Any = ...,
    ) -> None: ...
    def clean(self) -> Dict[str, Any]: ...
    def validate_unique(self) -> None: ...
    save_m2m: Any = ...
    def save(self, commit: bool = ...) -> Model: ...

class ModelForm(BaseModelForm): ...

def modelform_factory(
    model: Type[Model],
    form: Type[ModelForm] = ...,
    fields: Optional[Union[List[str], str]] = ...,
    exclude: None = ...,
    formfield_callback: Optional[str] = ...,
    widgets: None = ...,
    localized_fields: None = ...,
    labels: None = ...,
    help_texts: None = ...,
    error_messages: None = ...,
    field_classes: None = ...,
) -> Any: ...

class BaseModelFormSet(BaseFormSet):
    model: Any = ...
    unique_fields: Any = ...
    queryset: Any = ...
    initial_extra: Any = ...
    def __init__(
        self,
        data: Optional[Any] = ...,
        files: Optional[Any] = ...,
        auto_id: str = ...,
        prefix: Optional[Any] = ...,
        queryset: Optional[Any] = ...,
        *,
        initial: Optional[Any] = ...,
        **kwargs: Any
    ) -> None: ...
    def initial_form_count(self): ...
    def get_queryset(self): ...
    def save_new(self, form: Any, commit: bool = ...): ...
    def save_existing(self, form: Any, instance: Any, commit: bool = ...): ...
    def delete_existing(self, obj: Any, commit: bool = ...) -> None: ...
    saved_forms: Any = ...
    save_m2m: Any = ...
    def save(self, commit: bool = ...): ...
    def clean(self) -> None: ...
    def validate_unique(self) -> None: ...
    def get_unique_error_message(self, unique_check: Any): ...
    def get_date_error_message(self, date_check: Any): ...
    def get_form_error(self): ...
    changed_objects: Any = ...
    deleted_objects: Any = ...
    def save_existing_objects(self, commit: bool = ...): ...
    new_objects: Any = ...
    def save_new_objects(self, commit: bool = ...): ...
    def add_fields(self, form: Any, index: Any): ...

def modelformset_factory(
    model: Type[Model],
    form: Type[ModelForm] = ...,
    formfield_callback: None = ...,
    formset: Type[BaseModelFormSet] = ...,
    extra: int = ...,
    can_delete: bool = ...,
    can_order: bool = ...,
    max_num: None = ...,
    fields: None = ...,
    exclude: None = ...,
    widgets: None = ...,
    validate_max: bool = ...,
    localized_fields: None = ...,
    labels: None = ...,
    help_texts: None = ...,
    error_messages: None = ...,
    min_num: None = ...,
    validate_min: bool = ...,
    field_classes: None = ...,
) -> Any: ...

class BaseInlineFormSet(BaseModelFormSet):
    instance: Any = ...
    save_as_new: Any = ...
    unique_fields: Any = ...
    def __init__(
        self,
        data: Optional[Any] = ...,
        files: Optional[Any] = ...,
        instance: Optional[Any] = ...,
        save_as_new: bool = ...,
        prefix: Optional[Any] = ...,
        queryset: Optional[Any] = ...,
        **kwargs: Any
    ) -> None: ...
    def initial_form_count(self): ...
    @classmethod
    def get_default_prefix(cls): ...
    def save_new(self, form: Any, commit: bool = ...): ...
    def add_fields(self, form: Any, index: Any) -> None: ...
    def get_unique_error_message(self, unique_check: Any): ...

def inlineformset_factory(
    parent_model: Type[Model],
    model: Type[Model],
    form: Type[ModelForm] = ...,
    formset: Type[BaseInlineFormSet] = ...,
    fk_name: Optional[str] = ...,
    fields: Optional[str] = ...,
    exclude: None = ...,
    extra: int = ...,
    can_order: bool = ...,
    can_delete: bool = ...,
    max_num: None = ...,
    formfield_callback: None = ...,
    widgets: None = ...,
    validate_max: bool = ...,
    localized_fields: None = ...,
    labels: None = ...,
    help_texts: None = ...,
    error_messages: None = ...,
    min_num: None = ...,
    validate_min: bool = ...,
    field_classes: None = ...,
) -> Any: ...

class InlineForeignKeyField(Field):
    disabled: bool
    help_text: str
    initial: Optional[Union[django.db.models.base.Model, int, str]]
    label: Optional[str]
    label_suffix: None
    localize: bool
    required: bool
    show_hidden_initial: bool
    widget: Any = ...
    default_error_messages: Any = ...
    parent_instance: django.db.models.base.Model = ...
    pk_field: bool = ...
    to_field: Optional[str] = ...
    def __init__(
        self,
        parent_instance: Model,
        *args: Any,
        pk_field: bool = ...,
        to_field: Optional[Any] = ...,
        **kwargs: Any
    ) -> None: ...
    def clean(self, value: Optional[Union[int, str]]) -> Optional[Model]: ...
    def has_changed(
        self,
        initial: Optional[Union[int, str]],
        data: Optional[Union[int, str]],
    ) -> bool: ...

class ModelChoiceIterator:
    field: django.forms.models.ModelChoiceField = ...
    queryset: Optional[django.db.models.query.QuerySet] = ...
    def __init__(self, field: ModelChoiceField) -> None: ...
    def __iter__(self) -> Iterator[Tuple[Union[int, str], str]]: ...
    def __len__(self) -> int: ...
    def __bool__(self) -> bool: ...
    def choice(self, obj: Model) -> Tuple[int, str]: ...

class ModelChoiceField(ChoiceField):
    disabled: bool
    error_messages: Dict[str, str]
    help_text: str
    initial: Optional[Union[Callable, int, str, uuid.UUID]]
    label: Optional[str]
    label_suffix: None
    localize: bool
    required: bool
    show_hidden_initial: bool
    validators: List[Any]
    widget: django.forms.widgets.Select
    default_error_messages: Any = ...
    iterator: Any = ...
    empty_label: Optional[str] = ...
    queryset: Any = ...
    limit_choices_to: None = ...
    to_field_name: None = ...
    def __init__(
        self,
        queryset: Optional[Union[Manager, QuerySet]],
        *,
        empty_label: str = ...,
        required: bool = ...,
        widget: Optional[Any] = ...,
        label: Optional[Any] = ...,
        initial: Optional[Any] = ...,
        help_text: str = ...,
        to_field_name: Optional[Any] = ...,
        limit_choices_to: Optional[Any] = ...,
        **kwargs: Any
    ) -> None: ...
    def get_limit_choices_to(
        self
    ) -> Optional[Union[Dict[str, datetime], Q, MagicMock]]: ...
    def __deepcopy__(
        self,
        memo: Dict[
            int, Union[List[Union[Field, Widget]], OrderedDict, Field, Widget]
        ],
    ) -> ModelChoiceField: ...
    def label_from_instance(self, obj: Model) -> str: ...
    choices: Any = ...
    def prepare_value(self, value: Any) -> Any: ...
    def to_python(
        self,
        value: Optional[Union[List[Dict[str, str]], List[List[str]], int, str]],
    ) -> Optional[Model]: ...
    def validate(self, value: Optional[Model]) -> None: ...
    def has_changed(
        self,
        initial: Optional[Union[Model, int, str, UUID]],
        data: Optional[Union[int, str]],
    ) -> bool: ...

class ModelMultipleChoiceField(ModelChoiceField):
    disabled: bool
    empty_label: None
    help_text: str
    initial: Optional[Union[Callable, List[int]]]
    label: Optional[str]
    label_suffix: None
    localize: bool
    required: bool
    show_hidden_initial: bool
    widget: Any = ...
    hidden_widget: Any = ...
    default_error_messages: Any = ...
    def __init__(self, queryset: QuerySet, **kwargs: Any) -> None: ...
    def to_python(
        self, value: Union[List[str], Tuple[int, ...]]
    ) -> List[Model]: ...
    def clean(
        self,
        value: Optional[
            Union[
                List[Dict[str, str]], List[List[str]], List[Model], Tuple, str
            ]
        ],
    ) -> QuerySet: ...
    def prepare_value(
        self, value: Any
    ) -> Optional[Union[List[Dict[str, str]], List[List[str]], int, str]]: ...
    def has_changed(
        self,
        initial: Optional[Union[List[Model], QuerySet, str]],
        data: Optional[Union[List[int], List[str], str]],
    ) -> bool: ...
