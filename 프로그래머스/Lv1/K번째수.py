class items:
    def __init__(self, array, command):
        self.array = array
        self.command = command
    
    def Knum(self):
        a = self.array
        c = self.commands
        answer = []
        for i in range(len(c)):
            first = c[i][0] - 1
            last = c[i][1]
            Index = c[i][2] - 1
            cut = a[first:last]
            cut.sort()
            answer.append(cut[Index])
        print(answer)

def solution(array, commands):
    answer = items(array, commands)
    answer.Knum
    
    return answer