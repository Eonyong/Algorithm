def solution(n):
    binary = bin(n)[2:]
    if binary[-2:] == '10':
        binary = binary[-2:] + binary[:-2]
    elif binary[-2:] == '01':
        binary[-2:] = binary[-2:].replace('01', '10')
    elif binary[-2:] == '11':
        if '0' in binary:
            binary = binary[:binary.rindex('0')] + binary[binary.rindex('0') + 1:] + binary[
                                                                                     binary.rindex('0'):binary.rindex(
                                                                                         '0') + 1]
        else:
            print(bin(1 << len(binary)))
            print(1 << len(binary) + n >> 1)
    return int(binary, 2)


print(solution(78))
print(solution(15))
print(solution(11))
