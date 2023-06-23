
count = 0
total = 0.0

while True :
    sval = input("Enter a Number: ")
    if sval == "done" :
        break
    try:
        fval = float(sval)
    except:
        print("invalid input")
        continue
    total = total + fval
    count = count + 1

print("\nAll done!\n")
print(total, count, total/count)