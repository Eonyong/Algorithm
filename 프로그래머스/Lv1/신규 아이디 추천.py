def solution(new_id):
    # 1
    new_id = new_id.lower()
    # 2
    new = ''
    for w in new_id:
        if w.isdigit() or w.isalpha() or w == '-' or w == '_' or w == '.':
            new += w
    new_id = new
    # 3
    while True:
        if '..' in new_id:
            new_id = new_id.replace('..', '.')
        else:
            break
    # 4
    if new_id.startswith('.'):
        new_id = new_id[1:]
    if new_id.endswith('.'):
        new_id = new_id[:-1]
    # 5
    if new_id == '':
        new_id += 'a'
    # 6
    if len(new_id) >= 16:
        new_id = list(new_id)
        new_id = ''.join(new_id[:15])
        if new_id.endswith('.'):
            new_id = new_id[:-1]
    # 7
    if len(new_id) <= 2:
        new_id = list(new_id)
        while len(new_id) < 3:
            new_id.append(new_id[-1])
        new_id = ''.join(new_id)

    return new_id