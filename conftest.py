import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()


@pytest.fixture
def collector_with_book_scream():
    collector = BooksCollector()
    collector.add_new_book("Крик")
    return collector
