import random

start = random.randint(0, 13)

i = 0
path = "./rotowire.txt"
f = open(path, 'r', encoding='utf-8')
lines = list()
line = f.readline()

while len(line) > 0:
    if i % 14 == start:
        lines.append(line)
    i += 1
    line = f.readline()
f.close()

pathNew = "./test.text"
f = open(pathNew, 'w')
f.truncate()
f.writelines(lines)
f.close()
