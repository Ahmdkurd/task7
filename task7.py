
rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\n")
number = int(input("Enter number: "))
total = 0
for i in range(1, number + 1):
    total += i
print("Sum is:", total)

print("\n")
name = input("Enter your name: ")
length = len(name)
for i in range(length):
    for j in range(i + 1):
        print(name[j], end="")
    print()

for i in range(length - 1, 0, -1):
    for j in range(i):
        print(name[j], end="")
    print()

print("\n")
word = input("Enter a word to reverse: ")
reversed_word = word[::-1]
print("Reversed word:", reversed_word)

print("\n")
range_input = int(input("Enter range: "))
while range_input >= 1:
    print(range_input, end=" ")
    range_input -= 1
print()

print("\n")
for i in range(1, 11):
    print(i * 5, end=" ")
print()

print("\n")
limit_number = int(input("Enter the Limit_number: "))
max_display = int(input("Enter the maximum outputs to display (Max_display_on_screen): "))
target_number = int(input("Enter the Target_number: "))
count = 0
for i in range(target_number, limit_number + 1, target_number):
    if count < max_display:
        print(i, end=" ")
        count += 1
    else:
        break
print()
