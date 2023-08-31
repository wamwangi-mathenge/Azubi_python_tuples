address = (52066, "Aachen", "Eupener Str. 70", "0241-6009-12345")

students = (
    "Brian",
    "Mathenge",
    123456,
    "Python for beginners",
    "Azubi Africa",
    address
)

print(address[0])
print(address[1])
print(students[0])
print(students[1])
print(students[5][2])
print(students[-1])
print(address[-1])

numbers = (1, 1, 2, "three", "four", "V", 6)

print(numbers[2:4])
print(len(numbers))
print(numbers.count(1))
print(numbers.index("V"))


tuple1 = (12312, "abababa", [1, 2, 3, 4, 5], ("a", "b", "c", "d"), "end")
print(tuple1)