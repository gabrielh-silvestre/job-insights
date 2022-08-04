from unittest import mock
from unittest.mock import patch
import pytest
from src.brazilian_jobs import read_brazilian_file


@pytest.fixture
def brazilian_jobs():
    return [
        {"titulo": "Maquinista", "salario": "2000", "tipo": "trainee"},
        {"titulo": "Motorista", "salario": "3000", "tipo": "full time"},
        {
            "titulo": "Analista de Software",
            "salario": "4000",
            "tipo": "full time",
        },
        {
            "titulo": "Assistente administrativo",
            "salario": "1700",
            "tipo": "full time",
        },
    ]


def test_brazilian_jobs(brazilian_jobs):
    with patch("src.jobs.read", mock.Mock(return_value=brazilian_jobs)):
        translated_jobs = read_brazilian_file("src/jobs.csv")
        first_job = translated_jobs[0]

        assert first_job.keys() == {"title", "salary", "type"}
        assert first_job["title"] == "Maquinista"
        assert first_job["salary"] == "2000"
        assert first_job["type"] == "trainee"
