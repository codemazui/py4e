
ac = 0.0
count = 0
fname = input("File name: ")

try:
    fh = open(fname)
except:
    print("File not found")
    quit()

for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        snum = line[line.find(":")+1:]
        ac = ac + float(snum)
        count = count + 1

print(ac/count)