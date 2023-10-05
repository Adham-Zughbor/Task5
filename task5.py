#Q1
name = input('your name: ')
age = int(input('your age: '))
street = input('street: ')
city = input('city: ')
country = input('country: ')
address = street, city, country
#Q2
print(f'"Name: {name}"')
print(f'"Age: 20"')
print(f'"Address:{street},{city},{country}"')
#Q3
print(f'"Hello {name}, Your age is {age-5} years old, your address is {street}, {city}, {country}"')
#Q4
age = str(age)

print(type(name)), type(age)
print(type(street), type(city))
print(type(country))
#q5
age = int(age)

print(f' Hello {name}, How Are You? \\ """ Your Age Is "{age-5}"" +\n And Your Country Is: {country}')
#Q6
print(f' Hello {name}, How Are You? \\ \n """ Your Age Is "{age-5}"" + And\n Your City Is: {city}')
#q7
name = 'ITF Gsg Python'
n1 = name[0]
n2 = name[2]
n3 = name[-1]

print(f'First Letter Is "{n1}"')
print(f'First Letter Is "{n2}"')
print(f'First Letter Is "{n3}"')
#q8
print(name[-3:])
print(name[0:3])
print(name[0:7:2])
print(name[-1:-7:-1])
#q9
name = "$&$&Mohammed$&$&"
print(name.strip('$&'))
#q9
msg = "I %7 Python And Although I %7 GSG with Zakaria"
#q10
print(msg.replace('%7', 'Love'))
#q11+Q12
num1 = "4"
num2 = "56"
num3 = "963"
num4 = "385"
# num5 = "8719"
num6 = "87190"


print(num1.zfill(5))
print(num2.zfill(5))
print(num3.zfill(5))
print(num4.zfill(5))
print(num6.zfill(5))
#q13
ex = 'come in see me before i fall apart'
print(ex.capitalize())
print(ex.title())
#capitalize() method capitalizes the first character of the first word in a string and converts the rest of the characters to lowercase.
# On the other hand, title() method capitalizes the first character of each word in a string

#14
first_name = "Dana"
print("*" * 11 + first_name)
print("*" * 11 + first_name + "*" * 11)
print(first_name + "*" * 11)
#15
name_one = "SaMER"
name_two = "Abed"
print(name_one.swapcase())
print(name_two.swapcase())
print(name_one.lower())
print(name_two.upper())
#16
print(name_one.isupper())
print(name_two.islower())
#17
print(name_one.startswith('S'))
print(name_two.endswith('HD'))
#18
msg = "I Love Python And Although I Love GSG with Zakaria"
love_count = msg.count("Love")
t_count = msg.count("t")
print(f'Number of <Love> is: {love_count}')
print(f'Number of <t> is: {t_count}')
#19
msg = "I %7 Python And Although I %7 GSG with Zakaria"

modified_msg = msg.replace("%7", "Love", 1)
print(modified_msg)


