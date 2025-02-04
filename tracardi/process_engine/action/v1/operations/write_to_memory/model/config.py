from typing import Optional

from pydantic import validator

from tracardi.domain.named_entity import NamedEntity
from tracardi.service.plugin.domain.config import PluginConfig


class Config(PluginConfig):
    key: str
    prefix: Optional[str] = ""
    value: str
    ttl: Optional[int] = 0
    resource: Optional[NamedEntity] = NamedEntity(name="Local redis", id="")

    @validator("key")
    def must_not_be_empty(cls, value):
        if value == "":
            raise ValueError("This field can not be empty")
        return value
