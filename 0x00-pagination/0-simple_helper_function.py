#!/usr/bin/env python3
"""Simple helper function module"""
from typing import Tuple


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
