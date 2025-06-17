from dataclasses import dataclass
from typing import Optional, Dict, Any

from app.models.feature import Feature
from app.models.enums.feature_type import FeatureType
from app.models.enums.automation_type import AutomationType


@dataclass
class Automation(Feature):
    _automation_type: Optional[AutomationType] = None

    # Getter y setter
    @property
    def automation_type(self): return self._automation_type
    @automation_type.setter
    def automation_type(self, value): self._automation_type = value

    # Sobrescribe serialize_feature como en Java
    def serialize_feature(self) -> Dict[str, Any]:
        result = self.feature_attributes_map()
        result["type"] = FeatureType.AUTOMATION.value
        if self._automation_type is not None:
            result["automationType"] = self._automation_type.value
        return result

    def __str__(self):
        return (f"Automation(name={self._name}, valueType={self._value_type}, "
                f"defaultValue={self._default_value}, value={self._value}, "
                f"automationType={self._automation_type})")

    def __eq__(self, other):
        if not isinstance(other, Automation):
            return False
        return (super().__eq__(other) and self._automation_type == other._automation_type)

    def __hash__(self):
        return hash((super().__hash__(), self._automation_type))
