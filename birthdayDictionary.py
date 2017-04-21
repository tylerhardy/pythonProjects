birthdays = {'Tyler': 'December 10th', 'Danielle': 'Feburary 8th'}
while True:
    print('Enter a name: (Leave blank to quit)')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print('Their birthday is ' + birthdays[name] + '!')
    else:
        print('Unable to find ' + name + ' in birthday database.')
        print('Please input ' + name + "'s birthdate:")
        new_birthday = input()
        birthdays[name] = new_birthday
        print('Birthday Database Updated.')