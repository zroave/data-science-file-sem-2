n = input("Enter a number: ")
count = 0
for ch in n:
    if ch.isdigit():
        count += 1
print("Digits:", count)
