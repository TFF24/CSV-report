import argparse
import sys
from typing import List, Dict, Any
from file_utils import readEmployeeData
from exceptions import *
from reports.registry import registry as rep_reg
from formatters.registry import registry as fmt_reg



def parseArgs() -> argparse.Namespace:
    """Аргументы командной строки"""
    parser = argparse.ArgumentParser(
        description="Генерация отчётов по данным сотрудников",
        epilog="Например: python main.py data1.csv data2.csv --report payout --format json"
    )
    parser.add_argument(
        "files",
        nargs="+",
        help="Пути к csv файлам"
    )
    parser.add_argument(
        "--report",
        required=True,
        help=f"Тип отчёта (доступные {', '.join(rep_reg.get_avaliable_reports())})"
    )
    parser.add_argument(
        "--format",
        default='table',
        help=f"Форматировани отчёта (доступные {', '.join(fmt_reg.get_avaliable_formats())})"
        )
    return parser.parse_args()

def loadEmployees(file_paths: List[str]) -> List[Dict[str, Any]]:
    """Загрузка данных сотрудников из файла(-ов)"""
    employees = []
    for file_path in file_paths:
        try:
            employees.extend(readEmployeeData(file_path))
        except InvalidInputError as e:
            print(f"Ошибка: {str(e)}", file=sys.stderr)
    return employees

def main():
    try:
        args = parseArgs()
        employees = loadEmployees(args.files)

        if not employees:
            print("Нет данных для формирования отчёта", file=sys.stderr)
            return
        report = rep_reg.get_report(args.report)
        result = report.generate(employees, args.format)
        print(result)

    except ReportNotFoundError as e:
        print(f"Ошибка: {str(e)}", file=sys.stderr)
        if "Формат" in str(e):
            print(f"Доступные форматы: {', '.join(fmt_reg.get_avaliable_formats())}", file=sys.stderr)
        else:
            print(f"Доступные отчёты: {', '.join(rep_reg.get_avaliable_reports())}", file=sys.stderr)
        sys.exit(5)
    
    # except Exception as e:
    #     print(f"Непредвиденная ошибка: {str(e)}", file=sys.stderr)
    #     sys.exit(2)
if __name__ == "__main__":
    main()