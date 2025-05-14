from typing import Dict, Type, List
from .base import BaseFormatter
from exceptions import ReportNotFoundError
from .json import JSONFormatter
from .table import TableFormatter

class FormatterRegistry:
    """Реестр всех доступных форматтеров вывода"""

    def __init__(self):
        self._formatters: Dict[str, Type[BaseFormatter]] = {}

    def register(self, formatter_class: Type[BaseFormatter]):
        self._formatters[formatter_class().name] = formatter_class

    def get_formatter(self, format_name: str) -> BaseFormatter:
        if format_name not in self._formatters:
            raise ReportNotFoundError(f"Формат '{format_name}' не поддерживается")
        return self._formatters[format_name]()
    
    def get_avaliable_formats(self) -> List[str]:
        return list(self._formatters.keys())
    
registry = FormatterRegistry()
registry.register(JSONFormatter)
registry.register(TableFormatter)