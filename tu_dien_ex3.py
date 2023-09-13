d1 = ['D1', 'D2', 'D3']
d2 = [1,2,3]
new = {}

# for k, v in zip(d1, d2):
#     new[k] = v
new = dict(zip(d1, d2))
print(new)