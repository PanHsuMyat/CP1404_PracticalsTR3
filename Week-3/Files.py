# Question 1
out_file = open("name.txt", "w")
name = input("What is your name?: ")
print(name, file = out_file)
out_file.close()

# Question 2
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

# Question 3
with open("numbers.txt", "r") as file:
    first_number = int(file.readline())
    second_number = int(file.readline())
    result = first_number + second_number
    print(result)

# Question 4
with open("numbers.txt", "r") as file:
    total = 0
    for line in file:
        total += int(line)
    print(total)