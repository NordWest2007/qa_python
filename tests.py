from main import BooksCollector
import pytest

class TestBooksCollector:

    #Фикстура создает тестовый набор книг с указанием жанра
    @pytest.fixture()
    def create_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre("Гордость и предубеждение и зомби", "Ужасы")
        collector.add_new_book('Пила')
        collector.set_book_genre("Пила", "Ужасы")

        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre("Что делать, если ваш кот хочет вас убить", "Детективы")

        collector.add_new_book("Покемоны")
        collector.set_book_genre("Покемоны", "Мультфильмы")

        collector.add_new_book("Головоломка")
        collector.set_book_genre("Головоломка", "Мультфильмы")

        collector.add_new_book("Назад в будущее")
        collector.set_book_genre("Назад в будущее", "Фантастика")

        collector.add_new_book("Ширли - мырли")
        collector.set_book_genre("Ширли - мырли", "Комедии")
        return collector

    @pytest.mark.parametrize("book_name,book_genre", [["Гордость и предубеждение и зомби", "Ужасы"],
                                                      ["Что делать, если ваш кот хочет вас убить", "Детективы"],
                                                      ["Покемоны", "Мультфильмы"],
                                                      ["Назад в будущее", "Фантастика"],
                                                      ["Ширли - мырли", "Комедии"]])
    def test_set_book_genre_successful_all_possible_genres(self, book_name, book_genre):
        # параметризованный тест, создает книги со всеми доступными жанрами
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        assert collector.get_book_genre(book_name) == book_genre

    def test_add_new_book_book_duplication(self):
        #тест проверяет, что дубли не добавляются в каталог
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_with_name_more_than41_symbol(self):
        #тест проверяет, что не  добавляется книга в назвниии которой  больше 41 символа
        collector = BooksCollector()
        collector.add_new_book('Название книги содержит в себе больше допустимого количества символов')
        assert len(collector.get_books_genre()) == 0

    def test_get_books_genre_contains_all_given_lines(self, create_books):
        #тест проверяет, что каталог содержит все добавленные строки
        assert len(create_books.get_books_genre()) == 7

    @pytest.mark.parametrize("book_genre,count_books",
                             [['Фантастика', 1], ['Ужасы', 2], ['Детективы', 1],
                              ['Мультфильмы', 2], ['Комедии', 1]])
    def test_get_books_with_specific_genre_counting_books_selected_genre(self, create_books, book_genre, count_books):
        #параметризованный тест для подсчета книг выбранного жанра,
        #тестовый набор книг из фикстуры create_books
        assert len(create_books.get_books_with_specific_genre(book_genre)) == count_books

    def test_get_books_for_children_returns_correct_books_set(self, create_books):
        # тест проверяет, что возвращается правильный набор книг
        list_for_children = ['Покемоны', 'Головоломка', 'Назад в будущее', 'Ширли - мырли']
        assert create_books.get_books_for_children() == list_for_children

    def test_add_book_in_favorites_two_books(self, create_books):
        #тест проверяет добавление двух книг в избранное
        create_books.add_book_in_favorites('Головоломка')
        create_books.add_book_in_favorites('Ширли - мырли')
        assert len(create_books.get_list_of_favorites_books()) == 2

    def test_add_book_in_favorite_book_duplication(self, create_books):
        #тест проверяет, что дубли не добавляются в избранное
        create_books.add_book_in_favorites('Головоломка')
        create_books.add_book_in_favorites('Головоломка')
        assert len(create_books.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_removal_from_favorites_successful(self, create_books):
        #тест проверяет, что удаление из избранного происходит
        create_books.add_book_in_favorites('Головоломка')
        create_books.add_book_in_favorites('Ширли - мырли')
        create_books.delete_book_from_favorites('Ширли - мырли')
        assert len(create_books.get_list_of_favorites_books()) == 1 and (
                create_books.get_list_of_favorites_books() == ['Головоломка'])

    def test_add_new_book_double_add_genre_for_unknown_name(self):
        # тест проверяет, добавление жанра для книги, которая не была добавлена в каталог
        collector = BooksCollector()
        collector.set_book_genre("Неизвестная книга", "Ужасы")
        assert collector.get_book_genre('Неизвестная книга') is None

    def test_set_book_genre_unknown_genre(self):
        # тест проверяет, установку неизвестного жанра для книги не происходит
        collector = BooksCollector()
        collector.add_new_book('Призраки')
        collector.set_book_genre("Призраки", "НаучПоп")
        assert collector.get_book_genre('Призраки') == ''
