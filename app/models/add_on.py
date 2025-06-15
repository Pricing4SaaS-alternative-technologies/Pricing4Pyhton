from dataclasses import dataclass
from typing import List, Dict, Optional, Any
from abc import ABC
from collections import OrderedDict

from models.feature import Feature
from models.usage_limit import UsageLimit


class AddOnException(Exception):
    pass


@dataclass
class AddOn(ABC):
    _name: str
    _description: str
    _available_for: List[str]
    _depends_on: List[str]
    _excludes: List[str]
    _price: object
    _unit: str
    _is_private: bool
    _features: Dict[str, Feature]
    _usage_limits: Dict[str, UsageLimit]
    _usage_limits_extensions: Dict[str, UsageLimit]
    
    
    # -------- Propiedades protegidas (no deberia ser necesario) --------
    @property
    def name(self): return self._name
    @name.setter
    def name(self, v): self._name = v
    
    @property
    def description(self): return self._description
    @description.setter
    def description(self, v): self._description = v
    
    @property
    def available_for(self): return self._available_for
    @available_for.setter
    def available_for(self, v): self._available_for = v
    
    @property
    def depends_on(self): return self._depends_on
    @depends_on.setter
    def depends_on(self, v): self._depends_on = v
    
    @property
    def excludes(self): return self._excludes
    @excludes.setter
    def excludes(self, v): self._excludes = v
    
    @property
    def price(self): return self._price
    @price.setter
    def price(self, v): self._price = v
    
    @property
    def unit(self): return self._unit
    @unit.setter
    def unit(self, v): self._unit = v
    
    @property
    def is_private(self): return self._is_private
    @is_private.setter
    def is_private(self, v): self._is_private = v
    
    @property
    def features(self): return self._features
    @features.setter
    def features(self, v): self._features = v
    
    @property
    def usage_limits(self): return self._usage_limits
    @usage_limits.setter
    def usage_limits(self, v): self._usage_limits = v
    
    @property
    def usage_limits_extensions(self): return self._usage_limits_extensions
    @usage_limits_extensions.setter
    def usage_limits_extensions(self, v): self._usage_limits_extensions = v

    # -------- Lógica --------
    def __post_init__(self): 
    # Inicialización post-constructor para asegurar que las listas y diccionarios no sean None
        self.available_for = self.available_for or []
        self.depends_on = self.depends_on or []
        self.excludes = self.excludes or []
        self.features = self.features or {}
        self.usage_limits = self.usage_limits or {}
        self.usage_limits_extensions = self.usage_limits_extensions or {}

    def __eq__(self, other):
        if not isinstance(other, AddOn):
            return False
        return (
            self.name == other.name and
            self.description == other.description and
            self.available_for == other.available_for and
            self.depends_on == other.depends_on and
            self.excludes == other.excludes and
            self.price == other.price and
            self.unit == other.unit and
            self.is_private == other.is_private and
            self.features == other.features and
            self.usage_limits == other.usage_limits and
            self.usage_limits_extensions == other.usage_limits_extensions
        )

    def __hash__(self):
        return hash(
            (
                self.name,
                self.description,
                tuple(self.available_for),
                tuple(self.depends_on),
                tuple(self.excludes),
                self.price,
                self.unit,
                self.is_private,
                tuple(self.features.items()),
                tuple(self.usage_limits.items()),
                tuple(self.usage_limits_extensions.items())
            )
        )

    def __str__(self):
        return (f"AddOn [name={self.name}, description={self.description}, "
                f"available_for={self.available_for}, depends_on={self.depends_on}, "
                f"excludes={self.excludes}, price={self.price}, unit={self.unit}, "
                f"is_private={self.is_private}, features={self.features}, "
                f"usage_limits={self.usage_limits}, "
                f"usage_limits_extensions={self.usage_limits_extensions}]"
        )

    def serialize_add_on(self) -> Dict[str, Any]:
        serialized_add_on = OrderedDict()

        if self.description is not None:
            serialized_add_on["description"] = self.description

        if self.available_for and self.available_for:
            serialized_add_on["availableFor"] = self.available_for

        if self.depends_on and self.depends_on:
            serialized_add_on["dependsOn"] = self.depends_on

        if self.excludes and self.excludes:
            serialized_add_on["excludes"] = self.excludes

        if self.is_private is not None and self.is_private:
            serialized_add_on["private"] = self.is_private

        if self.price is not None:
            serialized_add_on["price"] = self.price

        if self.unit is not None:
            serialized_add_on["unit"] = self.unit

        features = self.serialize_features()
        usage_limits = self.serialize_usage_limits()
        usage_limit_extensions = self.serialize_usage_limit_extensions()

        serialized_add_on["features"] = features
        serialized_add_on["usageLimits"] = usage_limits
        serialized_add_on["usageLimitsExtensions"] = usage_limit_extensions

        return serialized_add_on

    def serialize_value(self, value: Any) -> Optional[Dict[str, Any]]:
        if value is None:
            return None

        return {"value": value}

    def serialize_features(self) -> Optional[Dict[str, Any]]:
        if self.features is None:
            return None

        serialized_features = OrderedDict()
        for feature_name, feature_value in self.features.items():
            serialized_feature = self.serialize_value(feature_value)
            if serialized_feature:
                serialized_features[feature_name] = serialized_feature

        return serialized_features if serialized_features else None

    def serialize_usage_limits(self) -> Optional[Dict[str, Any]]:
        if self.usage_limits is None:
            return None

        serialized_usage_limits = OrderedDict()
        for limit_name, limit_value in self.usage_limits.items():
            serialized_limit = self.serialize_value(limit_value)
            if serialized_limit:
                serialized_usage_limits[limit_name] = serialized_limit

        return serialized_usage_limits if serialized_usage_limits else None

    def serialize_usage_limit_extensions(self) -> Optional[Dict[str, Any]]:
        if self.usage_limits_extensions is None:
            return None

        serialized_extensions = OrderedDict()
        for extension_name, extension_value in self.usage_limits_extensions.items():
            serialized_extension = self.serialize_value(extension_value)
            if serialized_extension:
                serialized_extensions[extension_name] = serialized_extension

        return serialized_extensions if serialized_extensions else None
