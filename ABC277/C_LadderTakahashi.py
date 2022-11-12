import collections
n = int(input())
l = collections.defaultdict(list)
for i in range(n):
    a, b = map(int, input().split())
    l[a].append(b)
    l[b].append(a)


def bfs(x, y):
    ans = {1}
    q = collections.deque([y])
    while q:
        qq = q.popleft()
        for c in x[qq]:
            if c not in ans:
                q.append(c)
                ans.add(c)
    return max(ans)


print(bfs(l, 1))
