def repetiont(text: str, word: str) -> int:
    counter = 0
    words_in_text: list[str] = text.split()
    for w in words_in_text:
        if w == word:
            counter += 1

    return counter