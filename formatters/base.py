from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseFormatter(ABC):
    """Базовый класс для всех форматтеров вывода"""
    @abstractmethod
    def format(self, data: Dict[str, Any]) -> str:
        pass #форматирование данных в нужный формат

    @property
    @abstractmethod
    def name(self) -> str:
        pass #имя форматтера для регистрации