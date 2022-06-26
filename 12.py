input_file = open("input.txt")
n = int(input_file.readline())
seq = list(map(int, input_file.readline().split()))
amount = sum(seq)
if (amount % 2 == 1):
    output_file = open("output.txt", "w")
    output_file.write("-1")
    output_file.close()
    exit()

amount = amount // 2
taked = 0
i = 0
while ((i < len(seq)) and (taked < amount)):
    taked += seq[i]
    i += 1

if (taked == amount):
    result = ""
    takedSecondHalf = 0
    takedSecondCount = 0
    for index in range(i, len(seq)):
        takedSecondHalf += seq[index]
        takedSecondCount += 1
        result += f"{seq[index]} "
    if (takedSecondHalf == taked == amount):
        output_file = open("output.txt", "w")
        output_file.write(f"{takedSecondCount} \n")
        output_file.write(result)
        output_file.close()
        print(takedSecondCount)
        print(result)
        exit()

output_file = open("output.txt", "w")
output_file.write("-1")
output_file.close()


