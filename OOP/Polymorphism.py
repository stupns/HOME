# Python program to demonstrate in-built polymorphic functions

# len() being used for a string
print(len("geeks"))  # >> 5

# len() being used for a list
print(len([10, 20, 30]))  # >> 3


# A simple Python function to demonstrate Polymorphism

def add(x, y, z=0):
    return x + y + z


# Driver code
print(add(2, 3))  # >> 5
print(add(2, 3, 4))  # >> 9
print('\n')


# Polymorphism with class methods:


class India:
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")


class USA:
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")


obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()
"""
>> New Delhi is the capital of India.
>> Hindi is the most widely spoken language of India.
>> India is a developing country.
>> Washington, D.C. is the capital of USA.
>> English is the primary language of USA.
>> USA is a developed country.
"""
print('\n')

# Polymorphism with Inheritance:


class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")


class sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")


class ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")


obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()  # There are many types of birds.
obj_bird.flight()  # Most of the birds can fly but some cannot.

obj_spr.intro()  # There are many types of birds.
obj_spr.flight()  # Sparrows can fly.

obj_ost.intro()  # There are many types of birds.
obj_ost.flight()  # Ostriches cannot fly.

print('\n')


# Polymorphism with a Function and objects:


def func(obj):
    obj.capital()
    obj.language()
    obj.type()


obj_ind = India()
obj_usa = USA()

func(obj_ind)
func(obj_usa)
print('\n')

# Implementing Polymorphism with a Function


class Ukraine:
    def capital(self):
        print("Kiev is the capital of Ukraine.")

    def language(self):
        print("Ukrainians is the most widely spoken language of Ukraine.")

    def type(self):
        print("Ukraine is a developing country.")


class Poland:
    def capital(self):
        print("Warsaw, D.C. is the capital of Poland.")

    def language(self):
        print("Poland is the primary language of Poland.")

    def type(self):
        print("Poland is a developed country.")


def func(obj):
    obj.capital()
    obj.language()
    obj.type()


obj_uk = Ukraine()
obj_poland = Poland()


func(obj_uk)
#  >> Kiev is the capital of Ukraine.  Ukrainians is the most widely spoken language of Ukraine.
#  >> Ukraine is a developing country.
func(obj_poland)
#  >> Warsaw, D.C. is the capital of Poland.  Poland is the primary language of Poland.
#  >> Poland is a developed country.
