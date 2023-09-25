with open('DATA.in', 'r') as file:
    content = file.read()

words = content.split()

# for w in words:
#     try:
#         int(w)
#     except:
#         print(w, end = " ")

filtered_words = []
for w in words:
    if not w.isdigit():
        filtered_words.append(w)
    else:
        if len(w) > 19:
            filtered_words.append(w)

# filtered_words = [word for word in words if not word.isdigit() and len(word) > 10]
# filtered_words = [word for word in words if not word.isdigit()]

sorted_words = sorted(filtered_words)

output = ' '.join(sorted_words)
print(output)