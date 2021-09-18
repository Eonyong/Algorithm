def solution(nums):
    answer = 0
    breed = len(set(nums))
    total = len(nums) // 2
    return min(breed, total)