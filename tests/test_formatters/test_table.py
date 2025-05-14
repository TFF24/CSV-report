from formatters.table import TableFormatter

def testTableFormatter(sample_report_data):
    formatter = TableFormatter()
    result = formatter.format(sample_report_data)
    assert 'Alice' in result
    assert 'Marketing' in result
    assert '$ 8000' in result

def testTableFormatter_name():
    assert TableFormatter().name == 'table'