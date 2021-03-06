from collections import OrderedDict
from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple, Type, Union, Iterable

from django.db.backends.sqlite3.base import DatabaseWrapper
from django.db.models import expressions, lookups
from django.db.models.expressions import (Col, Combinable, Expression, Func,
                                          Ref)
from django.db.models.fields import TextField, related_lookups
from django.db.models.query_utils import RegisterLookupMixin
from django.db.models.sql.compiler import SQLCompiler
from django.db.models.sql.query import Query
from django.utils.datastructures import OrderedSet
from django.utils.safestring import SafeText


class Lookup:
    lookup_name: Any = ...
    prepare_rhs: bool = ...
    can_use_none_as_rhs: bool = ...
    rhs: Any = ...
    bilateral_transforms: Any = ...
    def __init__(
        self,
        lhs: Union[Expression, TextField, related_lookups.MultiColSource],
        rhs: Any,
    ) -> None: ...
    def apply_bilateral_transforms(self, value: Expression) -> Transform: ...
    def batch_process_rhs(
        self,
        compiler: SQLCompiler,
        connection: DatabaseWrapper,
        rhs: Optional[OrderedSet] = ...,
    ) -> Tuple[List[str], List[str]]: ...
    def get_source_expressions(self) -> List[Expression]: ...
    lhs: Any = ...
    def set_source_expressions(self, new_exprs: List[Ref]) -> None: ...
    def get_prep_lookup(self) -> Any: ...
    def get_db_prep_lookup(
        self, value: Union[int, str], connection: DatabaseWrapper
    ) -> Tuple[str, List[SafeText]]: ...
    def process_lhs(
        self,
        compiler: SQLCompiler,
        connection: DatabaseWrapper,
        lhs: Optional[Col] = ...,
    ) -> Tuple[str, List[Union[int, str]]]: ...
    def process_rhs(
        self, compiler: SQLCompiler, connection: DatabaseWrapper
    ) -> Tuple[str, Union[List[Union[int, str]], Tuple[int, int]]]: ...
    def rhs_is_direct_value(self) -> bool: ...
    def relabeled_clone(
        self, relabels: Union[Dict[Optional[str], str], OrderedDict]
    ) -> Union[BuiltinLookup, FieldGetDbPrepValueMixin]: ...
    def get_group_by_cols(self) -> List[Expression]: ...
    def as_sql(self, compiler: Any, connection: Any) -> None: ...
    def contains_aggregate(self) -> bool: ...
    def contains_over_clause(self) -> bool: ...
    @property
    def is_summary(self): ...

class Transform(RegisterLookupMixin, Func):
    bilateral: bool = ...
    arity: int = ...
    @property
    def lhs(self) -> Expression: ...
    def get_bilateral_transforms(self) -> List[Type[Transform]]: ...

class BuiltinLookup(Lookup):
    def process_lhs(
        self,
        compiler: SQLCompiler,
        connection: DatabaseWrapper,
        lhs: Optional[Col] = ...,
    ) -> Tuple[str, List[Union[int, str]]]: ...
    def as_sql(
        self, compiler: SQLCompiler, connection: DatabaseWrapper
    ) -> Tuple[str, List[float]]: ...
    def get_rhs_op(self, connection: DatabaseWrapper, rhs: str) -> str: ...

class FieldGetDbPrepValueMixin:
    get_db_prep_lookup_value_is_iterable: bool = ...
    def get_db_prep_lookup(
        self, value: Any, connection: DatabaseWrapper
    ) -> Tuple[str, List[float]]: ...

class FieldGetDbPrepValueIterableMixin(FieldGetDbPrepValueMixin):
    get_db_prep_lookup_value_is_iterable: bool = ...
    def get_prep_lookup(
        self
    ) -> Iterable[Any]: ...
    def process_rhs(
        self, compiler: SQLCompiler, connection: DatabaseWrapper
    ) -> Tuple[Union[Tuple[str, str], str], Tuple]: ...
    def resolve_expression_parameter(
        self,
        compiler: SQLCompiler,
        connection: DatabaseWrapper,
        sql: str,
        param: Optional[Union[Combinable, int, str]],
    ) -> Tuple[str, List[None]]: ...
    def batch_process_rhs(
        self,
        compiler: SQLCompiler,
        connection: DatabaseWrapper,
        rhs: Optional[OrderedSet] = ...,
    ) -> Tuple[Tuple[str], Tuple]: ...

class Exact(FieldGetDbPrepValueMixin, BuiltinLookup):
    bilateral_transforms: List[Type[lookups.Transform]]
    contains_aggregate: bool
    contains_over_clause: bool
    lhs: Expression
    rhs: Any
    lookup_name: str = ...
    def process_rhs(
        self, compiler: SQLCompiler, connection: DatabaseWrapper
    ) -> Tuple[str, Union[List[str], Tuple[int, int]]]: ...

class IExact(BuiltinLookup):
    bilateral_transforms: List[Any]
    contains_aggregate: bool
    lhs: expressions.Col
    rhs: Optional[Union[expressions.Col, str]]
    lookup_name: str = ...
    prepare_rhs: bool = ...
    def process_rhs(
        self, qn: SQLCompiler, connection: DatabaseWrapper
    ) -> Tuple[str, List[str]]: ...

class GreaterThan(FieldGetDbPrepValueMixin, BuiltinLookup):
    bilateral_transforms: List[Any]
    contains_aggregate: bool
    lhs: Expression
    rhs: Any
    lookup_name: str = ...

class GreaterThanOrEqual(FieldGetDbPrepValueMixin, BuiltinLookup):
    bilateral_transforms: List[Any]
    contains_aggregate: bool
    lhs: Expression
    rhs: Any
    lookup_name: str = ...

class LessThan(FieldGetDbPrepValueMixin, BuiltinLookup):
    bilateral_transforms: List[Any]
    contains_aggregate: bool
    lhs: Expression
    rhs: Any
    lookup_name: str = ...

class LessThanOrEqual(FieldGetDbPrepValueMixin, BuiltinLookup):
    bilateral_transforms: List[Type[lookups.Transform]]
    contains_aggregate: bool
    contains_over_clause: bool
    lhs: Expression
    rhs: Any
    lookup_name: str = ...

class IntegerFieldFloatRounding:
    rhs: Any = ...
    def get_prep_lookup(self) -> Union[Combinable, Query, int]: ...

class IntegerGreaterThanOrEqual(
    IntegerFieldFloatRounding, GreaterThanOrEqual
): ...
class IntegerLessThan(IntegerFieldFloatRounding, LessThan): ...

class In(FieldGetDbPrepValueIterableMixin, BuiltinLookup):
    bilateral_transforms: List[Type[lookups.Transform]]
    contains_aggregate: bool
    lhs: Expression
    rhs: Any
    lookup_name: str = ...
    def process_rhs(
        self, compiler: SQLCompiler, connection: DatabaseWrapper
    ) -> Tuple[str, Tuple]: ...
    def get_rhs_op(self, connection: DatabaseWrapper, rhs: str) -> str: ...
    def as_sql(
        self, compiler: SQLCompiler, connection: DatabaseWrapper
    ) -> Tuple[str, List[Union[int, str]]]: ...
    def split_parameter_list_as_sql(self, compiler: Any, connection: Any): ...

class PatternLookup(BuiltinLookup):
    param_pattern: str = ...
    prepare_rhs: bool = ...
    def get_rhs_op(self, connection: DatabaseWrapper, rhs: str) -> str: ...
    def process_rhs(
        self, qn: SQLCompiler, connection: DatabaseWrapper
    ) -> Tuple[str, List[Any]]: ...

class Contains(PatternLookup):
    bilateral_transforms: List[Type[lookups.Transform]]
    contains_aggregate: bool
    lhs: Expression
    rhs: Union[Expression, str]
    lookup_name: str = ...

class IContains(Contains):
    bilateral_transforms: List[Any]
    contains_aggregate: bool
    lhs: expressions.Col
    rhs: Union[Expression, str]
    lookup_name: str = ...

class StartsWith(PatternLookup):
    bilateral_transforms: List[Any]
    contains_aggregate: bool
    lhs: expressions.Col
    rhs: Union[Expression, str]
    lookup_name: str = ...
    param_pattern: str = ...

class IStartsWith(StartsWith):
    bilateral_transforms: List[Any]
    contains_aggregate: bool
    lhs: expressions.Col
    rhs: Union[Expression, str]
    lookup_name: str = ...

class EndsWith(PatternLookup):
    bilateral_transforms: List[Any]
    contains_aggregate: bool
    lhs: expressions.Col
    rhs: Union[Expression, str]
    lookup_name: str = ...
    param_pattern: str = ...

class IEndsWith(EndsWith):
    bilateral_transforms: List[Any]
    contains_aggregate: bool
    lhs: expressions.Col
    rhs: Union[Expression, str]
    lookup_name: str = ...

class Range(FieldGetDbPrepValueIterableMixin, BuiltinLookup):
    bilateral_transforms: List[Type[lookups.Transform]]
    contains_aggregate: bool
    lhs: Expression
    rhs: Union[
        List[datetime.datetime],
        Tuple[
            Union[expressions.F, int],
            Union[datetime.datetime, int],
        ],
    ]
    lookup_name: str = ...
    def get_rhs_op(
        self, connection: DatabaseWrapper, rhs: Tuple[str, str]
    ) -> str: ...

class IsNull(BuiltinLookup):
    bilateral_transforms: List[Any]
    contains_aggregate: bool
    lhs: Expression
    rhs: bool
    lookup_name: str = ...
    prepare_rhs: bool = ...
    def as_sql(
        self, compiler: SQLCompiler, connection: DatabaseWrapper
    ) -> Tuple[str, List[Any]]: ...

class Regex(BuiltinLookup):
    bilateral_transforms: List[Any]
    contains_aggregate: bool
    lhs: expressions.Col
    rhs: str
    lookup_name: str = ...
    prepare_rhs: bool = ...
    def as_sql(
        self, compiler: SQLCompiler, connection: DatabaseWrapper
    ) -> Tuple[str, List[str]]: ...

class IRegex(Regex):
    bilateral_transforms: List[Any]
    contains_aggregate: bool
    lhs: expressions.Col
    rhs: str
    lookup_name: str = ...

class YearLookup(Lookup):
    def year_lookup_bounds(
        self, connection: DatabaseWrapper, year: int
    ) -> List[str]: ...

class YearComparisonLookup(YearLookup):
    bilateral_transforms: List[Any]
    lhs: expressions.Value
    rhs: expressions.Value
    def as_sql(
        self, compiler: SQLCompiler, connection: DatabaseWrapper
    ) -> Tuple[str, List[str]]: ...
    def get_rhs_op(self, connection: DatabaseWrapper, rhs: str) -> str: ...
    def get_bound(self, start: datetime, finish: datetime) -> Any: ...

class YearExact(YearLookup, Exact):
    bilateral_transforms: List[Any]
    contains_aggregate: bool
    lhs: django.db.models.functions.datetime.ExtractYear
    rhs: Union[django.db.models.functions.datetime.Extract, int, str]
    lookup_name: str = ...
    def as_sql(
        self, compiler: SQLCompiler, connection: DatabaseWrapper
    ) -> Tuple[str, List[str]]: ...

class YearGt(YearComparisonLookup):
    bilateral_transforms: List[Any]
    contains_aggregate: bool
    lhs: django.db.models.functions.datetime.ExtractYear
    rhs: int
    lookup_name: str = ...
    def get_bound(self, start: str, finish: str) -> str: ...

class YearGte(YearComparisonLookup):
    bilateral_transforms: List[Any]
    contains_aggregate: bool
    lhs: django.db.models.functions.datetime.ExtractYear
    rhs: int
    lookup_name: str = ...
    def get_bound(self, start: str, finish: str) -> str: ...

class YearLt(YearComparisonLookup):
    bilateral_transforms: List[Any]
    contains_aggregate: bool
    lhs: django.db.models.functions.datetime.ExtractYear
    rhs: int
    lookup_name: str = ...
    def get_bound(self, start: str, finish: str) -> str: ...

class YearLte(YearComparisonLookup):
    bilateral_transforms: List[Any]
    contains_aggregate: bool
    lhs: django.db.models.functions.datetime.ExtractYear
    rhs: int
    lookup_name: str = ...
    def get_bound(self, start: str, finish: str) -> str: ...
