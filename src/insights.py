from typing import Dict, List, Union
from src.jobs import read


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """

    all_jobs = read(path)
    job_types = [job["job_type"] for job in all_jobs]

    return list(set(job_types))


def filter_by_job_type(
    jobs: List[Dict[str, str]], job_type: str
) -> List[Dict[str, str]]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    filtered_jobs = [
        job
        for job in jobs
        if job["job_type"].lower() == job_type.lower()
        ]

    return filtered_jobs


def get_unique_industries(path: str) -> List[str]:
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """

    all_jobs = read(path)
    industry = [
        job["industry"]
        for job in all_jobs
        if job["industry"] != ""
        ]

    return list(set(industry))


def filter_by_industry(
    jobs: List[Dict[str, str]], industry: str
) -> List[Dict[str, str]]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    filtered_jobs = [
        job
        for job in jobs
        if job["industry"].lower() == industry.lower()
        ]

    return filtered_jobs


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """

    # Checagem se a string pode ser convertida para int
    # https://stackoverflow.com/questions/5606585/python-test-if-value-can-be-converted-to-an-int-in-a-list-comprehension

    all_jobs = read(path)
    salaries = [
        int(job["max_salary"])
        for job in all_jobs
        if job["max_salary"].isdigit()
        ]

    return max(salaries)


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    all_jobs = read(path)
    salaries = [
        int(job["min_salary"])
        for job in all_jobs
        if job["min_salary"].isdigit()
        ]

    return min(salaries)


def matches_salary_range(
    job: Dict[str, Union[str, int]], salary: Union[str, int]
) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """

    max_salary = job.get("max_salary", None)
    min_salary = job.get("min_salary", None)

    if type(max_salary) != int or type(min_salary) != int:
        raise ValueError()
    elif max_salary < min_salary:
        raise ValueError()
    elif type(salary) != int:
        raise ValueError()

    is_on_range = max_salary >= salary >= min_salary

    return is_on_range


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
