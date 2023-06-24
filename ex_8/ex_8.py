
fh = open("mbox-short.txt")

for line in fh:
#    if line == "\n" :
#        continue
    wds = line.rstrip().split()

    #guardian pattern
#    if len(wds) < 3:
#        continue
#    if wds[0] != "From":
#        continue

    #guardian in a compound statement (must come first)
    if len(wds) < 3 or wds[0] != "From":
        continue
    
    print(wds[2])