f = open('ryzeal_01.txt','r')
lines = f.readlines()
#print(lines[1][3:])
q_c = []
for l in lines:
    if l[0].isdigit():
        q_c.append([l[0],l[3:-1]])
    elif l[0] == '-':
        break
print(q_c)
