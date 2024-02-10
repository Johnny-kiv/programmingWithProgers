inp = open("input.txt")
out = open("output.txt", "w")
l = inp.read()
out.write(str(l.count("AB")))
out.close()
inp.close()


