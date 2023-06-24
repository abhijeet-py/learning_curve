import re

string = input('Enter any string: ')

if re.search(r'[@_!#$%^&*()<>?/\|}{~:]', string) is None:
    print('String does not contain any special characters.')
else:
    print('The string contains special characters.')

txt = "The  rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.end())

txt = "The rain in Spain"
x = re.search('hi', txt)
print(x)

txt = "The rain in Spain"
y = re.split("\s", txt)
print(y)

txt = "The rain in Spain @"
x = re.sub("\W", "9", txt)
print(x)
