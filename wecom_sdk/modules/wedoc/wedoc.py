from wecom_sdk.exceptions.general import SDKException
from wecom_sdk.modules.base import WecomBaseClient
from wecom_sdk.schemas.wedoc import ModDocMemberIn, BaseResponse, CreateDocIn, CreateDocResponse
from wecom_sdk.utils.requests import HttpxRequest


class WecomWedocClient(WecomBaseClient):

    async def mod_doc_member(self, data: ModDocMemberIn) -> BaseResponse:
        url = self.BASE_URL + "/wedoc/mod_doc_member"
        params = {
            "access_token": await self.access_token,
        }
        resp = BaseResponse(**await HttpxRequest.post(url=url, params=params, json=data.model_dump()))
        
        if resp.errcode == 0:
            return resp
        else:
            raise SDKException(resp.errcode, resp.errmsg)

    async def create_doc(self, data: CreateDocIn) -> CreateDocResponse:
        url = self.BASE_URL + "/wedoc/create_doc"
        params = {
            "access_token": await self.access_token,
        }
        resp = CreateDocResponse(**await HttpxRequest.post(url=url, params=params, json=data.model_dump()))
        
        if resp.errcode == 0:
            return resp
        else:
            raise SDKException(resp.errcode, resp.errmsg)
      
