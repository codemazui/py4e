
fh = open("mbox.txt")

dic = dict()
for line in fh:
    if line.strip() == "":
        continue
    wds = line.rstrip().split()
    for w in wds:
        dic[w] = dic.get(w, 0) + 1

l = sorted([(y, x) for x, y in dic.items()], reverse=True)

for v, k in l[:5]:
    print(k, v)
