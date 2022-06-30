while True:
    sentences = input()
    if sentences == '.':
        break
    else:
        box = []
        for sentence in sentences:
            if sentence in ['(', '[']:
                box.append(sentence)
            elif sentence == ')':
                if box and box.pop() == '(':
                    continue
                else:
                    print('no')
                    break
            elif sentence == ']':
                if box and box.pop() == '[':
                    continue
                else:
                    print('no')
                    break
        else:
            if box:
                print('no')
            else:
                print('yes')