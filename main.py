# Задача 1

# class Person:
#     name = "Vasya"
#
# id_1 = Person()
# print(id_1.name)

# Задача 2

# class Person:
#     name = "Vasya"
#
# id_1 = Person()
# id_1.name = "Lena"
# Person.name = "Masha"
#
# print(Person.name)
# print(id_1.name)

# Задача 3

class Holiday:
    pass

friends = Holiday()
friends.name1 = 'Sveta'
friends.name2 = 'Katya'
friends.name3 = 'Lena'
friends.name4 = 'Natasha'
friends.name5 = 'Leonardo DiCaprio'

friends.name5 = 'Pavel'

print("\nОбновленный список друзей:")
print(friends.name1, friends.name2, friends.name3, friends.name4, friends.name5)