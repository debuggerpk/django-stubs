from typing import Any, Callable, Dict, List, Optional, Union
from unittest.mock import MagicMock

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sites.models import Site
from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Page, Paginator
from django.http.request import HttpRequest
from django.http.response import (HttpResponse, HttpResponseNotAllowed,
                                  HttpResponseRedirect)
from django.template.response import TemplateResponse
from django.views.generic.list import ListView

logger: Any

class ContextMixin:
    extra_context: Any = ...
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]: ...

class View:
    http_method_names: Any = ...
    def __init__(self, **kwargs: Any) -> None: ...
    head: Any = ...
    request: Any = ...
    args: Any = ...
    kwargs: Any = ...
    def as_view(cls, **initkwargs: Any) -> Callable: ...
    def dispatch(
        self, request: HttpRequest, *args: Any, **kwargs: Any
    ) -> Union[HttpResponse, View]: ...
    def http_method_not_allowed(
        self, request: WSGIRequest, *args: Any, **kwargs: Any
    ) -> HttpResponseNotAllowed: ...
    def options(
        self, request: WSGIRequest, *args: Any, **kwargs: Any
    ) -> HttpResponse: ...

class TemplateResponseMixin:
    template_name: Any = ...
    template_engine: Any = ...
    response_class: Any = ...
    content_type: Any = ...
    def render_to_response(
        self,
        context: Union[
            Dict[str, Any],
            Dict[str, Optional[Union[List[Dict[str, str]], bool, ListView]]],
            Dict[
                str,
                Union[List[Dict[str, str]], bool, Page, Paginator, ListView],
            ],
            Dict[
                str, Union[AuthenticationForm, Site, TemplateResponseMixin, str]
            ],
            MagicMock,
        ],
        **response_kwargs: Any
    ) -> TemplateResponse: ...
    def get_template_names(self) -> List[str]: ...

class TemplateView(TemplateResponseMixin, ContextMixin, View):
    args: Tuple
    content_type: str
    extra_context: Dict[str, str]
    head: Callable
    kwargs: Dict[str, str]
    request: django.core.handlers.wsgi.WSGIRequest
    template_engine: str
    template_name: str
    def get(
        self, request: WSGIRequest, *args: Any, **kwargs: Any
    ) -> TemplateResponse: ...

class RedirectView(View):
    args: Tuple
    kwargs: Dict[str, Union[int, str]]
    request: django.core.handlers.wsgi.WSGIRequest
    permanent: bool = ...
    url: str = ...
    pattern_name: str = ...
    query_string: bool = ...
    def get_redirect_url(self, *args: Any, **kwargs: Any) -> Optional[str]: ...
    def get(
        self, request: WSGIRequest, *args: Any, **kwargs: Any
    ) -> HttpResponse: ...
    def head(
        self, request: WSGIRequest, *args: Any, **kwargs: Any
    ) -> HttpResponse: ...
    def post(
        self, request: WSGIRequest, *args: Any, **kwargs: Any
    ) -> HttpResponseRedirect: ...
    def options(
        self, request: WSGIRequest, *args: Any, **kwargs: Any
    ) -> HttpResponseRedirect: ...
    def delete(
        self, request: WSGIRequest, *args: Any, **kwargs: Any
    ) -> HttpResponseRedirect: ...
    def put(
        self, request: WSGIRequest, *args: Any, **kwargs: Any
    ) -> HttpResponseRedirect: ...
    def patch(
        self, request: WSGIRequest, *args: Any, **kwargs: Any
    ) -> HttpResponseRedirect: ...
