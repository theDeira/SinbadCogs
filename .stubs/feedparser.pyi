# These stubs are possibly wrong.
# They were generated with monkeytype and are "good enough"
# After some minor corrections
from io import BytesIO
from time import struct_time
from typing import Any, Callable, Dict, List, Optional, Tuple, Union
from xml.sax.xmlreader import AttributesNSImpl  # nosec

def _l2bytes(l: List[int]) -> bytes: ...
def _makeSafeAbsoluteURI(base: str, rel: Optional[str] = ...) -> str: ...
def _open_resource(
    url_file_stream_or_string: bytes,
    etag: None,
    modified: None,
    agent: None,
    referrer: None,
    handlers: List[Any],
    request_headers: Dict[Any, Any],
) -> BytesIO: ...
def _parse_date(dateString: str) -> struct_time: ...
def _parse_date_asctime(dt: str) -> None: ...
def _parse_date_perforce(aDateString: str) -> None: ...
def _parse_date_rfc822(date: str) -> None: ...
def _parse_date_w3dtf(datestr: str) -> struct_time: ...
def _resolveRelativeURIs(
    htmlSource: str, baseURI: str, encoding: str, _type: str
) -> str: ...
def _s2bytes(s: str) -> bytes: ...
def _sanitizeHTML(htmlSource: str, encoding: str, _type: str) -> str: ...
def _urljoin(base: str, uri: str) -> str: ...
def convert_to_utf8(
    http_headers: Dict[Any, Any], data: bytes
) -> Tuple[bytes, str, None]: ...
def parse(
    url_file_stream_or_string: bytes,
    etag: None = ...,
    modified: None = ...,
    agent: None = ...,
    referrer: None = ...,
    handlers: None = ...,
    request_headers: None = ...,
    response_headers: None = ...,
) -> FeedParserDict: ...
def registerDateHandler(func: Callable) -> None: ...
def replace_doctype(data: bytes) -> Tuple[None, bytes, Dict[Any, Any]]: ...

class FeedParserDict:
    def __iter__(self): ...
    def __contains__(self, key: str) -> bool: ...
    def __getattr__(
        self, key: str
    ) -> Union[str, FeedParserDict, List[FeedParserDict], struct_time, int]: ...
    def __getitem__(self, key: str) -> Any: ...
    def __hash__(self) -> int: ...
    def __setitem__(self, key: str, value: Any) -> None: ...
    def get(
        self, key: str, default: Optional[Union[List[FeedParserDict], str, int]] = ...
    ) -> Optional[Union[str, List[FeedParserDict], struct_time, int]]: ...
    def setdefault(
        self, key: str, value: Union[str, FeedParserDict, List[FeedParserDict], bool]
    ) -> Union[str, FeedParserDict, List[FeedParserDict], bool]: ...

class _FeedParserMixin:
    def __init__(
        self, baseuri: Optional[str] = ..., baselang: None = ..., encoding: str = ...
    ) -> None: ...
    def _cdf_common(self, attrsD: Dict[Any, Any]) -> None: ...
    def _end_author(self) -> None: ...
    def _end_channel(self) -> None: ...
    def _end_content(self) -> None: ...
    def _end_guid(self) -> None: ...
    def _end_item(self) -> None: ...
    def _end_link(self) -> None: ...
    def _end_media_thumbnail(self) -> None: ...
    def _end_name(self) -> None: ...
    def _end_title(self) -> None: ...
    def _end_updated(self) -> None: ...
    def _end_url(self) -> None: ...
    def _getAttribute(self, attrsD: Dict[Any, Any], name: str) -> None: ...
    def _getContext(self) -> FeedParserDict: ...
    def _isBase64(
        self, attrsD: Dict[str, str], contentparams: FeedParserDict
    ) -> int: ...
    def _itsAnHrefDamnIt(self, attrsD: Dict[str, str]) -> Dict[str, str]: ...
    def _mapToStandardPrefix(self, name: str) -> str: ...
    def _normalize_attributes(self, kv: Tuple[str, str]) -> Tuple[str, str]: ...
    def _save(
        self, key: str, value: Union[bool, str, struct_time], overwrite: bool = ...
    ) -> None: ...
    def _save_author(self, key: str, value: str, prefix: str = ...) -> None: ...
    def _start_author(self, attrsD: Dict[Any, Any]) -> None: ...
    def _start_content(self, attrsD: Dict[str, str]) -> None: ...
    def _start_feed(self, attrsD: Dict[str, str]) -> None: ...
    def _start_guid(self, attrsD: Dict[Any, Any]) -> None: ...
    def _start_item(self, attrsD: Dict[Any, Any]) -> None: ...
    def _start_link(self, attrsD: Dict[str, str]) -> None: ...
    def _start_media_thumbnail(self, attrsD: Dict[str, str]) -> None: ...
    def _start_name(self, attrsD: Dict[Any, Any]) -> None: ...
    def _start_title(self, attrsD: Dict[Any, Any]) -> None: ...
    def _start_updated(self, attrsD: Dict[Any, Any]) -> None: ...
    def _start_url(self, attrsD: Dict[Any, Any]) -> None: ...
    def _sync_author_detail(self, key: str = ...) -> None: ...
    def decodeEntities(self, element: str, data: str) -> str: ...
    def handle_data(self, text: str, escape: int = ...) -> None: ...
    def mapContentType(self, contentType: str) -> str: ...
    def pop(self, element: str, stripWhitespace: int = ...) -> Optional[str]: ...
    def popContent(self, tag: str) -> str: ...
    def push(self, element: str, expectingText: int) -> None: ...
    def pushContent(
        self,
        tag: str,
        attrsD: Dict[str, str],
        defaultContentType: str,
        expectingText: int,
    ) -> None: ...
    def resolveURI(self, uri: str) -> str: ...
    def trackNamespace(self, prefix: Optional[str], uri: str) -> None: ...
    def unknown_endtag(self, tag: str) -> None: ...
    def unknown_starttag(self, tag: str, attrs: List[Tuple[str, str]]) -> None: ...

class _StrictFeedParser:
    def __init__(self, baseuri: str, baselang: None, encoding: str) -> None: ...
    def characters(self, text: str) -> None: ...
    def endElementNS(self, name: Tuple[str, str], qname: None) -> None: ...
    def startElementNS(
        self, name: Tuple[str, str], qname: None, attrs: AttributesNSImpl
    ) -> None: ...
    def startPrefixMapping(self, prefix: Optional[str], uri: str) -> None: ...
