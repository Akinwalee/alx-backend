#!/usr/bin/env python3
"""
Pagination helper fucntion
"""


def index_range(page, page_size):
    """
    Calculates and returns the start and end indices
    corresponding to the range of index
    """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)
