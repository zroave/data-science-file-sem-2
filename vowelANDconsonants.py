s = input("Enter a string: ").lower()
v = c = 0
for ch in s:
    if ch in "aeiou":
        v += 1
    elif ch.isalpha():
        c += 1
print("Vowels:", v)
print("Consonants:", c)
