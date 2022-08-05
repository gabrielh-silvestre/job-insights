from src.sorting import sort_by


JOBS_WITH_SALARY = [
    {"max_salary": 25000, "min_salary": 2500, "date_posted": "2022-06-29"},
    {"max_salary": -1000, "min_salary": 1000, "date_posted": "2022-06-27"},
    {"max_salary": 30000, "min_salary": 2000, "date_posted": "2022-06-28"},
    {"max_salary": 10, "min_salary": 0, "date_posted": "2022-06-26"},
    {"max_salary": 20000, "min_salary": 1100, "date_posted": "2022-06-30"},
    {"max_salary": 10000, "min_salary": 1000, "date_posted": "2022-07-01"},
]


CRITERIAS = ["min_salary", "max_salary", "date_posted"]


def test_sort_by_criteria():
    for criteria in CRITERIAS:
        sort_by(JOBS_WITH_SALARY, criteria)
        if criteria == "min_salary":
            first_compare = (
                JOBS_WITH_SALARY[0][criteria] <= JOBS_WITH_SALARY[1][criteria]
            )
            second_compare = (
                JOBS_WITH_SALARY[1][criteria] <= JOBS_WITH_SALARY[2][criteria]
            )
            third_compare = (
                JOBS_WITH_SALARY[2][criteria] <= JOBS_WITH_SALARY[3][criteria]
            )

            assert first_compare
            assert second_compare
            assert third_compare
        else:
            first_compare = (
                JOBS_WITH_SALARY[0][criteria] >= JOBS_WITH_SALARY[1][criteria]
            )
            second_compare = (
                JOBS_WITH_SALARY[1][criteria] >= JOBS_WITH_SALARY[2][criteria]
            )
            third_compare = (
                JOBS_WITH_SALARY[2][criteria] >= JOBS_WITH_SALARY[3][criteria]
            )

            assert first_compare
            assert second_compare
            assert third_compare
