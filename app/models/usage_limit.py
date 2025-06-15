from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
import pickle

from app.models.enums.value_type import ValueType


class CloneUsageLimitException(Exception):
    pass


@dataclass
class Usage_limit(ABC):
    _name: Optional[str] = None
    _description: Optional[str] = None
    _value_type: Optional[ValueType] = None  # puedes sustituir por un Enum si lo tienes
    _default_value: Optional[Any] = None
    _type: Optional[UsageLimitType] = None  # UsageLimitType enum
    _unit: Optional[str] = None
    _linked_features: Optional[List[str]] = field(default_factory=list)
    _expression: Optional[str] = None
    _server_expression: Optional[str] = None
    _value: Any = field(default=None, repr=False, compare=False)  # transient

    # -------- Getters y setters --------
    @property
    def name(self): return self._name
    @name.setter
    def name(self, val): self._name = val

    @property
    def description(self): return self._description
    @description.setter
    def description(self, val): self._description = val

    @property
    def value_type(self): return self._value_type
    @value_type.setter
    def value_type(self, val): self._value_type = val

    @property
    def default_value(self): return self._default_value
    @default_value.setter
    def default_value(self, val): self._default_value = val

    @property
    def type(self): return self._type
    @type.setter
    def type(self, val): self._type = val

    @property
    def unit(self): return self._unit
    @unit.setter
    def unit(self, val): self._unit = val

    @property
    def value(self): return self._value
    @value.setter
    def value(self, val): self._value = val

    @property
    def linked_features(self): return self._linked_features
    @linked_features.setter
    def linked_features(self, val): self._linked_features = val

    @property
    def expression(self): return self._expression
    @expression.setter
    def expression(self, val): self._expression = val

    @property
    def server_expression(self): return self._server_expression
    @server_expression.setter
    def server_expression(self, val): self._server_expression = val

    # -------- Funcionalidad lógica --------
    def is_linked_to_feature(self, feature_name: str) -> bool:
        return feature_name in self._linked_features

    def serialize(self) -> Dict[str, Any]:
        result = {}
        if self._description is not None:
            result["description"] = self._description
        if self._value_type is not None:
            result["valueType"] = str(self._value_type)
        if self._default_value is not None:
            result["defaultValue"] = self._default_value
        if self._unit is not None:
            result["unit"] = self._unit
        if self._type is not None:
            result["type"] = str(self._type)
        if self._linked_features:
            result["linkedFeatures"] = self._linked_features
        if self._expression is not None:
            result["expression"] = self._expression
        if self._server_expression is not None:
            result["serverExpression"] = self._server_expression
        return result

    def __getstate__(self):
        state = self.__dict__.copy()
        state.pop("_value", None)  # simulamos transient
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self._value = None

    @staticmethod
    def clone_usage_limit(original: 'Usage_limit') -> 'Usage_limit':
        try:
            return pickle.loads(pickle.dumps(original))
        except Exception:
            raise CloneUsageLimitException("Error cloning usageLimit")

    def __eq__(self, other):
        if not isinstance(other, Usage_limit):
            return False
        return (
            self._name == other._name and
            self._description == other._description and
            self._value_type == other._value_type and
            self._default_value == other._default_value and
            self._type == other._type and
            self._unit == other._unit and
            self._value == other._value and
            self._linked_features == other._linked_features and
            self._expression == other._expression and
            self._server_expression == other._server_expression
        )

    def __hash__(self):
        return hash((
            self._name, self._description, self._value_type, self._default_value,
            self._type, self._unit, tuple(self._linked_features),
            self._expression, self._server_expression
        ))

    def __str__(self):
        return (
            f"UsageLimit(name={self._name}, description={self._description}, "
            f"value_type={self._value_type}, default_value={self._default_value}, "
            f"type={self._type}, unit={self._unit}, linked_features={self._linked_features}, "
            f"expression={self._expression}, server_expression={self._server_expression})"
        )