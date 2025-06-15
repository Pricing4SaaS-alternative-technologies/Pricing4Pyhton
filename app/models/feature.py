from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import Any, Optional, Dict
import pickle

from app.models.enums.value_type import ValueType


class CloneFeatureException(Exception):
    pass


@dataclass
class Feature(ABC):
    _name: Optional[str] = None
    _description: Optional[str] = None
    _value_type: Optional[ValueType] = None
    _default_value: Any = None
    _expression: Optional[str] = None
    _server_expression: Optional[str] = None
    _tag: Optional[str] = None
    _value: Any = field(default=None, repr=False, compare=False)#el trnsient

    # -------- Propiedades protegidas --------
    @property
    def name(self): return self._name
    @name.setter
    def name(self, v): self._name = v

    @property
    def description(self): return self._description
    @description.setter
    def description(self, v): self._description = v

    @property
    def value_type(self): return self._value_type
    @value_type.setter
    def value_type(self, v): self._value_type = v

    @property
    def default_value(self): return self._default_value
    @default_value.setter
    def default_value(self, v): self._default_value = v

    @property
    def expression(self): return self._expression
    @expression.setter
    def expression(self, v): self._expression = v

    @property
    def server_expression(self): return self._server_expression
    @server_expression.setter
    def server_expression(self, v): self._server_expression = v

    @property
    def tag(self): return self._tag
    @tag.setter
    def tag(self, v): self._tag = v

    @property
    def value(self): return self._value
    @value.setter
    def value(self, v): self._value = v

    # -------- Lógica --------
    def prepare_to_plan_writing(self):
        self._name = None
        self._description = None
        self._value_type = None
        self._default_value = None
        self._value = None
        self._expression = None
        self._server_expression = None
        self._tag = None

    def has_overwritten_default_value(self) -> bool:
        return self._default_value != self._value

    def feature_attributes_map(self) -> Dict[str, Any]:
        result = {}
        for k, v in {
            "description": self._description,
            "valueType": self._value_type,
            "defaultValue": self._default_value,
            "expression": self._expression,
            "serverExpression": self._server_expression,
            "tag": self._tag
        }.items():
            if v is not None:
                result[k] = v
        return result 

    def __getstate__(self):
        state = self.__dict__.copy()
        state.pop("_value", None)  # simulamos 'transient'
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self._value = None

    @staticmethod
    def clone_feature(original: 'Feature') -> 'Feature':
        try:
            return pickle.loads(pickle.dumps(original))
        except Exception:
            raise CloneFeatureException("Error cloning feature")

    @abstractmethod
    def serialize_feature(self) -> Dict[str, Any]:
        pass
