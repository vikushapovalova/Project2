import random
from config import locations, actions, when, events, universal_actions
from exceptions import InvalidGenreError, InvalidNameError, InvalidActionChoiceError, InvalidInputError
from colorama import Fore, Style
import pyfiglet


class StoryGenerator:
    """
    Класс для генерации случайных историй на основе имени героя и выбранного жанра.
    """

    def __init__(self, name, genre):
        """
        Конструктор для инициализации имени героя и жанра.

        :param name: Имя героя, должно быть строкой и содержать только буквы.
        :param genre: Жанр, должен быть одним из доступных жанров.
        """
        self.name = self._validate_name(name)
        self.genre = self._validate_genre(genre)
        self.story = ""

    def _validate_name(self, name):
        """
        Валидация имени героя. Имя должно быть строкой и содержать только буквы.

        :param name: Имя героя
        :return: Имя, если оно валидно
        :raises InvalidNameError: Если имя невалидно
        """
        if not name.isalpha():
            raise InvalidNameError("Имя героя должно содержать только буквы.")
        return name.strip()

    def _validate_genre(self, genre):
        """
        Валидация жанра. Жанр должен быть одним из доступных.

        :param genre: Жанр
        :return: Жанр, если он валиден
        :raises InvalidGenreError: Если жанр невалиден
        """
        valid_genres = ["фэнтези", "детектив", "хоррор", "приключения", "фантастика"]
        if genre not in valid_genres:
            raise InvalidGenreError("Неверный жанр. Пожалуйста, выберите из доступных вариантов.")
        return genre

    def generate_story(self):
        """
        Генерация начальной истории для героя в зависимости от выбранного жанра.

        :return: Сгенерированная история
        """
        when_choice = random.choice(when)
        location_choice = random.choice(locations[self.genre])
        action_choice = random.choice(actions)
        event_choice = random.choice(events[self.genre])

        self.story = f"{when_choice}, {self.name} {action_choice} {location_choice}, {event_choice}"
        return self.story

    def continue_story(self):
        """
        Генерация продолжения истории для выбранного жанра.

        :return: Продолжение истории
        """
        event_choice = random.choice(events[self.genre])
        self.story += " " + event_choice
        return event_choice

    def change_story(self):
        """
        Генерация альтернативного хода истории для изменения пути.

        :return: Новый ход в истории
        """
        new_path = random.choice(universal_actions)
        self.story += " " + new_path
        return new_path


# Основной интерфейс
def main():
    """
    Основной интерфейс программы, который позволяет выбрать жанр, ввести имя героя и
    генерировать уникальную историю.
    """
    # Генерация ASCII баннера с помощью pyfiglet
    ascii_banner = pyfiglet.figlet_format("Генератор Историй!")
    print(Fore.CYAN + ascii_banner + Style.RESET_ALL)

    # Приветственное сообщение с использованием colorama для раскраски
    print(Fore.MAGENTA + "Добро пожаловать в Генератор Историй!" + Style.RESET_ALL)

    # Даем пользователю выбор жанра
    print("Выберите жанр:")
    genres = ["фэнтези", "детектив", "хоррор", "приключения", "фантастика"]
    for idx, genre in enumerate(genres, start=1):
        print(f"{idx}. {genre}")

    while True:
        try:
            choice = int(input("\nВведите номер жанра: "))
            if choice not in range(1, len(genres) + 1):
                raise InvalidGenreError()
            else:
                genre = genres[choice - 1]
                break
        except ValueError:
            print("Ошибка: введите целое число.")
        except InvalidGenreError as e:
            print(e)

    print("\nГенерация истории...\n")

    # Ввод имени персонажа
    while True:
        try:
            name = input("Введите имя героя: ").strip()
            if not name:
                raise InvalidNameError()
            elif not name.isalpha():
                raise InvalidNameError()
            else:
                break
        except InvalidNameError as e:
            print(e)

    # Создание экземпляра класса и генерация истории
    try:
        story_generator = StoryGenerator(name, genre)
        story = story_generator.generate_story()
        print(f"\nВот начало вашей истории:\n{story}")

        # Даем пользователю возможность изменить ход истории
        while True:
            try:
                choice = int(input("\nХотите продолжить историю (1) или изменить ход (2)?\n"))
                if choice == 1:  # Продолжить историю
                    continuation = story_generator.continue_story()
                    print(f"\nПродолжение истории:\n{story_generator.story}")
                    break
                elif choice == 2:  # Изменить ход истории
                    new_path = story_generator.change_story()
                    print(f"\nНовый ход в истории:\n{story_generator.story}")
                    break
                else:
                    raise InvalidActionChoiceError()
            except ValueError:
                print("Ошибка: введите целое число.")
            except InvalidActionChoiceError as e:
                print(e)

        print(Fore.GREEN + "Спасибо за использование Генератора Историй!" + Style.RESET_ALL)

    except Exception as e:
        print(f"Произошла ошибка при генерации истории: {e}")


if __name__ == "__main__":
    main()
