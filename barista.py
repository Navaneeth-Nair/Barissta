import time
print("Welcome to BarStrucks")
time.sleep(2)
print("My Name Is Robot Barista")
time.sleep(2)
name = input("What is your name? ")
time.sleep(2)
if name == 'Ajinkya':
    print("Chala Ja Bsdk")
    exit()
else:
    print("Hey " + name + ", Nice Having You Here!!")
    time.sleep(1)
menu = ("Black Tea, Frappuccino, Cappuccino, Boba Tea, Espresso")
order = input("Here is our menu: " + menu + ". What Would you Like ")
time.sleep(2)
if order == 'Black Tea':
    price = 10
elif order == 'Frappuccino':
    price = 8
elif order == 'Cappucino':
    price = 9
elif order == 'Boba Tea':
    price = 12
elif order == 'Espresso':
    price = 5
else:
    print("Your Order Is Not Available As Of Now. Please Order Something else")
    exit()
number = input("How many " + order + " would you like? ")
number = int(number)
print("Your Total Would Be " + str(price*number)) 
time.sleep(2)
print("Your Order Will be ready shortly")