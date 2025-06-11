from typing import TypeVar, Generic
from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    model_config = ConfigDict(
        extra="ignore",
        use_enum_values=True,
        from_attributes=True,
        validate_assignment=True,
        populate_by_name=True,
        coerce_numbers_to_str=True,
        arbitrary_types_allowed=True,
    )


class BaseResponse(BaseSchema):
    errcode: int
    errmsg: str


T = TypeVar("T")

class BasePaginationResponse(BaseResponse, Generic[T]):
    total: int
    has_more: bool
    next: int
    records: list[T]
