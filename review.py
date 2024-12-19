# print("Hello World!")













'''
Data types and what they are used for:

Floats: Percentages, decimal numbers, money, etc..
Integers: Whole numbers, counting, etc..
Strings: Anything with text or non-number characters.
Booleans: True of False
'''







'''
This is a multi-line comment...

No need for new comment symbols

It ends here:
'''
"""
This is with double quotes
"""







# my_dictionary = {'key1':1, 'key2':2, 'key3':3}

# del my_dictionary['key1']
# my_dictionary.pop('key2')

# print(my_dictionary)









# for i in range(9):
#     print(i)













# var_1 = 'Some interesting string'

# var_2 = 3

# print(var_1 + var_2)










# my_dictionary = {'first_name':'John', 'last_name':'Doe', 'email':'lost@mymemory.com'}

# result = '-'.join(my_dictionary.keys())

# print(result)










'''
True AND (False AND False OR True) OR False
True


(False OR True AND False) OR (True AND True XOR False)
False    OR   (True XOR False)
False OR True
True
'''







# first_name = "John"
# last_name = "Doe"

# print(f'|{first_name:<10}|{last_name:^10}|')











'''
Write a query that retrieves all fields from the Users table,
that have a user_id above 35 and the result is sorted by their first_name,
and it only shows 10 rows



SELECT *
FROM Users
WHERE user_id > 35
ORDER BY first_name
LIMIT 10
'''






# Dissect components of this line:


# new_person = create_person('George of the Jungle', 'george@jungle.com', 12)












'''
Define these terms:

Primary Key: Unique Identifier, not null, unique
Foreign Key: References a primary key from another table, necessary for creating relationships
Table: A set of tuples(rows) that share the same attributes(fields, columns). Also called a relation
Column: An attribute or field in each row/tuple.
Row: Data representing a single record with matching attributes, aka a tuple.
Result Set: A set of records, in response to a query.

'''






# a, b, c = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)[1::4]


# print(c,a,b)









'''
Write 165 in binary:

128  64  32  16   8   4   2   1
  1   0   1   0   0   1   0   1

  165
  128
  ---
   37
   32
   --
    5
    4
    -
    1
'''








# As a rule which return statement will run?

# def my_function(a, b):
#     if a == 12:
#         return a * 2
#     else:
#         b = b * 3

#     return a + b


# print(my_function(12, 3))






# What is the difference between positional and keyword arguments?


# def my_func(param_1, param_2, param_3, param_4):
#     return param_1+param_2+param_3+param_4



# print(my_func(1, 2, param_4 = 3, param_3 = 4))










# What does a function without a return statment return?


# def add_1(num):
#     num += 1


# print(add_1(5))











# my_list = list(range(12))

# print(my_list[::3])












# What is the differenct between integer division and modulus division?

# print(9//3)

# print(15%7)












# What is a negative index?




# my_list = [1, 2, 3]

# print(my_list[-1])









# def my_func(num):
#     if num < 3:
#         return num + 3

#     return num - 1


# print(my_func(my_func(my_func(4))))







# What is an infinite loop?


# x = 4

# while True:
#     if x > 3:
#         x -=2
#         print(x)
#     if x > 12:
#         break











# How many values does a function return?














# Use .sort() and sorted()


# my_list = [1, 2, 5, 7 ,2, 5, 3]



# print(my_list.sort())














# Your Insert and Update queries are giving no errors, but nothing is appearing in the database,
# what's going wrong?

# connection.commit()













# How do you use ORDER BY














# Use the .join method



# my_list = ['a', 'b', 'c', 'd']

# my_string = ' '.join(my_list)

# print(my_string)









# quote = 'The quick brown fox jumped over the lazy dog'

# quote_list = quote.split(' ', 5)

# print(quote_list)










# Why do we use variable binding?

# user_input = "3; DROP TABLE Users;"

# query = f"SELECT * FROM Users WHERE user_id = ?"
# values = (user_input,)

# cursor.execute(query, values)


'''
Protects against injection attacks,
The strings are atomatically escaped,
Makes the code easier to understand and maintain
'''










# Convert 10110100 to Decimal
'''
 2
128
 32
 16
  4
---
180
'''














# Convert -68 using two's complement

'''
128  64  32  16   8   4   2   1
  0   1   0   0   0   1   0   0

                      1   1
  1   0   1   1   1   0   1   1
  0   0   0   0   0   0   0   1
-------------------------------
  1   0   1   1   1   1   0   0


  68
  64
  --
   4

'''













# Can you change a string after it's been created?














# import sqlite3

# connection = sqlite3.connect('new.db')












# What is the most selling computer of all time?














# What does AUTOINCREMENT do?














# What column in a database table references an existing column from another table?














# What does ROLLBACK do?














# When would you use Indexes on a database?














# What is a many-to-many relationship?  Examples?














'''
In regards to OOP, define these terms:

Class:   Blueprint, details what data an object of this class will have.
Method:  Function that works specifically on objects of this class.
Instance: An object of that class.
__init__: The function called to create an instanse/object of that class.
self:    A standin to the object that the method is working with.
Attribute: A variable that represnts data for an instance of the class.  (key/value pair)

'''




# See examples of inheritance:














# Polymorphism vs Inheritance?














