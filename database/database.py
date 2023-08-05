# Создаем шаблон заполнения словаря с пользователями
user_dict_template: dict[str: int, str: set] = {
                            'page': 1,
                            'bookmarks': set()
                            }

# Инициализируем "Базу данных"
users_db: dict = dict()