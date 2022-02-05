import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

NAMES = ['Dana Hausman', 'Corrine Haley', 'Huan Xin (Winnie) Cai', 'Greg Willits', 'Michael Lyda',
         'Aidana Utepkaliyeva',
         'Claudius Taylor', 'Dyian Nikolv', 'Higl Daniel', 'Mary Beth Arroyo', 'Sajini George', 'Natalia Gomez',
         'Riad Mesharafa', 'Shafan Sugarman', 'Sarah Chang', 'Rashmi Venkatesh', 'Higl Daniel', 'Domineco Sacca',
         'Tanzeela Chaudry',
         'Nataliia Zdrok', 'Natnael Argaw', 'Nosa Okundaye', 'Sibel Gulmez', 'Serge Mavuba', 'Geethalakshmi Prasanna',
         'Gwei Balantar',
         'Imran Barker', 'Lesley Ndeh', 'Trevor Unaegbu', 'Abraham Musa', 'Roberto Santos']
print(Fore.BLACK + Back.RED + Style.BRIGHT + "Names = " + ", ".join(NAMES))
print(155 * "-")

# Make an empty list
PerScholas = []
# Loop over the list of names
for student in NAMES:
    # We can use the startswith method to see the student names that start with the letter S
    if student.startswith("S"):
        # then append the results to a list
        PerScholas.append(student)
# print to make sure that it worked
print(Fore.BLACK + Back.LIGHTBLUE_EX + Style.BRIGHT + ", ".join(PerScholas))
print(155 * "-")

# Using a Comprehension you can reduce lines of code into a single line
# ---------------------------------------------------------------------------
PerScholas2 = [student for student in NAMES if student.startswith('S')]
# the expression we want to appear on our list is simply the student; next loop over the names
# but also check that the name starts with the letter S then print
print(Fore.BLACK + Back.LIGHTBLUE_EX + Style.BRIGHT + ", ".join(PerScholas2))
print(155 * "-")

# Lets get fancier: consider a List of tuples
# -------------------------------------------

NEW = [('Dana Hausman', 1996), ('Corrine Haley', 1998), ('Huan Xin (Winnie) Cai', 1997), ('Greg Willits', 2001),
       ('Michael Lyda', 1995), ('Aidana Utepkaliyeva', 2000),
       ('Claudius Taylor', 2001), ('Dyian Nikolv', 2016), ('Higl Daniel', 2009), ('Mary Beth Arroyo', 2010),
       ('Sajini George', 2006), ('Natalia Gomez', 2007),
       ('Riad Mesharafa', 1922), ('Shafan Sugarman', 1980), ('Sarah Chang', 1946), ('Rashmi Venkatesh', 1970),
       ('Higl Daniel', 1919), ('Domineco Sacca', 2000), ('Tanzeela Chaudry', 2020),
       ('Nataliia Zdrok', 2121), ('Natnael Argaw', 2021), ('Nosa Okundaye', 2525), ('Sibel Gulmez', 2527),
       ('Serge Mavuba', 1995), ('Geethalakshmi Prasanna', 2000), ('Gwei Balantar', 3000),
       ('Imran Barker', 1900), ('Lesley Ndeh', 1999), ('Trevor Unaegbu', 2001), ('Abraham Musa', 2000),
       ('Roberto Santos', 1890)]

# Using a list comprehension list all the students born before the year 2000
# ---------------------------------------------------------------------------
pre2k = [student for (student, year) in NEW if year < 2000]
# we want our list to contain the student name but this time when we write the for-loop; each element is a tuple.
# Next We select the students that were born before 2000 using an if clause

print(Fore.BLACK + Back.LIGHTBLUE_EX + Style.BRIGHT + ", ".join(pre2k))
