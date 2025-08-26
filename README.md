# qa_python


Автотесты для BooksCollector:

# Тесты добавления книг
test_add_new_book_add_two_books - Добавление двух разных книг в коллекцию
test_add_new_book_add_two_identical_books - Попытка добавления дубликатов книг
test_add_new_book_add_wrong_length_books - Добавление книг с невалидной длиной названия

# Тесты работы с жанрами
test_set_book_genre_set_genre_to_book - Установка жанра для существующей книги
test_set_book_genre_set_genre_to_not_existing_book - Установка жанра для несуществующей книги
test_set_book_genre_set_not_existing_genre_to_book - Установка несуществующего жанра

# Тесты поиска по жанрам
test_get_books_with_specific_genre_get_specific_books - Поиск книг по конкретному жанру
test_get_books_with_specific_genre_get_specific_books_another_genre - Поиск по жанру, которого нет в коллекции
test_get_books_with_specific_genre_get_specific_books_wrong_genre - Поиск по несуществующему жанру
test_get_books_with_specific_genre_get_specific_books_empty_books - Поиск в пустой коллекции

# Тесты детских книг
test_get_books_for_children_add_children_book - Добавление детской книги
test_get_books_for_children_add_not_children_book - Добавление недетской книги

# Тесты избранного
test_add_book_in_favorites_add_favorite_book - Добавление книги в избранное
test_add_book_in_favorites_add_identical_favorite_books - Добавление дубликата в избранное
test_add_book_in_favorites_add_favorite_book_not_exists - Добавление несуществующей книги в избранное
test_delete_book_from_favorites_delete_favorite_book - Удаление книги из избранного
test_delete_book_from_favorites_delete_not_exists_favorite_book - Удаление несуществующей книги из избранного

# Фикстуры
collector - Чистый экземпляр BooksCollector
collector_with_book_scream - Коллектор с добавленной книгой "Крик"