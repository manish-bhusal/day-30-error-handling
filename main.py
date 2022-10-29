# FileNotFoundError
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["kejfkdfy"]

# IndexError
# fruit_list = ["Apple", "Banana", "Mango"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text+5)

# ----------------------------------------------------------------------
# FileNotFound
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", mode="w")
#     file.write("A simple file.")
# except KeyError as error_message:
#     print(f"The Key {error_message} doesn't exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed!")

# Raise Keyword
number = int(input("Type number below 10: "))
if number >= 10:
    raise ValueError("Only number less than 10 are allowed.")
print("You got it!")
