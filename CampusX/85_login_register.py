'''
Write a dummy program that can perform login and registration using a menu driven program
'''

# Initialize a dictionary to store usernames and passwords
users = {}

while True:
    print("\n1. Register\n2. Login\n3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        # Registration
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        users[username] = password
        print("Registration successful!")

    elif choice == 2:
        # Login
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in users and users[username] == password:
            print("Login successful!")
        else:
            print("Invalid username or password!")

    elif choice == 3:
        # Exit
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
