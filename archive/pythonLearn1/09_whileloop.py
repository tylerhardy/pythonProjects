import random

random_num = 0

#while(random != 15):
    #print(random_num)
    #random_num = random.randrange(0,100)

i = 0
while(i <= 20):
    if(i%2 == 0):
        print(i)
    elif (i == 9):
        break
    else:
        i += 1 # i = i + 1
        continue
    
    i += 1