
text_string = ""
text_lines = []
with open('./names.txt', mode = 'r') as f:
    text_string += f.read()
    f.seek(0)
    text_lines = f.readlines()
from collections import Counter
count_names = Counter(text_lines)
print(count_names['Lea'])

with open('./names.txt', mode = 'a') as f:
    f.write('\nJuliana')
    f.write('\nWesley')

for i, name in enumerate(text_lines):
    if name == 'Luke':
        text_lines[i] += 'Skywalker'

print(text_lines)
with open('./names.txt', mode = 'w') as f:
    for line in text_lines:
        f.writelines(line + '\n')

        
print(text_lines[4])
print(text_string[:5])


