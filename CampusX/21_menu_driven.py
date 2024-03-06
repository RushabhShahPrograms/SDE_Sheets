'''
Write a menu driven program - 1.cm to ft 2.kl to miles 3.usd to inr
4.exit
'''

def menu():
    print("1. Convert cm to ft")
    print("2. Convert km to miles")
    print("3. Convert USD to INR")
    print("4. Exit")

def cm_to_ft(cm):
    return cm/30.48 

def km_to_miles(km):
    return km*0.621371

def usd_to_inr(usd):
    return usd*85.8

while True:
    menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        cm = float(input("Enter length in cm: "))
        print(f"{cm} cm is approximately {cm_to_ft(cm)} ft.")
    elif choice == 2:
        km = float(input("Enter distance in km: "))
        print(f"{km} km is approximately {km_to_miles(km)} miles.")
    elif choice == 3:
        usd = float(input("Enter amount in USD: "))
        print(f"{usd} USD is approximately {usd_to_inr(usd)} INR.")
    elif choice == 4:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")