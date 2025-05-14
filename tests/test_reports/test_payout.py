from reports.payout import PayoutReport

def testPayoutReport(sample_employees):
    report = PayoutReport()
    result = report.generate(sample_employees, 'table')
    assert 'Alice Johnson' in result
    assert 'Bob Smith' in result

def testPayoutReport_name():
    assert PayoutReport().name == 'payout'
