from typing import Any, Dict, List, Optional
from wecom_sdk.schemas.base import BasePaginationResponse, BaseSchema, BaseResponse


class GetSheetIn(BaseSchema):
    """
    表单信息
    """
    doc_id: str
    sheet_id: Optional[str] = None
    need_all_type_sheet: Optional[bool] = None


class _GetSheetOut(BaseSchema):
    """
    表单信息
    """
    sheet_id: str
    title: str
    is_visible: bool
    type: str

class GetSheetOut(BaseResponse):
    """
    获取表单
    """
    sheet_list: list[_GetSheetOut]



class GetRecordIn(BaseSchema):
    """
    表单信息
    """
    docid: str
    sheet_id: str
    view_id: Optional[str] = None
    record_ids: Optional[List[str]] = None
    key_type: Optional[str] = None
    field_titles: Optional[List[str]] = None
    field_ids: Optional[List[str]] = None
    sort: Optional[List[Dict]] = None
    offset: Optional[int] = 0
    limit: Optional[int] = 100
    ver: Optional[int] = None
    filter_spec: Optional[Dict] = None
    
    class Config:
        extra = "forbid"
    


class _GetRecordOut(BaseSchema):
    record_id: str
    create_time: str
    update_time: str
    values: Dict[str, Any]
    creator_name: Optional[str] = None
    updater_name: Optional[str] = None
    
    class Config:
        extra = "ignore"

class GetRecordOut(BasePaginationResponse[_GetRecordOut]):
    """
    获取表单
    """
    pass
