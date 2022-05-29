import heapq
import collections
q = int(input())
s = collections.defaultdict(int)
Max = []
Min = []
for i in range(q):
    a = list(map(int, input().split()))
    if a[0] == 1:
        k = a[1]
        s[k] += 1
        heapq.heappush(Max, -k)
        heapq.heappush(Min, k)
    elif a[0] == 2:
        k = a[1]
        s[k] = max(0, s[k] - a[2])
    else:
        while s[-Max[0]] == 0:
            heapq.heappop(Max)
        while s[Min[0]] == 0:
            heapq.heappop(Min)
        print(-Max[0] - Min[0])
