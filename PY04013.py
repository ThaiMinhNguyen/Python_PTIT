from datetime import datetime

def change(s):
    k = list(map(int, s.split(':')))
    return k[0]*60 + k[1]

class Tram:
    def __init__(self,cnt,  name, start, end, record):
        self.ma = "T" + '%02d'%cnt
        self.name = name
        self.record = record
        self.time = change(end) - change(start)

    def __str__(self):
        return f"{self.ma} {self.name} " + "{:.2f}".format(self.record/self.time * 60)


cnt = 1
ls = []
for _ in range(int(input())):
    ten = input()
    ok = 0
    for i in ls:
        if ten == i.name:
            start = input()
            end = input()
            i.time += change(end) - change(start)
            i.record += int(input())
            ok = 1
            break
    if ok == 0:
        ls.append(Tram(cnt, ten, input(), input(), int(input())))
        cnt+=1

for i in ls:
    print(i)

