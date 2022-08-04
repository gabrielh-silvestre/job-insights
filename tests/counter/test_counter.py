from unittest.mock import mock_open, patch
import pytest
from src.counter import count_ocurrences


@pytest.fixture
def jobs():
    return [
        {"title": "Front end developer", "salary": "2000", "type": "trainee"},
        {"title": "Back end developer", "salary": "3000", "type": "full time"},
        {
            "title": "Full stack end developer",
            "salary": "4000",
            "type": "full time",
        },
    ]


def test_counter(jobs):
    with patch("builtins.open", mock_open(read_data=str(jobs))):
        normal_developer_count = count_ocurrences("src/jobs.csv", "developer")
        assert normal_developer_count == 3

        sensitive_developer_count = count_ocurrences(
            "src/jobs.csv", "dEvELoPER"
        )
        assert sensitive_developer_count == 3
