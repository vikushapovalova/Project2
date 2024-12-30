import random
from story_gen.config import locations, actions, when, events, universal_actions

def generate_story(genre, name):
    """
    Генерация базовой истории для одного персонажа в зависимости от жанра и имени.
    """
    # Начальная часть истории
    when_choice = random.choice(when)
    character_choice = name
    location_choice = random.choice(locations[genre])
    action_choice = random.choice(actions)
    event_choice = random.choice(events[genre])

    return f"{when_choice}, {character_choice} {action_choice} {location_choice}, {event_choice}"

def generate_alternative_story():
    """
    Генерация альтернативного хода истории, который можно использовать для изменения пути.
    """
    return random.choice(universal_actions)

def continue_event_choice(genre):
    """
    Генерация продолжения истории для указанного жанра.
    """
    return random.choice(events[genre])
