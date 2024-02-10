inp = open("input.txt")
out = open("output.txt", "w")
l = list(inp.read())
n = 0
for i in range(len(l)):
    if l[i] == "A" and l[i+1]=="B":
       n+=1
out.write(str(n))
out.close()
inp.close()


