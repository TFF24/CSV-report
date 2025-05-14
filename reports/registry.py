from typing import Dict, Type, List
from .base import BaseReport
from exceptions import ReportNotFoundError
from .payout import PayoutReport

class ReportRegistry:
    def __init__(self):
        self._reports: Dict[str, Type[BaseReport]] = {}

    def register(self, report_class: Type[BaseReport]):
        """Регистрация нового отчёта"""
        self._reports[report_class().name] = report_class

    def get_report(self, report_name: str) -> BaseReport:
        """Получение экземпляра отчёта"""
        if report_name not in self._reports:
            raise ReportNotFoundError(f"Отчёт '{report_name}' не найден.")
        return self._reports[report_name]()
    
    def get_avaliable_reports(self)-> List[str]:
        return list(self._reports.keys())
    
registry = ReportRegistry()
registry.register(PayoutReport)