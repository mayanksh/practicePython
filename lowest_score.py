score_list = {}
for _ in range(input()):
    name = raw_input()
    score = float(raw_input())
    arr = map(int, input().split())
    arr = list(set(list(arr)))
    if score in score_list:
        score_list[score].append(name)
    else:
        score_list[score] = [name]
new_list = []
for i in score_list:
    new_list.append([i, score_list[i]])
new_list.sort()
result = new_list[1][1]
result.sort()
print (*result, sep = "\n")
