n = int(input())
nums = list(map(int, input().split()))

total = 0
even = 0
odd = 0

for x in nums:
    total += x

    if x % 2 == 0:
        even += 1
    else:
        odd += 1

print("SUM", total)
print("EVEN", even)
print("ODD", odd)