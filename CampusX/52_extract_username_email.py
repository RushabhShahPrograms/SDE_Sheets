'''
Extract username from a given email.
Eg if the email is nitish24singh@gmail.com then the username
should be nitish24singh
'''

def extract_username(email):
    return email.split('@')[0]

email = input("Enter the email: ")
print(f"The username is {extract_username(email)}")