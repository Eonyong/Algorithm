from collections import deque

def solution(cacheSize, cities):
    answer = 0
    # cacheSize가 0인 경우와 아닌 경우를 분리
    if cacheSize:
        # 배열 순서대로 이므로 deque를 이용해 앞에서 차례대로 계산하도록 함
        cache = deque()
        cities = deque(cities)
        # cities의 배열이 전부 비워질 때까지 수행
        while cities:
            city = cities.popleft().lower() # 대소문자 의미가 없으므로 모두 lower
            # 캐시 안에 해당 도시가 존재하는 경우
            if city in cache:
                answer += 1
                # 캐시가 캐시 사이즈보다 작으면
                if len(cache) < cacheSize:
                    cache.remove(city)  # 중복되지 않게 가지고 있는거 지움
                    cache.append(city)  # 그리고 추가
                else:
                    # 캐시가 크면 이전의 자신을 지운다 
                    if cache:
                        cache.remove(city)
                    cache.append(city)
            # 해당 도시가 존재하지 않을 경우
            else:
                answer += 5
                # 크기가 작은 경우에는 그냥 대입
                if len(cache) < cacheSize:
                    cache.append(city)
                else:
                    # 가장 먼저 들어온 것을 지우고 추가
                    if cache:
                        cache.popleft()
                    cache.append(city)
    # cacheSize가 0인 경우엔 도시의 길이에 *5를 해준 값을 return
    else:
        return 5 * len(cities)
        
    return answer