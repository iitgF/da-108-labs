while True:
    username = input("Enter username: ")
    if username == 'q':
       print("Exiting the program.")
       break
    elif len(username)<5:
        print("Username is too short, please try again.")
    else: print(f"Username is {username}.")
