"""
Модуль вспомогательных функций для проверки ввода и других операций.
"""

def validate_choice(choice, max_choice):
    """
    Проверяет корректность выбора, введенного пользователем.

    Args:
        choice (int): Введенное значение.
        max_choice (int): Максимально допустимое значение.

    Returns:
        bool: True, если выбор корректен, иначе False.
    """
    return 1 <= choice <= max_choice
