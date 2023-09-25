# arithmetic: +, -, *, /, %

print(10 - 2)
print(10 + 2)
print(10 * 3)

print(10 / 3)
print(10 / 2)

print(10 % 3)

# shorthand assignment operators: =, +=, -=, *=, /=, %=

a = 100
a = 200
print(a)

a += 100
print(a)

a -= 50
print(a)

a /= 2
print(a)

# logical operators: and, or, not
s = 'Hello World'
print('H' and 'W' in s)

print(True and True)
print(True or False)

s = 'Java Python C# C++'
print('Java' or 'Rubby' in s)

age = 29
citizenship = 'USA'
is_eligible = age >= 18 and citizenship == 'USA'
print(is_eligible)

has_java = 'Java' in s
print(has_java)

# !contains()
print('Python' not in s)

print(not False)
print(not True)  # !

print('---------------------------------')
s = 'Java'
s2 = 'Java'
print(s is s2)