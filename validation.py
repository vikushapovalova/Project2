"""
Модуль для проверки корректности пользовательских данных.
"""

def is_valid_choice(choice, valid_choices):
    """
    Проверяет, что пользователь сделал допустимый выбор.

    Args:
        choice: Выбор пользователя.
        valid_choices (list): Список допустимых значений.

    Returns:
        bool: True, если выбор корректен, иначе False.
    """
    return choice in valid_choices
