class InvalidGenreError(Exception):
    def __init__(self, message="Неверный жанр. Пожалуйста, выберите из доступных вариантов."):
        self.message = message
        super().__init__(self.message)

class InvalidNameError(Exception):
    def __init__(self, message="Имя героя должно содержать только буквы и не быть пустым."):
        self.message = message
        super().__init__(self.message)

class InvalidActionChoiceError(Exception):
    def __init__(self, message="Неверный выбор. Пожалуйста, выберите действие (1 или 2)."):
        self.message = message
        super().__init__(self.message)

class InvalidInputError(Exception):
    def __init__(self, message="Ошибка ввода. Пожалуйста, введите корректное значение."):
        self.message = message
        super().__init__(self.message)

class StoryGenerationError(Exception):
    def __init__(self, message="Ошибка при генерации истории."):
        self.message = message
        super().__init__(self.message)
