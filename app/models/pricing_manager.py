from dataclasses import dataclass
from typing import Dict, List, Optional, Any
from datetime import datetime
from models.feature import Feature
from models.usage_limit import UsageLimit
from models.plan import Plan
from app.models.add_on import AddOn


@dataclass
class PricingManager:
    _syntax_version: Version ##TODO: version viene del updaters
    _saas_name: str
    _url: str
    _created_at: datetime
    _version: str
    _currency: str
    _tags: List[str]
    _billing: Dict[str, float]
    _variables: Dict[str, Any]
    _features: Dict[str, Feature]
    _usage_limits: Dict[str, UsageLimit]
    _plans: Dict[str, Plan]
    _add_ons: Dict[str, AddOn]
    
    # -------- Propiedades protegidas --------
    @property
    def syntax_version(self) -> Version:
        return self._syntax_version
    @syntax_version.setter
    def syntax_version(self, v: Version) -> None:
        self._syntax_version = v

    @property
    def saas_name(self) -> str:
        return self._saas_name
    @saas_name.setter
    def saas_name(self, v: str) -> None:
        self._saas_name = v

    @property
    def url(self) -> str:
        return self._url
    @url.setter
    def url(self, v: str) -> None:
        self._url = v

    @property
    def created_at(self) -> datetime:
        return self._created_at
    @created_at.setter
    def created_at(self, v: datetime) -> None:
        self._created_at = v

    @property
    def version(self) -> str:
        return self._version
    @version.setter
    def version(self, v: str) -> None:
        self._version = v

    @property
    def currency(self) -> str:
        return self._currency
    @currency.setter
    def currency(self, v: str) -> None:
        self._currency = v

    @property
    def tags(self) -> List[str]:
        return self._tags
    @tags.setter
    def tags(self, v: List[str]) -> None:
        self._tags = v

    @property
    def billing(self) -> Dict[str, float]:
        return self._billing
    @billing.setter
    def billing(self, v: Dict[str, float]) -> None:
        self._billing = v

    @property
    def variables(self) -> Dict[str, Any]:
        return self._variables
    @variables.setter
    def variables(self, v: Dict[str, Any]) -> None:
        self._variables = v

    @property
    def features(self) -> Dict[str, Feature]:
        return self._features
    @features.setter
    def features(self, v: Dict[str, Feature]) -> None:
        self._features = v

    @property
    def usage_limits(self) -> Dict[str, UsageLimit]:
        return self._usage_limits
    @usage_limits.setter
    def usage_limits(self, v: Dict[str, UsageLimit]) -> None:
        self._usage_limits = v

    @property
    def plans(self) -> Dict[str, Plan]:
        return self._plans
    @plans.setter
    def plans(self, v: Dict[str, Plan]) -> None:
        self._plans = v

    @property
    def add_ons(self) -> Dict[str, AddOn]:
        return self._add_ons
    @add_ons.setter
    def add_ons(self, v: Dict[str, AddOn]) -> None:
        self._add_ons = v

    # -------- Lógica --------
    def __post_init__(self):
    # Inicialización post-constructor para asegurar que las listas y diccionarios no sean None
        self.tags = self.tags or []
        self.billing = self.billing or {}
        self.variables = self.variables or {}
        self.features = self.features or {}
        self.usage_limits = self.usage_limits or {}
        self.plans = self.plans or {}
        self.add_ons = self.add_ons or {}

    def __eq__(self, other):
        if not isinstance(other, PricingManager):
            return False
        return (
            self.syntax_version == other.syntax_version and
            self.saas_name == other.saas_name and
            self.url == other.url and
            self.created_at == other.created_at and
            self.version == other.version and
            self.currency == other.currency and
            self.tags == other.tags and
            self.billing == other.billing and
            self.variables == other.variables and
            self.features == other.features and
            self.usage_limits == other.usage_limits and
            self.plans == other.plans and
            self.add_ons == other.add_ons
        )

    def __hash__(self):
        return hash(
            (
                self.syntax_version,
                self.saas_name,
                self.url,
                self.created_at,
                self.version,
                self.currency,
                tuple(self.tags),
                tuple(self.billing.items()),
                tuple(self.variables.items()),
                tuple(self.features.items()),
                tuple(self.usage_limits.items()),
                tuple(self.plans.items()),
                tuple(self.add_ons.items())
            )
        )

    def __str__(self):
        return (f"PricingManager [syntax_version={self.syntax_version}, "
                f"saas_name={self.saas_name}, url={self.url}, "
                f"created_at={self.created_at}, version={self.version}, "
                f"currency={self.currency}, tags={self.tags}, "
                f"billing={self.billing}, variables={self.variables}, "
                f"features={self.features}, usage_limits={self.usage_limits}, "
                f"plans={self.plans}, add_ons={self.add_ons}]")

    def validate_feature_tags(self) -> None:

        for feature in self.features.values():
            if feature.tag is not None and feature.tag not in self.tags:
                raise ValueError(f"Tag {feature.tag} not found in pricing configuration")
