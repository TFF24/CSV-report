"""Вместо того, чтобы обрабатывать одно и то же исключение кучу раз в коде, легче вытащить его в отдельный файл и объявлять где угодно."""
class InvalidInputError(Exception):
    pass #некорректные входные данные

class ReportNotFoundError(Exception):
    pass #такой отчёт не существует