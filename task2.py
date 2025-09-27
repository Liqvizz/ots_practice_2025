cnt = 0
for line in open('9zad.txt'):
    a = sorted([int(x) for x in line.split()])
    nepovt = [x for x in a if a.count(x) == 1]
    povt = [x for x in a if a.count(x) == 3]
    if len(nepovt) == 3 and sum(povt) > sum(nepovt):
        print(povt)
        cnt+=1
print(cnt)


