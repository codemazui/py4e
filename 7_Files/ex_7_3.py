
ac = 0.0
count = 0
fname = input("File name: ")

try:
    fh = open(fname)
except:
    if fname == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
    else:
        print("File not found")
    quit()

for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        sf = line[line.find(":")+1:]
        ac = ac + float(sf)
        count = count + 1

print(ac/count)