x = input()
check = 1
# print(x[-2:])
for i in x:
    # print(i)
    if(i.isalpha() == False and i != '_' and i != '.') :
        check = 0
        break

# print(check)
if(check == 0 or x[-3:].lower() != '.py'):
    print("no")
else:
    print("yes")