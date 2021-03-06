from typing import Any, Dict, List, Optional, Tuple, Union

from django.db.backends.base.introspection import (BaseDatabaseIntrospection,
                                                   FieldInfo, TableInfo)
from django.db.backends.utils import CursorWrapper
from django.db.models.fields import Field

field_size_re: Any

def get_field_size(name: str) -> Optional[int]: ...

class FlexibleFieldLookupDict:
    base_data_types_reverse: Any = ...
    def __getitem__(
        self, key: str
    ) -> Union[Tuple[str, Dict[str, int]], str]: ...

class DatabaseIntrospection(BaseDatabaseIntrospection):
    connection: django.db.backends.sqlite3.base.DatabaseWrapper
    data_types_reverse: Any = ...
    def get_table_list(self, cursor: CursorWrapper) -> List[TableInfo]: ...
    def get_table_description(
        self, cursor: CursorWrapper, table_name: str
    ) -> List[FieldInfo]: ...
    def get_sequences(
        self,
        cursor: CursorWrapper,
        table_name: str,
        table_fields: List[Field] = ...,
    ) -> List[Dict[str, str]]: ...
    def get_relations(
        self, cursor: CursorWrapper, table_name: str
    ) -> Dict[str, Tuple[str, str]]: ...
    def get_key_columns(
        self, cursor: CursorWrapper, table_name: str
    ) -> List[Tuple[str, str, str]]: ...
    def get_primary_key_column(
        self, cursor: CursorWrapper, table_name: str
    ) -> Optional[str]: ...
    def get_constraints(
        self, cursor: CursorWrapper, table_name: str
    ) -> Dict[str, Dict[str, Union[List[str], bool]]]: ...
