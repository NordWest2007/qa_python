
# qa_python

Финальный проект 4 спринта
Unit - тестирование приложения BooksCollector.  Оно позволяет установить жанр книг и добавить их в избранное.


## Описание тестов

| Название теста             | Описание                                                                |
| ----------------- | ------------------------------------------------------------------ |
| test_set_book_genre_successful_all_possible_genres | параметризованный тест, создает книги со всеми доступными жанрами |
| test_add_new_book_book_duplication | дубли не добавляются в каталог |
| test_add_new_book_with_name_more_than41_symbol | не  добавляется книга в назвниии которой  больше 41 символа |
| test_get_books_genre_contains_all_given_lines | каталог содержит все добавленные строки |
| test_get_books_for_children_returns_correct_books_set |  возвращается правильный набор книг |
| test_add_book_in_favorites_two_books | добавление двух книг в избранное |
| test_add_book_in_favorite_book_duplication | дубли не добавляются в избранное |
| test_delete_book_from_favorites_removal_from_favorites_successful | удаление из избранного происходит |
| test_add_new_book_double_add_genre_for_unknown_name |  добавление жанра для книги, которая не была добавлена в каталог |
| test_set_book_genre_unknown_genre | установка неизвестного жанра для книги не происходит| 

## Authors

- @NordWest2007
