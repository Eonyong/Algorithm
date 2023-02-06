import sys
import math

go, back, finish = map(int, sys.stdin.readline().split())

print(math.ceil((finish - go) / (go - back)) + 1)