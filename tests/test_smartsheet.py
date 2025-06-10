import pytest

from wecom_sdk.modules.wedoc.smartsheet import WecomSmartsheetClient


class TestAccessToken:
    @pytest.fixture
    def setup(self) -> WecomSmartsheetClient:
        return WecomSmartsheetClient(
            corpid="your_corpid",
            corpsecret="your_corpsecret",
        )

    @pytest.mark.asyncio
    async def test_get_sheet(self, setup: WecomSmartsheetClient):
        sheet = await setup.get_sheet({"docid": ""})

        assert sheet is not None

    @pytest.mark.asyncio
    async def test_get_records(self, setup: WecomSmartsheetClient):
        records = await setup.get_records({"docid": "", "sheet_id": ""})

        assert records is not None
