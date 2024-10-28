#!/usr/bin/env python3
"""
Get a dataset based on specified pagination
"""


import csv
import math
from typing import List


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return (self.__dataset)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return appropriate page of the dataset
        """
        assert isinstance(page, int)
        assert page > 0
        assert isinstance(page_size, int)
        assert page_size > 0
        start, end = index_range(page, page_size)
        dataset = self.dataset()

        return (dataset[start:end])

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns dictionary for hypermedia pagination
        """
        data = self.get_page(page, page_size)
        size = len(data)
        hyper = {
                    "page_size": size,
                    "page":  page,
                    "data": data,
                    "next_page": page + 1 if page != size else None,
                    "prev_page": page - 1 if page != 1 else None,
                    "total_pages": len(self.__dataset)
                }

        return (hyper)


def index_range(page, page_size):
    """
    Returns the range of data based on pagination
    """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)
