import os

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050
book: dict[int, str] = dict()


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text, start, page_size):
    page = text[start: start + page_size]
    reversed_page = page[::-1]
    punctuation = ['.', ',', '!', '?', ';', ':']
    page_size = len(page)
    for i in range(len(reversed_page)):
        if reversed_page[i] in punctuation:
            if reversed_page[i + 1] not in punctuation and reversed_page[i - 1] not in punctuation:
                ready_text = reversed_page[i:][::-1]
                len_ready_text = len(ready_text)
                return (ready_text, len_ready_text)
            

# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as file_with_book:
        content = file_with_book.read()
    start, page_number = 0, 1
    while start < len(content):
        text_page, len_page = _get_part_text(content, start, PAGE_SIZE)
        book[page_number] = text_page.strip()
        start += len_page
        page_number += 1 


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(os.getcwd(), BOOK_PATH))

