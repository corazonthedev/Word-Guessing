import random
from typing import Sequence

WORDS_BY_CATEGORY: dict[str, list[str]] = {
    "animals": [
        "elephant", "giraffe", "dolphin", "penguin", "cheetah",
        "octopus", "kangaroo", "flamingo", "chameleon", "jaguar",
    ],
    "food": [
        "pizza", "spaghetti", "chocolate", "sandwich", "omelette",
        "lasagna", "avocado", "broccoli", "margarita", "pancake",
    ],
    "nature": [
        "rainbow", "volcano", "waterfall", "thunder", "mountain",
        "sunflower", "constellation", "lagoon", "tornado", "glacier",
    ],
    "tech": [
        "algorithm", "keyboard", "monitor", "software", "circuit",
        "database", "python", "javascript", "encryption", "binary",
    ],
    "mixed": [
        "dog", "cat", "car", "sea", "beach", "horse",
        "umbrella", "balloon", "guitar", "puzzle",
    ],
}


def get_categories() -> list[str]:
    return list(WORDS_BY_CATEGORY.keys())


def get_random_word(category: str | None = None) -> str:
    if category and category in WORDS_BY_CATEGORY:
        return random.choice(WORDS_BY_CATEGORY[category])
    all_words: list[str] = []
    for word_list in WORDS_BY_CATEGORY.values():
        all_words.extend(word_list)
    return random.choice(all_words)


def words_in_category(category: str) -> Sequence[str]:
    return WORDS_BY_CATEGORY.get(category, [])
