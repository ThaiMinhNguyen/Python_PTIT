tu_dien = {1: {'k': 2, 'l' : 2}, 2: {'k': 2, 'l' : 2}, 3: {'k': 2, 'l' : 2},4: '3'}

new = dict()
values = []
for k, v in tu_dien.items():
    if v not in values:
        new[k] = v
        values.append(v)
# for k, v in tu_dien.items():
#     new.setdefault(k,v)
print(new)