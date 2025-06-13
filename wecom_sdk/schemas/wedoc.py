from typing import Any, Dict, List, Optional
from wecom_sdk.schemas.base import BasePaginationResponse, BaseSchema, BaseResponse


class ModDocMemberIn(BaseSchema):
    """
    修改文档成员
    """
    
    class _UpdateFileMember(BaseSchema):
        type: int
        auth: int
        userid: str
        external_userid: Optional[str] = None

    class _DelFileMember(BaseSchema):
        type: int
        userid: str
        tmp_external_userid: Optional[str] = None

    docid: str
    update_file_member_list: Optional[List[_UpdateFileMember]] = None
    del_file_member_list: Optional[List[_DelFileMember]] = None
    tmp_external_userid: Optional[str] = None


class CreateDocIn(BaseSchema):
    """
    创建文档请求参数
    """
    spaceid: str
    fatherid: str
    doc_type: str
    doc_name: str
    admin_users: List[str]


class CreateDocResponse(BaseResponse):
    """
    创建文档响应结果
    """
    url: str
    docid: str

