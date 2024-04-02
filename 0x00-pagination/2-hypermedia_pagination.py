#!/usr/bin/env python3
"""Simple helper function module"""
from typing import Tuple, List, Dict
import csv
import math


def index_range(page: int, page_size: int) -> Tuple:
    """Return a tuple of size two containing a start index and an end index
       corresponding to the range of indexes to return in a list
       for those particular pagination parameters @page and @page_size

       Args:
         page: int
         page_size: int

       Returns:
         a tuple of size two containing a start index and an end index
    """
    return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Reurn the contents page requested"""
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0

        # Get the start and end index
        start, end = index_range(page, page_size)

        # Load dataset
        self.dataset()

        # Return page contents
        return self.__dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Returns a dictionary containing informations about @page"""
        page_data = self.get_page(page, page_size)
        dataset_size = len(self.__dataset)

        d_size_per_page = dataset_size // page_size
        remainder = dataset_size % page_size
        total_pages = d_size_per_page + 1 if remainder else d_size_per_page

        full_data = {
          'page_size': page_size,
          'page': page,
          'date': page_data,
          'next_page': page + 1 if page_size * page < dataset_size else None,
          'prev_page': page - 1 if page > 1 else None,
          'totale_pages': total_pages
        }

        return full_data
