def solution(dirs):
    # 시작 위치인 (0, 0)을 지정
    s_x, s_y = 0, 0
    track = set()
    # 위치 이동시 발생하는 트랙에 따라 s_x, s_y의 값을 변화주고
    # 양 방향을 track에 저장
    # 상, 하, 좌, 우가 5를 넘기지 않도록 함
    for direction in dirs:
        if direction == 'U':
            if s_y < 5:
                track.add((s_x, s_y, s_x, s_y + 1))
                track.add((s_x, s_y + 1, s_x, s_y))
                s_y += 1

        elif direction == 'D':
            if s_y > -5:
                track.add((s_x, s_y, s_x, s_y - 1))
                track.add((s_x, s_y - 1, s_x, s_y))
                s_y -= 1

        elif direction == 'R':
            if s_x < 5:
                track.add((s_x, s_y, s_x + 1, s_y))
                track.add((s_x + 1, s_y, s_x, s_y))
                s_x += 1

        elif direction == 'L':
            if s_x > -5:
                track.add((s_x, s_y, s_x - 1, s_y))
                track.add((s_x - 1, s_y, s_x, s_y))
                s_x -= 1
    # 전체 길이의 절반을 반환 해주면 됩니다.
    return len(track) // 2