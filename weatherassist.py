import random


temp = random.randint(0,30)

print( "It's " +str(temp) + "°C out there")

if 0<=temp<=10:
    print("get yourself some warm clothes")

if 11<=temp<=20:
    print("what a lovely day")


if 21<=temp<=30:
    print("""it's fucking hot!
dont forget to drink plenty of water.""")
