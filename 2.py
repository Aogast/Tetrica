f = open('names.txt', mode='r')
array = f.read().split('","')
array = [array[0][1:]] + array[1:-1] + [array[-1][:-1]]
array.sort()
names = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
sum = 0
for i in range(len(array)):
    sum_now = 0
    for j in array[i]:
        sum_now += names.find(j) + 1
    sum += sum_now * (i + 1)
print(sum)
