import json
from typing import Dict, Any
from .base import BaseFormatter

"""Форматтер вывода в json"""

class JSONFormatter(BaseFormatter):
    @property
    def name(self) ->str:
        return 'json'
    
    def format(self, data: Dict[str, Any]) -> str: #перевод в json-строку
        return json.dumps(data, indent=2, ensure_ascii=False) 