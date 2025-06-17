from app.models.feature import Feature
from app.models.enums.feature_type import FeatureType
from typing import Dict

class Support(Feature):
    def serialize_feature(self) -> Dict[str, any]:
        attributes = self.feature_attributes_map()
        attributes["type"] = FeatureType.SUPPORT.name
        return attributes
