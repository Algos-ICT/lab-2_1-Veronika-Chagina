file = open('input.txt')
need = int(file.readline())
tank = int(file.readline())
n = int(file.readline())
stations = list(map(int, file.readline().split()))
file.close()


def getFillsCount(need, tank, stations):
    stations.append(need)
    curr = 0
    count = 0
    for i in range(len(stations) - 1):
        if stations[i] - curr > tank:
            return -1
        if (stations[i + 1] - curr) > tank:
            curr = stations[i]
            count += 1
    if stations[len(stations) - 1] - curr < tank:
        return count
    else:
        return -1


count = getFillsCount(need, tank, stations)
out = open('output.txt', 'w')
out.write(str(count))
print(str(count))
out.close()
