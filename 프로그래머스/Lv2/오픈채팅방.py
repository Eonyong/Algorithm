def solution(record):
    answer = []
    user = {'Enter':"들어왔습니다.", "Leave":"나갔습니다."}
    
    for code in record:
        chat = code.split(' ')
        # 닉네임 변경의 경우, 
        if chat[0] == 'Change':
            user[chat[1]] = chat[2]
        else:
            # 유저 입장과 퇴장
            if chat[0] == 'Enter':
                # 입장의 경우 유저의 이름을 dictionary에 추가 하는 작업을 진행
                user[chat[1]] = chat[2]
            # 유저 이름을 닉네임이 아닌 유저 아이디로 저장하여 나중에 빠르게 변경할 수 있게 한다
            answer.append([f'{chat[1]}', f'님이 {user[chat[0]]}'])
    
    # 모든 채팅을 answer 리스트에 추가한 이후,
    for i in range(len(answer)):
        # 모든 리스트를 탐색하며 유저 아이디를 저장된 유저 닉네임으로 변경해줍니다.
        answer[i] = user[answer[i][0]]+answer[i][1]
    
    return answer