path = "/Users/zaha/Примеры решений/100  Days of coding/Day24/lect/lec7/Desktop"

with open(f'{path}/my_file.txt') as file:
    contents = file.read()
    print(contents)
#Второй способ иморта ТОП!!!!!!!!!!!!!!
with open("../../lect/lec7/Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)


