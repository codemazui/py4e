
def count(word, letter):
    count = 0
    for x in word:
        if x == letter:
            count = count +1
    return count


word = input("what is the word?: ")
letter = input("what is the letter?: ")


c = count(word, letter)

print(c)