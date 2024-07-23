# variables
name = "oju"
print(name)
age = 16

print(age)
inschool = True
print(inschool)

print("")
# opertor
newage = age + 1
print(newage)

fullname = name + "nagar"
print(fullname)

print("")
# confitional

# if (true ){
# do this
# }
# if
if age > 18:
    print("adult")

if age < 18:
    print("child")

print("")

# else
if age > 18:
    print("adult")
else:
    print("child")

print("")

# elif
if age > 18:
    print("adult")
elif age < 18:
    print("child")
else:
    print("of age 18")

print("")
# loop
# for
for i in range(10):
    print(i, "j")

print("")

for i in range(2, 10):
    print(i, "j")

print("")

for i in range(3, 31, 3):
    print(f"3 *  {int(i / 3)} = {i} ")


# function
def name():
    print("oju")


name()
