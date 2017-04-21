"""21 Try Except"""
number = input("Just pick a number?\n")
number = 0

while True:
    try:
        number = int(input("Pick a number: \n"))
    except ValueError:
        print("It's not a number!\n")
        continue
        # else:
        #     print("It's a number")
        #     break
    if number % 4 == 0: # If is multiple of 4
        print("The number " + str(number) + " Is multiple of 4 and an even number")
    elif number % 2 == 0: # If is multiple of 2 and if it is even number
        print("The number " + str(number) + " is an even number")
    else:
        print("The number " + str(number) + " is an odd number")