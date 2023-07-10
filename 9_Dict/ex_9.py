
fh = open("mbox.txt")

dic = dict()
for line in fh:
    if line.strip() == "":
        continue
    wds = line.rstrip().split()
    for w in wds:
        dic[w] = dic.get(w, 0) + 1

bk = None
bv = None
for k, v in dic.items():
    if bv == None or v > bv:
        bv = v
        bk = k

print(bk, dic[bk])