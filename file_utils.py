from typing import Dict, List, Any, Optional
from pathlib import Path
from exceptions import InvalidInputError

def readEmployeeData(filePath: str) -> List[Dict[str, Any]]:
    """Чтение из csv-файла с обработкой ошибок, таких как отсутствие файла, отсутствие обязательных полей в csv, ошибка чтения"""
    try:
        path = Path(filePath)
        if not path.exists():
            raise InvalidInputError(f"Не найден файл {filePath}")
        
        with path.open('r') as fp:
            lines = [line.strip() for line in fp if line.strip()]

        if len(lines)<2:
            return []
        
        headers = [h.strip() for h in lines[0].split(',')]
        requiredFields = {'name', 'department', 'hours_worked'} 
        if not requiredFields.issubset(headers):
            raise InvalidInputError(f"В файле нет обязательных полей: {filePath}")
        
        rateFields = findRateFields(headers)
        employees = parseEmployeeData(lines[1:], headers, rateFields)
        return employees
    except Exception as e:
        raise InvalidInputError(f"Ошибка чтения файла {filePath}: {str(e)}")
    
def findRateFields(headers: List[str]) -> Optional[str]:
    """Поиск поля с З/П в час. Как известно из условий, название поля и его очерёдность может быть разной"""

    for field in ['hourly_rate', 'salary', 'rate']:
        if field in headers:
            return field
    return None

def parseEmployeeData(lines: List[str], headers: List[str], rateField: Optional[str]) -> List[Dict[str, Any]]:
    """Парсинг данных сотрудников, откидывание строк, где количество значений не совпадает с количеством заголовков"""
    
    employees = []
    for line in lines:
        values = [v.strip() for v in line.split(',')]
        if len(values) != len(headers):
            continue

        employee= dict(zip(headers, values))
        try:
            employee['hours_worked'] = int(employee['hours_worked'])
            if rateField:
                employee['hourly_rate'] = float(employee[rateField])
            employees.append(employee)
        except (ValueError, KeyError):
            continue
    return employees