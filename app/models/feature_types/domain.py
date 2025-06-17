from dataclasses import dataclass
from typing import Dict, Any

from app.models.feature import Feature
from app.models.enums.feature_type import FeatureType


@dataclass
class Domain(Feature):
    def serialize_feature(self) -> Dict[str, Any]:
        attributes = self.feature_attributes_map()
        attributes["type"] = FeatureType.DOMAIN.value
        return attributes