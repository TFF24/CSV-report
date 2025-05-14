import pytest 
import tempfile
from pathlib import Path

@pytest.fixture
def sample_csv_data():
    return """id,name,department,hours_worked,hourly_rate
1,Alice Johnson,Marketing,160,50
2,Bob Smith,Design,150,40
3,Carol Williams,Design,170,60"""

@pytest.fixture
def sample_csv_file(sample_csv_data):
    with tempfile.NamedTemporaryFile(mode='w+', suffix='.csv', delete=False) as f:
        f.write(sample_csv_data)
        f.flush()
        yield Path(f.name)
    Path(f.name).unlink()

@pytest.fixture
def sample_employees():
    return [
        {"name": "Alice Johnson", "department": "Marketing", "hours_worked": 160, "hourly_rate": 50},
        {"name": "Bob Smith", "department": "Design", "hours_worked": 150, "hourly_rate": 40}
    ]

@pytest.fixture
def sample_report_data():
    return {
        "departments": {
            "Marketing": {
                "employees": [{"name": "Alice", "hours": 160, "rate": 50, "payout": 8000}],
                "total_hours": 160,
                "total_payout": 8000
            }
        },
        "total_hours": 160,
        "total_payout": 8000
    }
