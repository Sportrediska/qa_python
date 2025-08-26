import pytest


class TestBooksCollector:
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.add_new_book("Что делать, если ваш кот хочет вас убить")
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_add_two_identical_books(self, collector):
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.add_new_book("Гордость и предубеждение и зомби")
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize("name", ["", "12345678901234567890123456789012345678901"])
    def test_add_new_book_add_wrong_length_books(self, name, collector):
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_set_genre_to_book(self, collector_with_book_scream):
        collector_with_book_scream.set_book_genre("Крик", "Ужасы")
        assert collector_with_book_scream.get_book_genre("Крик") == "Ужасы"

    def test_set_book_genre_set_genre_to_not_existing_book(self, collector):
        collector.set_book_genre("Крик", "Ужасы")
        assert collector.get_book_genre("Крик") is None

    def test_set_book_genre_set_not_existing_genre_to_book(
        self, collector_with_book_scream
    ):
        collector_with_book_scream.set_book_genre("Крик", "Аниме")
        assert collector_with_book_scream.get_book_genre("Крик") == ""

    def test_get_books_with_specific_genre_get_specific_books(
        self, collector_with_book_scream
    ):
        collector_with_book_scream.set_book_genre("Крик", "Ужасы")
        assert (
            len(collector_with_book_scream.get_books_with_specific_genre("Ужасы")) == 1
        )

    def test_get_books_with_specific_genre_get_specific_books_another_genre(
        self, collector_with_book_scream
    ):
        collector_with_book_scream.set_book_genre("Крик", "Комедии")
        assert collector_with_book_scream.get_books_with_specific_genre("Ужасы") == []

    def test_get_books_with_specific_genre_get_specific_books_wrong_genre(
        self, collector_with_book_scream
    ):
        collector_with_book_scream.set_book_genre("Крик", "Ужасы")
        assert collector_with_book_scream.get_books_with_specific_genre("Аниме") == []

    def test_get_books_with_specific_genre_get_specific_books_empty_books(
        self, collector
    ):
        assert collector.get_books_with_specific_genre("Ужасы") == []

    def test_get_books_for_children_add_children_book(self, collector):
        collector.add_new_book("Маша и Медведь")
        collector.set_book_genre("Маша и Медведь", "Мультфильмы")
        assert "Маша и Медведь" in collector.get_books_for_children()

    def test_get_books_for_children_add_not_children_book(
        self, collector_with_book_scream
    ):
        collector_with_book_scream.set_book_genre("Крик", "Ужасы")
        assert "Ужасы" not in collector_with_book_scream.get_books_for_children()

    def test_add_book_in_favorites_add_favorite_book(self, collector_with_book_scream):
        collector_with_book_scream.add_book_in_favorites("Крик")
        assert "Крик" in collector_with_book_scream.get_list_of_favorites_books()

    def test_add_book_in_favorites_add_identical_favorite_books(
        self, collector_with_book_scream
    ):
        collector_with_book_scream.add_book_in_favorites("Крик")
        collector_with_book_scream.add_book_in_favorites("Крик")
        assert len(collector_with_book_scream.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_add_favorite_book_not_exists(self, collector):
        collector.add_book_in_favorites("Крик")
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_delete_favorite_book(
        self, collector_with_book_scream
    ):
        collector_with_book_scream.add_book_in_favorites("Крик")
        collector_with_book_scream.delete_book_from_favorites("Крик")
        assert "Крик" not in collector_with_book_scream.get_list_of_favorites_books()

    def test_delete_book_from_favorites_delete_not_exists_favorite_book(
        self, collector_with_book_scream
    ):
        collector_with_book_scream.add_book_in_favorites("Крик")
        collector_with_book_scream.delete_book_from_favorites("Капитошка")
        assert len(collector_with_book_scream.get_list_of_favorites_books()) == 1

    def test_get_books_genre_all_books_genre(self, collector_with_book_scream):
        collector_with_book_scream.set_book_genre("Крик", "Ужасы")
        assert len(collector_with_book_scream.get_books_genre()) == 1

    def test_get_book_genre_get_book_by_name(self, collector_with_book_scream):
        collector_with_book_scream.set_book_genre("Крик", "Ужасы")
        assert collector_with_book_scream.get_book_genre("Крик") == "Ужасы"
