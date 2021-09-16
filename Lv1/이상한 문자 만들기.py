def solution(s):
    words = s.split(' ')
    length = len(words)
    while length:
        length -= 1
        spelling = ''
        word = words.pop(0)
        for i in range(len(word)):
            if i % 2:
                spelling += word[i].lower()
            else:
                spelling += word[i].upper()
        words.append(spelling)
    return ' '.join(words)