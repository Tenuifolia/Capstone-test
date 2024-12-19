import bcrypt


unencrypted_password = "Test123!"

salt = bcrypt.gensalt()
encoded_password = unencrypted_password.encode('utf-8')

encrypted_password = bcrypt.hashpw(encoded_password, salt)

# encrypted_password = bcrypt.hashpw(unencrypted_password.encode('utf-8'), bcrypt.gensalt())




database_password = encrypted_password

# user_response = "Test123!asdfasdfasdf"

# print(bcrypt.checkpw(user_response.encode('utf-8'), encrypted_password))



while True:
    user_response = input("Enter your password: ")
    if bcrypt.checkpw(user_response.encode('utf-8'), database_password):
        print("Correct, well done.")
        break
    else:
        print("Wrong... Try again.")








# def add_user():
#     user_fname = input("First Name: ")
#     user_lname = input("Last name: ")
#     user_password = input("Enter Password: ")

#     encrypted_password = bcrypt.hashpw(user_password.encode('utf-8'), bcrypt.gensalt())

#     values = (user_fname, user_lname, encrypted_password)
#     cursor.execute("INSERT INTO Users (first_name, last_name, password) VALUES (?,?,?)", values)



# while True:


#     try:
#         print(4+'4')
#     except:
#         break



# user_input = input("Search person: ")


# query = "SELECT * FROM Users WHERE first_name LIKE ? or last_name LIKE ?"

# cursor.execute(query, ("%"+"user_input"+"%", f"%{user_input}%"))