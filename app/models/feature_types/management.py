from dataclasses import dataclass
from typing import Any, Dict
from app.models.feature import Feature
from app.models.enums.feature_type import FeatureType

@dataclass
class Management(Feature):
    def serialize_feature(self) -> Dict[str, Any]:
        attributes = self.feature_attributes_map()
        attributes["type"] = FeatureType.MANAGEMENT.name
        return attributes