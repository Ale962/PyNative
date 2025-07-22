def remove_char(text, n) -> str|None:
    if n < (len(text) -1):
        new_text = text[n:]
        return new_text
    else:
        raise IndexError('The value n specified is out of range of the index')