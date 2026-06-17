from word_guessing.words import get_categories, get_random_word


def test_get_categories_returns_list() -> None:
    cats = get_categories()
    assert isinstance(cats, list)
    assert len(cats) > 0
    assert "mixed" in cats


def test_get_random_word_no_category() -> None:
    word = get_random_word()
    assert isinstance(word, str)
    assert len(word) > 0
    assert word.isalpha()


def test_get_random_word_with_category() -> None:
    word = get_random_word("animals")
    from word_guessing.words import WORDS_BY_CATEGORY
    assert word in WORDS_BY_CATEGORY["animals"]


def test_get_random_word_invalid_category_falls_back() -> None:
    word = get_random_word("nonexistent")
    assert isinstance(word, str)
    assert len(word) > 0
