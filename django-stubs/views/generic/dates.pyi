from datetime import date
from typing import Any, Dict, Optional, Tuple, Union

from django.core.handlers.wsgi import WSGIRequest
from django.db.models.base import Model
from django.db.models.query import QuerySet
from django.template.response import TemplateResponse
from django.views.generic.base import View
from django.views.generic.detail import (BaseDetailView,
                                         SingleObjectTemplateResponseMixin)
from django.views.generic.list import (MultipleObjectMixin,
                                       MultipleObjectTemplateResponseMixin)


class YearMixin:
    year_format: str = ...
    year: Any = ...
    def get_year_format(self) -> str: ...
    def get_year(self) -> int: ...
    def get_next_year(self, date: date) -> Optional[date]: ...
    def get_previous_year(self, date: date) -> Optional[date]: ...

class MonthMixin:
    month_format: str = ...
    month: Any = ...
    def get_month_format(self) -> str: ...
    def get_month(self) -> Union[int, str]: ...
    def get_next_month(self, date: date) -> Optional[date]: ...
    def get_previous_month(self, date: date) -> Optional[date]: ...

class DayMixin:
    day_format: str = ...
    day: Any = ...
    def get_day_format(self) -> str: ...
    def get_day(self) -> Union[int, str]: ...
    def get_next_day(self, date: date) -> Optional[date]: ...
    def get_previous_day(self, date: date) -> Optional[date]: ...

class WeekMixin:
    week_format: str = ...
    week: Any = ...
    def get_week_format(self) -> str: ...
    def get_week(self) -> int: ...
    def get_next_week(self, date: date) -> Optional[date]: ...
    def get_previous_week(self, date: date) -> Optional[date]: ...

class DateMixin:
    date_field: Any = ...
    allow_future: bool = ...
    def get_date_field(self) -> str: ...
    def get_allow_future(self) -> bool: ...
    def uses_datetime_field(self) -> bool: ...

class BaseDateListView(MultipleObjectMixin, DateMixin, View):
    allow_empty: bool = ...
    date_list_period: str = ...
    def get(
        self, request: WSGIRequest, *args: Any, **kwargs: Any
    ) -> TemplateResponse: ...
    def get_dated_items(self) -> None: ...
    def get_ordering(self) -> Union[Tuple[str, str], str]: ...
    def get_dated_queryset(self, **lookup: Any) -> QuerySet: ...
    def get_date_list_period(self) -> str: ...
    def get_date_list(
        self, queryset: QuerySet, date_type: None = ..., ordering: str = ...
    ) -> QuerySet: ...

class BaseArchiveIndexView(BaseDateListView):
    context_object_name: str = ...
    def get_dated_items(self) -> Tuple[QuerySet, QuerySet, Dict[Any, Any]]: ...

class ArchiveIndexView(
    MultipleObjectTemplateResponseMixin, BaseArchiveIndexView
):
    template_name_suffix: str = ...

class BaseYearArchiveView(YearMixin, BaseDateListView):
    date_list_period: str = ...
    make_object_list: bool = ...
    def get_dated_items(
        self
    ) -> Tuple[QuerySet, QuerySet, Dict[str, Optional[date]]]: ...
    def get_make_object_list(self) -> bool: ...

class YearArchiveView(MultipleObjectTemplateResponseMixin, BaseYearArchiveView):
    template_name_suffix: str = ...

class BaseMonthArchiveView(YearMixin, MonthMixin, BaseDateListView):
    date_list_period: str = ...
    def get_dated_items(
        self
    ) -> Tuple[QuerySet, QuerySet, Dict[str, Optional[date]]]: ...

class MonthArchiveView(
    MultipleObjectTemplateResponseMixin, BaseMonthArchiveView
):
    template_name_suffix: str = ...

class BaseWeekArchiveView(YearMixin, WeekMixin, BaseDateListView):
    def get_dated_items(
        self
    ) -> Tuple[None, QuerySet, Dict[str, Optional[date]]]: ...

class WeekArchiveView(MultipleObjectTemplateResponseMixin, BaseWeekArchiveView):
    template_name_suffix: str = ...

class BaseDayArchiveView(YearMixin, MonthMixin, DayMixin, BaseDateListView):
    def get_dated_items(
        self
    ) -> Tuple[None, QuerySet, Dict[str, Optional[date]]]: ...

class DayArchiveView(MultipleObjectTemplateResponseMixin, BaseDayArchiveView):
    template_name_suffix: str = ...

class BaseTodayArchiveView(BaseDayArchiveView):
    def get_dated_items(
        self
    ) -> Tuple[None, QuerySet, Dict[str, Optional[date]]]: ...

class TodayArchiveView(
    MultipleObjectTemplateResponseMixin, BaseTodayArchiveView
):
    template_name_suffix: str = ...

class BaseDateDetailView(
    YearMixin, MonthMixin, DayMixin, DateMixin, BaseDetailView
):
    def get_object(self, queryset: Optional[QuerySet] = ...) -> Model: ...

class DateDetailView(SingleObjectTemplateResponseMixin, BaseDateDetailView):
    template_name_suffix: str = ...

def timezone_today() -> date: ...
