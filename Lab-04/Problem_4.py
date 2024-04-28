string_1 = input("Enter String 1: ")
string_2 = input("Enter String 2: ")
if len(string_1)>len(string_2):
    print("String 1 is longer.")
elif len(string_1)<len(string_2):
    print("String 2 is longer.")
else: print("Both strings are equally long.")

