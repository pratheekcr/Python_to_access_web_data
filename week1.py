import re
list = []
fhand = open('regex_sum_92864.txt')
for line in fhand:
    word = (re.findall('[0-9]+',line))
    for str in word:
        list.append(str)
print(list)
sum = 0
for str in list:
    str1 = int(str)
    sum += str1
print(sum)
#print(word)

