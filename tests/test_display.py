from word_guessing.display import hangman, lives_bar, word_render, line


def test_hangman_stage_0() -> None:
    assert hangman(0) == ""


def test_hangman_stage_1() -> None:
    result = hangman(1)
    assert "(｡)" in result
    assert "|" not in result


def test_hangman_full() -> None:
    result = hangman(5)
    assert "(｡)" in result
    assert "/" in result
    assert "\\" in result


def test_hangman_clamps_above_max() -> None:
    assert hangman(99) == hangman(5)


def test_lives_bar_full() -> None:
    bar = lives_bar(5)
    assert bar.count("♥") == 5


def test_lives_bar_empty() -> None:
    bar = lives_bar(0)
    # Gray hearts remain as placeholder — only count red ones
    assert bar.count("\033[91m") == 0
    assert bar.count("\033[90m") == 5


def test_word_render_all_hidden() -> None:
    result = word_render("cat", [])
    assert "_" in result
    assert "c" not in result


def test_word_render_partial() -> None:
    result = word_render("cat", ["a"])
    assert "a" in result


def test_word_render_full() -> None:
    result = word_render("cat", ["c", "a", "t"])
    assert "_" not in result


def test_line_format() -> None:
    top = line(True)
    assert "┌" in top
    assert "┐" in top
    bottom = line(False)
    assert "└" in bottom
    assert "┘" in bottom
