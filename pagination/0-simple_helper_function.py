#!/usr/bin/env python3
"""Simple helper function for pagination"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple containing start and end index for pagination.

    Args:
        page: current page number (1-indexed)
        page_size: number of items per page

    Returns:
        Tuple of (start_index, end_index)
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
