import random
alph = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
inp = open("input.txt")
out = open("output.txt", "w")
f = inp.read().split("\n")
kol = int(f[0])
min = int(f[1])
max = int(f[2])
w = f[3]
stat = [0,1]
for i in range(kol):
    x = random.randint(min,max)
    line = ''
    n = 0
    for i in range(x):
        y = random.choice(stat)
        if y==stat[0] and n!=10:
            line+=w
            x-=3
            n+=1
        else:
            line +=random.choice(alph)

    out.write(line+"\n")
out.close()
inp.close()


