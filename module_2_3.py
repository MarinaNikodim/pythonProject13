my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
new_list=[item for item in my_list if item != 0]
while index < len(new_list):
    if new_list[index] < 0:
        break
    else:
        print(new_list[index])
        index = index + 1

#2nd vertion
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
my_list.remove(0)
while index < len(my_list):
    if my_list[index] < 0:
        break
    else:
        print(my_list[index])
        index = index + 1
#3d vertion Прошу пояснить, почему в этом варианте не работает программа, что не так?
#while index < len(my_list):
#    if my_list[index] == 0:
#        continue
#    if my_list[index] < 0:
#        break
#    else:
#        print(my_list[index])
#        index += 1


















