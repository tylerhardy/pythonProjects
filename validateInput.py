user_info = {'age':'','first_name':'','last_name':'','email':'','password':''}

def age():
    while True:
        print('Please enter your age:', end=' ')
        age = input()
        if age.isdecimal():
            user_info['age'] = age
            return age
        else:
            print('Invalid input, please try again')
            continue

def first_name():
    while True:
        print('Please enter your first name:', end=' ')
        first_name = input()
        if first_name.isalpha():
            user_info['first_name'] = first_name
            return first_name
        else:
            print('Invalid input, please try again')
            continue

def last_name():
    while True:
        print('Please enter your last name:', end=' ')
        last_name = input()
        if last_name.isalpha():
            user_info['last_name'] = last_name
            return last_name
        else:
            print('Invalid input, please try again')
            continue

def email():
    while True:
        print('Please enter your email:', end=' ')
        email = input()
        if email.isspace() == False:
            user_info['email'] = email
            return email
        else:
            print('Invalid input, please try again')
            continue

def password():
    while True:
        print('Please enter a new password (letters and numbers only):', end=' ')
        password = input()
        if password.isalnum():
            user_info['password'] = password
            return password
        else:
            print('Invalid input, please try again')
            continue

age = age()
first_name = first_name()
last_name = last_name()
email = email()
password = password()

print(user_info)
# print('Is everything correct?', age, first_name, last_name, email, password, sep='\n')