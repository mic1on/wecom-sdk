from typing import Optional
from wecom_sdk.schemas.base import BasePaginationResponse, BaseSchema, BaseResponse


class GetSheetIn(BaseSchema):
    """
    表单信息
    """
    doc_id: str
    sheet_id: Optional[str]
    need_all_type_sheet: Optional[bool]


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
    view_id: Optional[str]
    
    
class GetRecordOut(BasePaginationResponse):
    """
    获取表单
    """
    pass
