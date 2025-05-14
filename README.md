# CSV-report
Консольное приложение для генерации отчётов по заработной плате сотрудников на основе данных из CSV-файлов. Поддерживаются различные форматы вывода отчётов.
Были учтены все требования тех.задания, а именно: 
В скрипт можно передать несколько файлов
В скрипт можно передать тип отчёта
Название отчёта передается через параметр --report
Заложена возможность добавления новых отчётов
Предусмотрено, что название колонки hourly_rate может быть разным: hourly_rate, rate, salary, а порядок колонок не гарантируется
Можно передать пути к файлам, название отчёта, сформировать отчёт Payout
Не используется стандартная библиотека csv, не используется pandas, не используется click
Выходные форматы json и table, обеспечена возможность лёгкого добавления новых форматов
Покрытие тестами

Для добавления нового отчёта нужно создать новый файл в папке reports, например, average_rate.py, а затем прописать в нём дочерний класс для BaseReport, например:
from .base import (BaseReport)
class AverageRate(BaseReport):
  @property #обязательное свойство, описанное в абстрактном классе
  def name(self) -> str:
    return 'average_rate'
  def generate(self, employees: List[Dict[str, Any]]) -> str: #объявление этого метода обязательно, так как он описан в абстрактном классе. 
    #логика метода

После этого регистрируем класс в reports/registry.py
from .average_rate.py import AverageRate
...
registry.register(AverageRate)

После этого его можно вызвать через --average_rate

Добавление нового формата - похожая процедура:
Создаём файл, допустим, to_csv.py в папке formatters,
import csv
from .base import BaseFormatter
class CSVFormatter(BaseFormatter):
  @property
  def name(self) -> str:
    return "to_csv"
И регистрируем его в formatters/registry.py
from .to_csv import CSVFormatter
...
registry.register(CSVFormatter)
Вызов через --to_csv


Для запуска проекта
1. Необходимо клонировать репозиторий 
git-clone <https://github.com/TFF24/CSV-report>
и перейти в папку payout.
В папке есть requirements.txt (зависимости, нужны для тестов)

Формирование отчёта происходит по команде:
python main.py filename(s).csv --report payout --format json (или table)
Для просмотра доступных отчётов и форматов:
python main.py --help
