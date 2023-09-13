
def check(n):
    for i in range(len(n)):
        if(n[i] != '4' and n[i] != '7'):
            return False
    return True

for t in range(int(input())):
    a = input()
    if(check(a)):
        print("YES")
    else:
        print("NO")
