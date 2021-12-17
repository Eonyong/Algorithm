number = int(input())

for num in range(1, number):
    num_ls = sum(map(int, list(str(num))))
    if num + num_ls == number:
        print(num)
        break
else:
    print(0)