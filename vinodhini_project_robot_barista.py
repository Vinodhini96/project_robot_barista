# robot coffee barista project

#welcome the customers
print("Hello!!Welcome to vinie's coffee cafe!!")

print("------------------------------------------------------------")

#ask for the customers name
name = input("what is your name?\n")

#welcome the customer with their name
print(f"hello {name}. thankyou for coming in today.\n")

print("--------------------------------------------------------------")

#set the menu
menu= '''*****
black coffee     ₹ 150 
macchiato        ₹ 250
cappucino        ₹ 200
mocha            ₹ 230
latte            ₹ 200
americano        ₹ 185
espresso         ₹ 190       
*****'''

#ask for the order from the customer and displey the menu
order = input(f"what would you like to order?\n our menu today is: \n{menu}\n")

# if order == "black coffee" or order == "macchiato" or order=="cappucino" or order == "mocha" or order == "latte" or order == "americano" or order== "espresso":
#     quantity = input(f"nice choice!! how many {order}s would you like?\n")
# else:
#     print("invalid input")
menu_list = ["black coffee", "macchiato", "cappucino", "mocha","latte", "americano", "espresso"]    
    
if order not in menu_list:
    print("invalid input")
    print("please try again")
    exit()   
else:
    quantity = input(f"nice choice!! how many {order}s would you like?\n")

#set cost for each item
if order == "black coffee":
    cost = 150
elif order == "macchiato": 
    cost = 250
elif order == "cappucino":
    cost = 200
elif order == "mocha":
    cost = 230
elif order == "latte":
    cost = 200
elif order == "americano":
    cost = 185
elif order == "espresso":
    cost = 190

#print(f"the price of 1 {order} is: ₹{cost}")

print("-----------------------------------------------------------------")

#ask the customer if they have more orders
another_order = input("would you like to order anything else?: YES/NO\n")

#if amother_order is yes , show the menu  and take the order

if another_order == "yes" :
    order2 = input(menu)
    if order2 not in menu_list:
        print("invalid input")
        print("please try gain")
        exit()   
    else:
        quantity2 = input(f"nice choice!! how many {order2}s would you like?\n")

    if order2 == "black coffee":
        cost2 = 150
    elif order2 == "macchiato":
        cost2 = 250
    elif order2 == "cappucino":
        cost2 = 200
    elif order2 == "mocha":
        cost2 = 230
    elif order2 == "latte":
        cost2 = 200
    elif order2 == "americano":
        cost2 = 185
    elif order2 == "espresso":
        cost2 = 190

    #print(f"the price of 1{order2} is : ₹{cost2}")
else:                                                #if another_order is no, finalise
    cost2 = 0
    quantity2 =0

#calculate the order price and set it to to a variable "total"
total = cost * int(quantity) + cost2 * int(quantity2)

print("----------------------------------------------------------")

#finalize
print(f"the total amount of your order is : ₹{total}")
print("thankyou for choosing vinie's coffee cafe!!\nSee you soon!!!!")
print("------------------------------------------------------------")