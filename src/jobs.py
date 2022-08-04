import csv
from functools import lru_cache
from typing import Dict, List


@lru_cache
def read(path: str) -> List[Dict[str, str]]:
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """

    with open(path) as csv_file:
        return [row for row in csv.DictReader(csv_file)]
