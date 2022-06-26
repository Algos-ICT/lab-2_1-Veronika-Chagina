input_file = open("input.txt")
n, height = map(int, input_file.readline().split())
apples = []
result = ""
for i in range(n):
    minus, plus = map(int, input_file.readline().split())
    if(plus >= minus) and (height > minus):
        height += (plus - minus)
        result += f"{i+1} "
    else:
        apples.append((minus, plus, i))
input_file.close()
apples = list(sorted(apples, key=lambda x: x[0])) # [minus, plus, i]
isHeightUp = True
isPositiveExist = False
while isHeightUp:
    toDelete = []
    isHeightUp = False
    isPositiveExist = False
    for i in range(len(apples)):
        if apples[i][1] >= apples[i][0]:
            isPositiveExist = True
            if height > apples[i][0]:
                height += (apples[i][1] - apples[i][0])
                result += f"{apples[i][2] + 1} "
                toDelete.append(apples[i])
                isHeightUp = True
    if isPositiveExist and (isHeightUp == False):
        result = "-1"
        break
    for delete in toDelete:
        apples.remove(delete)
for i in range(len(apples)):
    if apples[i][0] >= height:
        result = "-1"
        break;
    height += (apples[i][1] - apples[i][0])
    if height <= 0:
        result = "-1"
        break
    result += f"{apples[i][2] + 1} "
output_file = open("output.txt", "w")
output_file.write(result)
output_file.close()
print(result)
