x = input()
v = [0]*11

def Try(s):
    if len(s) == len(x):
        print(s)
    for i in range(len(x)):
        if(v[i] == 0):
            v[i] = 1
            Try(s + x[i])
            v[i] = 0

Try('')