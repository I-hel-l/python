my_string = ''''этот если способ вы плохо это подходит читаете для что-то
шифрования пошло важных не сообщений так'''

print(my_string)

#dir(my_string)
#help(str)

my_list = my_string.split()

print(my_list)

for x in range(0, len(my_list), 2):
    print(my_list[x])
