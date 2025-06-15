from dataclasses import dataclass
from typing import Optional, Any
import re

@dataclass
class FeatureStatus:
    _eval: bool
    _used: object
    _limit: object
    
    # -------- Propiedades protegidas --------
    @property
    def eval(self) -> bool:
        return self._eval
    @eval.setter
    def eval(self, value: bool) -> None:
        self._eval = value
    
    @property
    def used(self) -> object:
        return self._used
    @used.setter
    def used(self, value: object) -> None:
        self._used = value
    
    @property
    def limit(self) -> object:
        return self._limit
    @limit.setter
    def limit(self, value: object) -> None:
        self._limit = value
    
    @staticmethod
    def compute_feature_evaluation(expression: str, plan_context_manager: Any) -> Optional[bool]:

        if expression is None:
            raise ValueError("expression was null. A expression must be provided to compute its evaluation")
            
        if expression.strip() == "":
            return False

        try: ##TODO
            # Aquí se debería implementar la lógica específica de evaluación
            # que corresponda a tu caso de uso
            return bool(eval(expression, {}, {"plan": plan_context_manager}))
        except:
            return None

    @staticmethod
    def compute_user_context_variable(expression: str) -> Optional[str]:

        if "<" not in expression and ">" not in expression:
            return None

        try:
            match = re.search(r'\[\"\'(.*?)\"\'\]', expression)
            if match:
                return match.group(1).strip()
            return None
        except:
            return None
