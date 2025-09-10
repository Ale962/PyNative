def remove_char(text: str, n: int) -> str|None:
    if n < (len(text) -1):
        new_text = text[n:]
        return new_text
    else:
        raise IndexError('The value n specified is out of range of the index')
    

if __name__ == '__main__':
    print(remove_char('pynative', 4))
