def f(l, r):
    global cnt
    sort_ls = []
    i, j = 0, 0
 
    if l[-1] > r[-1]:
        cnt += 1
 
    while i < len(l) and j < len(r):
        if l[i] > r[j]:
            sort_ls.append(r[j])
            j += 1
        else:
            sort_ls.append(l[i])
            i += 1
 
    if i == len(l):
        for z in range(j, len(r)):
            sort_ls.append(r[z])
 
    elif j == len(r):
        for z in range(i, len(l)):
            sort_ls.append(l[z])
 
    return sort_ls
 
 
def mg_sort(array):
    if len(array) == 1:
        return array
    else:
        left = mg_sort(array[:len(array) // 2])
        right = mg_sort(array[len(array) // 2:])
    return f(left, right)
 
 
for tc in range(1, int(input()) + 1):
    N = int(input())
    cnt = 0
    arr = list(map(int, input().split()))
    print(f'#{tc} {mg_sort(arr)[N//2]} {cnt}')
