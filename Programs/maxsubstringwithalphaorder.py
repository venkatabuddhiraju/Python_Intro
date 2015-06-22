str = 'abcdefghijklmnoabcdefghijabababcdefghijklmnopabcdefgababcdabcdefghijklabcdefghijklmnopqrst'
a = 0
results = 0
curFirstIndex = 0
curLastIndex = 0
firstIndex = 0
lastIndex = 0
c = str[0]
for i in range(len(str)):
    if str[i] > c:
        results = i + 1
    else:
        firstIndex = i
        results = 0
    c = str[i]
    if results - firstIndex > curLastIndex - curFirstIndex:
            curLastIndex = results
            curFirstIndex = firstIndex
print 'Longest substring in alphabetical order is ' + str[curFirstIndex:curLastIndex]