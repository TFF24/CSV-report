from typing import List, Dict, Any
from .base import BaseFormatter

"""Форматтер для вывода в таблицу"""

class TableFormatter(BaseFormatter):
    @property
    def name(self) -> str:
        return "table"
    
    def format(self, data:Dict[str, Any]) -> str:
        departments = data['department']
        lines = [
            "|       | name                         | hours      | rate       | payout       |",
            "|-------|------------------------------|------------|------------|--------------|"
        ]

        for dept, dept_data in sorted(departments.items()):
            lines.append(f"| {dept:<77} |")
            for emp in dept_data['employees']:
                lines.append(f"|-------| {emp['name']:<28} | {emp['hours']:>10} | {emp['rate']:>10} | {emp['payout']:>12} |")
            lines.append(f"| Total | {' '* 28} | {dept_data['total_hours']:>10} | { ' ' * 11 }| ${dept_data['total_payout']:>12}|")
        lines.append(f"| {' '*5} | {" " * 28} | {data['total_hours']:>10} | {" " * 10} | {data['total_payout']:>12} |")
        return "\n".join(lines)