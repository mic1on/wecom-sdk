from wecom_sdk.exceptions.general import SDKException
from wecom_sdk.modules.base import WecomBaseClient
from wecom_sdk.schemas.smartsheet import GetSheetIn, GetSheetOut, GetRecordIn, GetRecordOut
from wecom_sdk.utils.requests import HttpxRequest


class WecomSmartsheetClient(WecomBaseClient):

    async def get_sheet(self, data: GetSheetIn) -> list:
        """
        获取表单
        @param data: 表单ID
        @return: 表单信息
        """
        url = self.BASE_URL + "/wedoc/smartsheet/get_sheet"
        params = {
            "access_token": await self.access_token,
        }
        resp = GetSheetOut(**await HttpxRequest.post(url=url, params=params, json=data.model_dump()))
        
        if resp.errcode == 0:
            return resp.sheet_list
        else:
            raise SDKException(resp.errcode, resp.errmsg)

    async def get_records(self, data: GetRecordIn) -> GetRecordOut:
        """
        获取表单记录
        @param data: 表单ID
        """
        
        url = self.BASE_URL + "/wedoc/smartsheet/get_records"
        params = {
            "access_token": await self.access_token,
        }
        resp = GetRecordOut(**await HttpxRequest.post(url=url, params=params, json=data.model_dump()))
        
        if resp.errcode == 0:
            return resp
        else:
            raise SDKException(resp.errcode, resp.errmsg)
