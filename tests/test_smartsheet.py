import pytest

from wecom_sdk.modules.wedoc.smartsheet import WecomSmartsheetClient
from wecom_sdk.schemas.smartsheet import GetSheetIn, GetRecordIn


class TestAccessToken:
    @pytest.fixture
    def setup(self) -> WecomSmartsheetClient:
        return WecomSmartsheetClient(
            corpid="your_corpid",
            corpsecret="your_corpsecret",
        )

    @pytest.mark.asyncio
    async def test_get_sheet(self, setup: WecomSmartsheetClient):
        # 使用 GetSheetIn 类型作为参数传递
        sheet = await setup.get_sheet(GetSheetIn(
            doc_id="test_doc_id"
        ))

        assert sheet is not None

    @pytest.mark.asyncio
    async def test_get_records(self, setup: WecomSmartsheetClient):
        records = await setup.get_records(GetRecordIn(
            docid="test_docid",
            sheet_id="test_sheet_id",
            view_id="test_view_id",
        ))

        assert records is not None
