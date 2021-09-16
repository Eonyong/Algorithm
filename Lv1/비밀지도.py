def solution(n, arr1, arr2):
    answer = []
    for idx in range(n):

        bin_list1 = list(map(int, list(bin(arr1[idx]))[2:]))
        bin_list2 = list(map(int, list(bin(arr2[idx]))[2:]))

        if len(bin_list1) < n:
            for _ in range(n - len(bin_list1)):
                bin_list1.insert(0, 0)
        if len(bin_list2) < n:
            for _ in range(n - len(bin_list2)):
                bin_list2.insert(0, 0)
        
        bin_list = [bin_list1[i] + bin_list2[i] for i in range(n)]
        bin_list = map(lambda x: '#' if x else ' ', bin_list)
        bin_list = ''.join(bin_list)
        
        answer.append(bin_list)
    
    return answer