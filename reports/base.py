from abc import ABC, abstractmethod
from typing import List, Dict, Any

class BaseReport(ABC):
    @abstractmethod
    def generate(self, employees: List[Dict[str, Any]]) -> str:
        """Абстрактная генерация отчёта"""
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        """Имя отчёта (для регистрации)"""
        pass
    