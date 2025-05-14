from typing import List, Dict, Any
from formatters.registry import registry as fmt_reg
from .base import BaseReport

class PayoutReport(BaseReport):
    @property
    def name(self) -> str:
        return 'payout'
    
    def _groupByDepartment(self, employees: List[Dict[str, Any]]):
        """Группирует сотрудников по отделам"""
        departments = {}
        for emp in employees:
            dept = emp["department"]
            if dept not in departments:
                departments[dept] = []
            departments[dept].append(emp)
        return departments
    
    def _prepareData(self, employees: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Подготовка данных под форматтеры"""
        departments = self._groupByDepartment(employees)
        result = {
            "department": {},
            "total_hours": 0,
            "total_payout": 0
        }
        
        for dept, emps in departments.items():
            dept_data = {
                "employees": [],
                "total_hours": 0,
                "total_payout": 0
            }

            for emp in emps:
                hours = emp['hours_worked']
                rate = emp.get('hourly_rate', 0)
                payout = hours * rate

                dept_data["employees"].append(
                    {
                        "name": emp["name"],
                        "hours": hours,
                        "rate": rate,
                        "payout": payout
                    }
                )
                dept_data["total_hours"] += hours
                dept_data["total_payout"] += payout

            result["department"][dept]=dept_data
            result["total_hours"] += dept_data["total_hours"]
            result["total_payout"] += dept_data["total_payout"]
        return result
    
    def generate(self, employees: List[Dict[str, Any]], outputFormat: str='table') ->str:
        """Генерирует отчёт в указанном формате"""
        data = self._prepareData(employees)
        formatter = fmt_reg.get_formatter(outputFormat)
        return formatter.format(data)