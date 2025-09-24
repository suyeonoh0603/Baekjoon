piece = [1,1,2,2,2,8]
founded = list(map(int, input().split()))

result = []
for i in range (6) :
    diff = piece[i] - founded[i]
    result.append(diff)

print(*result)