import pytest
import os

from wecom_sdk.modules.wedoc.smartsheet import WecomSmartsheetClient
from wecom_sdk.schemas.smartsheet import GetSheetIn, GetRecordIn

corpid = os.environ.get('WECOM_CORPID', '')
corpsecret = os.environ.get('WECOM_CORPSECRET', '')
doc_id = os.environ.get('WECOM_DOC_ID', '')
sheet_id = os.environ.get('WECOM_SHEET_ID', '')


class TestSmartsheet:
    @pytest.fixture
    def setup(self) -> WecomSmartsheetClient:
        return WecomSmartsheetClient(
            corpid=corpid,
            corpsecret=corpsecret,
        )

    @pytest.mark.asyncio
    async def test_get_sheet(self, setup: WecomSmartsheetClient):
        sheet = await setup.get_sheet(GetSheetIn(
            doc_id=doc_id
        ))

        assert sheet is not None

    @pytest.mark.asyncio
    async def test_get_records(self, setup: WecomSmartsheetClient):
        records = await setup.get_records(GetRecordIn(
            docid=doc_id,
            sheet_id=sheet_id,
        ))

        assert records is not None
