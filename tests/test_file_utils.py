import pytest
from file_utils import read_employee_data, find_rate_field, parse_employee_data

def test_find_rate_field():
    headers = ["name", "hours_worked", "rate"]
    assert find_rate_field(headers) == "rate"
    
    headers = ["name", "salary", "hours"]
    assert find_rate_field(headers) == "salary"
    
    headers = ["name", "hours"]
    assert find_rate_field(headers) is None

def test_parse_employee_data(sample_csv_data):
    lines = sample_csv_data.split('\n')[1:]  # Пропускаем заголовок
    headers = sample_csv_data.split('\n')[0].split(',')
    employees = parse_employee_data(lines, headers, "hourly_rate")
    assert len(employees) == 3
    assert employees[0]["name"] == "Alice Johnson"

def test_read_employee_data(sample_csv_file):
    employees = read_employee_data(sample_csv_file)
    assert len(employees) == 3
    assert employees[0]["department"] == "Marketing"

def test_read_nonexistent_file():
    with pytest.raises(Exception):
        read_employee_data("nonexistent.csv")