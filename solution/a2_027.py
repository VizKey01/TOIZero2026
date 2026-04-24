n = int(input())

scores = []

for i in range(n):
    x = int(input())
    scores.append(x)

max_score = scores[0]

for x in scores:
    if x > max_score:
        max_score = x

count = 0

for x in scores:
    if x == max_score:
        count += 1

print(max_score)
print(count)
