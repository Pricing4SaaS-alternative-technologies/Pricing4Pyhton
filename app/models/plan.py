from dataclasses import dataclass
from typing import Dict, Any, Optional
from models.feature import Feature
from models.usage_limit import UsageLimit
from collections import OrderedDict

@dataclass
class Plan:
    _name: str
    _description: str
    _price: object
    _unit: str
    _is_private: bool
    _features: Dict[str, Feature]
    _usage_limits: Dict[str, UsageLimit]
    
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
    
    # -------- Lógica --------
    def __post_init__(self):
        # Inicialización post-constructor para asegurar que las listas y diccionarios no sean None
        self.features = self.features or {}
        self.usage_limits = self.usage_limits or {}

    def __eq__(self, other):
        if not isinstance(other, Plan):
            return False
        return (
            self.name == other.name and
            self.description == other.description and
            self.price == other.price and
            self.unit == other.unit and
            self.is_private == other.is_private and
            self.features == other.features and
            self.usage_limits == other.usage_limits
        )

    def __hash__(self):
        return hash(
            (
                self.name,
                self.description,
                self.price,
                self.unit,
                self.is_private,
                tuple(self.features.items()),
                tuple(self.usage_limits.items())
            )
        )

    def __str__(self):
        return (f"Plan [name={self.name}, description={self.description}, "
                f"price={self.price}, unit={self.unit}, is_private={self.is_private}, "
                f"features={self.features}, usage_limits={self.usage_limits}]")

    def parse_to_map(self) -> Dict[str, Any]:
        # Convierte el plan en un diccionario ordenado
        plan_map = OrderedDict()
        plan_map["name"] = self.name
        plan_map["description"] = self.description
        plan_map["price"] = self.price
        plan_map["unit"] = self.unit
        plan_map["is_private"] = self.is_private
        plan_map["features"] = self.features
        plan_map["usage_limits"] = self.usage_limits
        return plan_map

    def serialize_plan(self) -> Dict[str, Any]:
        # Serializa el plan para su uso en JSON o similar
        attributes = OrderedDict()
        
        if self.description:
            attributes["description"] = self.description
        
        attributes["price"] = self.price
        
        if self.unit:
            attributes["unit"] = self.unit
        
        if self.is_private:
            attributes["private"] = self.is_private
        
        features = self._serialize_features()
        if features:
            attributes["features"] = features
        
        usage_limits = self._serialize_usage_limits()
        if usage_limits:
            attributes["usageLimits"] = usage_limits
        
        return attributes

    def _serialize_value(self, value: Any) -> Optional[Dict[str, Any]]:
        # Serializa un valor en un diccionario con la clave 'value'
        if value is None:
            return None
        return {"value": value}

    def _serialize_features(self) -> Optional[Dict[str, Any]]:
        # Serializa las características del plan
        if not self.features:
            return None
            
        serialized_features = OrderedDict()
        for feature in self.features.values():
            serialized = self._serialize_value(feature.value)
            if serialized:
                serialized_features[feature.name] = serialized
        
        return serialized_features if serialized_features else None

    def _serialize_usage_limits(self) -> Optional[Dict[str, Any]]:
        # Serializa los límites de uso del plan
        if not self.usage_limits:
            return None
            
        serializedUsageLimits = OrderedDict()
        for limit in self.usage_limits.values():
            serialized = self._serialize_value(limit.limit)
            if serialized:
                serializedUsageLimits[limit.name] = serialized
        
        return serializedUsageLimits if serializedUsageLimits else None
