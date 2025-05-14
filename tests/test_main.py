import pytest
from main import parseArgs, loadEmployees, main
from unittest.mock import patch, MagicMock

def testParseArgs():
    with patch('sys.argv', ['main.py', 'data.csv', '--report', 'payout']):
        args = parseArgs()
        assert args.report == 'payout'

@patch('main.readEmployeeData')
def testLoadEmployees(mock_read):
    mock_read.return_value = [{'name': 'Test'}]
    employees = loadEmployees(['test.csv'])
    assert len(employees) == 1
    assert employees[0]['name'] == 'Test'

@patch('main.rep_reg.get_report')
@patch('main.loadEmployees')
def test_main_success(mock_load, mock_get):
    mock_load.return_value = [{"name": "Test"}]
    mock_report = MagicMock()
    mock_report.generate.return_value = "test output"
    mock_get.return_value = mock_report
    
    with patch('sys.argv', ['main.py', 'data.csv', '--report', 'payout']):
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_with("test output")