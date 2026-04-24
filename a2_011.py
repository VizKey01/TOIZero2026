nums = list(map(int, input().split()))

ans = []

for x in nums:
    if x not in ans:
      ans.append(x)

for i in ans:
  print(i, end=" ")