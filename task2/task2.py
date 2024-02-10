inp = open("input.txt")
out = open("output.txt", "w")
f = inp.read().split("\n")
for s in range(len(f)):
    l = f[s]
    n = 0
    for i in range(len(l)):
        if l[i] == "C" and l[i+1]=="D" and l[i+2]=="A":
           n+=1
    out.write(str(n)+"\n")

out.close()
inp.close()


