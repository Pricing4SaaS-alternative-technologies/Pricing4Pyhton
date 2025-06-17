from dataclasses import dataclass, field
from typing import Any, Dict, Optional

from app.models.feature import Feature
from app.models.enums.feature_type import FeatureType


@dataclass
class Guarantee(Feature):
    _doc_url: Optional[str] = None

    @property
    def doc_url(self) -> Optional[str]:
        return self._doc_url

    @doc_url.setter
    def doc_url(self, value: str):
        self._doc_url = value

    def serialize_feature(self) -> Dict[str, Any]:
        attributes = self.feature_attributes_map()
        attributes["type"] = FeatureType.GUARANTEE.value
        if self._doc_url:
            attributes["docUrl"] = self._doc_url
        return attributes

    def __str__(self):
        return (
            f"Guarantee[name: {self._name}, valueType: {self._value_type}, "
            f"defaultValue: {self._default_value}, value: {self._value}, "
            f"docURL: {self._doc_url}]"
        )
