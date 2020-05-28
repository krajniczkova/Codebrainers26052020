# Write a Python class which has two methods get_String and print_String.
# get_String accept a string from the user and print_String print the string in upper case.

# Tworzymy klasę

class TwoMethods():
    def __init__(self):
        # i mówimy, że self będzie stringiem 1, który jest inicjalnie pusty
        self.str1 = ""

    # definiujemy metody
    def get_String(self):
        self.str1 = input("Podaj stringa: ")

    def print_String(self):
        print(self.str1.upper())


str1 = TwoMethods()
str1.get_String()
str1.print_String()
