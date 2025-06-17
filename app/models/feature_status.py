from dataclasses import dataclass
from typing import Optional, Any
import re
from simpleeval import SimpleEval

from app.models.plan_context_manager import PlanContextManager

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
    def compute_feature_evaluation(expression: str, planContextManager: PlanContextManager) -> Optional[bool]:
        if expression is None:
            raise ValueError("expression was null. A expression must be provided to compute its evaluation.")
        
        if expression.strip() == "":
            return False

        try:
            evaluator = SimpleEval()
            evaluator.names = {
                "userContext": planContextManager.get_user_context(),
                "planContext": planContextManager.get_plan_context(),
                "usageLimitsContext": planContextManager.get_usage_limits_context()
            }
            result = evaluator.eval(expression)
            return result if isinstance(result, bool) else None
        
        except Exception:
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
