from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge = deque()
    bridge_weight = deque()
    truck_weights = deque(truck_weights)
    cnt = 0
    while True:
        cnt += 1
        if truck_weights:
            if sum(bridge_weight) + truck_weights[0] <= weight:
                w = truck_weights.popleft()
                bridge.append([w, cnt])
                bridge_weight.append(w)
        if bridge_length == cnt - bridge[0][1] + 1:
            bridge.popleft()
            bridge_weight.popleft()
            if not bridge and not truck_weights:
                break

    return cnt + 1