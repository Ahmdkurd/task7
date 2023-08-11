
def print_number_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

rows = int(input("Enter number of rows: "))
print_number_pattern(rows)

print("\n")
def calculate_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

number = int(input("Enter number: "))
sum_result = calculate_sum(number)
print("Sum is:", sum_result)


print("\n")
def print_name_pattern(name):
    length = len(name)
    for i in range(length):
        for j in range(i + 1):
            print(name[j], end="")
        print()

    for i in range(length - 1, 0, -1):
        for j in range(i):
            print(name[j], end="")
        print()

name = input("Enter your name: ")
print_name_pattern(name)


print("\n")
def reverse_word(word):
    return word[::-1]

word = input("Enter a word to reverse: ")
reversed_word = reverse_word(word)
print("Reversed word:", reversed_word)


print("\n")
def print_descending_natural_numbers(n):
    while n >= 1:
        print(n, end=" ")
        n -= 1
    print()

range_input = int(input("Enter range: "))
print_descending_natural_numbers(range_input)


print("\n")
def print_multiples_of_5():
    for i in range(1, 11):
        print(i * 5, end=" ")
    print()

print_multiples_of_5()


print("\n")
def print_multiples_with_limit_target(limit_number, target_number, max_display):
    for i in range(target_number, limit_number + 1, target_number):
        print(i, end=" ")
        max_display -= 1
        if max_display == 0:
            break
    print()

limit_number = int(input("Enter the Limit_number: "))
max_display = int(input("Enter the maximum outputs to display (Max_display_on_screen): "))
target_number = int(input("Enter the Target_number: "))
print_multiples_with_limit_target(limit_number, target_number, max_display)

