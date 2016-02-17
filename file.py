fo = open("test.py", "rw+")
print fo.name
i = 0
fo.writelines("#:0")
while(fo.readline()):
    i = i + 1
    sequence = "#:%s" % i
    print sequence
    fo.writelines(sequence)
fo.close()

