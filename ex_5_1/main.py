
count = 0
total = 0.0

while True:
    sval = input("Enter a Number: ")
    if sval.lower() == "done":
        break
    try:
        fval = float(sval)
    except:
        print("invalid input")
        continue
    total = total + fval
    count = count + 1

try:
    med = total/count
except:
    med = 0.0

print("done!\n")
print(total, count, med)