
fh = open("mbox-short.txt")

for line in fh:
    print(line.rstrip().upper())