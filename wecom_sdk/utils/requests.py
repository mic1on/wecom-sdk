import httpx

from wecom_sdk.exceptions.general import SDKException


class HttpxRequest:
    @classmethod
    async def get(
        cls, url: str, params: dict | None = None, headers: dict | None = None
    ) -> dict:
        """
        发送GET请求
        @param url: 请求URL
        @param params: 请求参数
        @param headers: 请求头
        @return: 响应内容
        """
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params, headers=headers)
            try:
                response_data = response.json()
                if 'errcode' in response_data and response_data['errcode'] != 0:
                    raise SDKException(response_data.get('errcode', -1), response_data.get('errmsg', 'Unknown error'))
                return response_data
            except ValueError:
                raise SDKException(-1, 'Failed to parse response')

    @classmethod
    async def post(
        cls,
        url: str,
        params: dict | None = None,
        data: dict | None = None,
        json: dict | None = None,
        headers: dict | None = None,
    ) -> dict:
        """
        发送POST请求
        @param url: 请求URL
        @param params: 请求参数
        @param headers: 请求头
        @return: 响应内容
        """
        async with httpx.AsyncClient() as client:
            response = await client.post(
                url, params=params, data=data, json=json, headers=headers
            )
            try:
                response_data = response.json()
                if 'errcode' in response_data and response_data['errcode'] != 0:
                    raise SDKException(response_data.get('errcode', -1), response_data.get('errmsg', 'Unknown error'))
                return response_data
            except ValueError:
                raise SDKException(-1, 'Failed to parse response')
