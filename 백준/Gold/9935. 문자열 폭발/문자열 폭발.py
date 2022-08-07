mails = input()
changes = list(input())
c = len(changes)
queue = []
for mail in mails:
    queue.append(mail)
    if len(queue) >= c and queue[-c:] == changes:
        for _ in range(c):
            queue.pop()
else:
    queue = ''.join(queue)
    print(queue) if queue else print('FRULA')