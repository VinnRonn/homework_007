usr_list = ["world","sagas", "apple", "cup", "deed", ]

palindrom_pars = list(filter(lambda x: x == x[::-1], usr_list))
print(palindrom_pars)

test = list(map(lambda x: x == x[::-1], usr_list))
print(test)


#что делать с reduce - не понял, т.к. это свертка списка, то как проверить на палиндром?