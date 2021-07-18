student=[['Harry',37.21],['Berry',37.21],['Tina',37.2],['Akriti',41],['harsh',41], ['Murali',37.2], ['chandhan',42]]
score_map = {}
score_list = []
runner_up = []
for i in student:
   score_list.append(i[1])

[37.21, 37.21, 37.2, 41, 39]
[37.2, 37.21, 37.21, 41, 39]

for i in range(0, len(score_list)):
    min_index = i #3
    for j in range(i+1, len(score_list)): #j = 4
        if score_list[i] < score_list[j]: #41 >39
            min_index = j
            score_list[i], score_list[j] = score_list[j], score_list[i]
print(score_list)

min_v = min(score_list)
# min_v = score_list[0]

least_diff = [i for i in score_list if i - min_v != 0]

for i in student:
    if i[1] == least_diff[0]:
        runner_up.append(i[0])

print(runner_up)


