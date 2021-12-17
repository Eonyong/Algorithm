words = [set() for _ in range(50)]
N = int(input())

for _ in range(N):
    word = input()
    words[len(word) - 1].add(word)

for idx in range(50):

    for w in sorted(words[idx]):
        print(w)