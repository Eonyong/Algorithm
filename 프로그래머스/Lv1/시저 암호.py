def solution(s, n):
    change_word = ''
    for char in s:
        if 65 <= ord(char) <= 90:
            if ord(char) + n > 90:
                change_word += chr(ord(char) + n - 26)
            else:
                change_word += chr(ord(char) + n)
        elif 97 <= ord(char) <= 122:
            if ord(char) + n > 122:
                change_word += chr(ord(char) + n - 26)
            else:
                change_word += chr(ord(char) + n)
        else:
            change_word += char

    return change_word