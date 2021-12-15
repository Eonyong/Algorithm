from collections import defaultdict

N, M = map(int, input().split())
answer = []
rooms = defaultdict(list)

for _ in range(N):
    rooms[input()] = [False] * 9

for _ in range(M):
    room, s, e = input().split()
    s, e = int(s) - 9, int(e) - 9
    for idx in range(s, e):
        rooms[room][idx] = True

avail_room = defaultdict(list)
for room, times in rooms.items():

    avail_room[room] = []
    avail_time = -1
    for time in range(9):
        if avail_time == -1 and not times[time]:
            avail_time = time
        elif avail_time != -1 and times[time]:
            if not avail_time:
                avail_room[room].append(f'0{avail_time + 9}-{time + 9}')
            else:
                avail_room[room].append(f'{avail_time + 9}-{time + 9}')
            avail_time = -1
    else:
        if avail_time != -1 and not times[-1]:
            if not avail_time:
                avail_room[room].append(f'0{avail_time + 9}-18')
            else:
                avail_room[room].append(f'{avail_time + 9}-18')

for key, val in avail_room.items():
    answer.append([key, val])
else:
    answer.sort(key=lambda x:x[0])

flag = 0
for car, time in answer:
    if flag:
        print('-----')

    print(f'Room {car}:')
    if time:
        print(f'{len(time)} available:')
        for t in time:
            print(t)
    else:
        print('Not available')
    flag += 1