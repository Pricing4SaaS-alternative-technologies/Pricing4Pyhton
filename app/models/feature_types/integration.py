from dataclasses import dataclass
from typing import Dict

from app.models.feature import Feature
from app.models.enums.feature_type import FeatureType


@dataclass
class Information(Feature):
    def serialize_feature(self) -> Dict[str, any]:
        attributes = self.feature_attributes_map()
        attributes["type"] = FeatureType.INFORMATION.value
        return attributes
