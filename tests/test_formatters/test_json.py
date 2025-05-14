from formatters.json import JSONFormatter

def testJSONFormatter(sample_report_data):
    formatter = JSONFormatter()
    result = formatter.format(sample_report_data)
    assert '"Marketing"' in result
    assert '"total_payout: 8000"' in result

def testJSONFormatter_name():
    assert JSONFormatter().name == 'json'
