#Jeffrey Linney
#April 15, 2024
#P5LAB
#User-defined functions

#Define function
def disperse_change(change):

    print(f"Change owed: {change}")
    
    if change == 0:
        print("No Change Due")

    #Calculate the amount of each coin needed
    #integer division - //

    num_dollars = change // 100
    change = change - (num_dollars * 100)

    num_quarters = change // 25
    change = change - (num_quarters * 25)

    num_dimes = change // 10
    change = change - (num_dimes * 10)

    num_nickles = change // 5
    change = change - (num_nickles *5)

    num_pennies = change // 1

    #Display coins owed

    if num_dollars > 0:
            print(num_dollars,  end=" ")
            if num_dollars == 1:
                print("Dollar")
            else:
                print("Dollars")
                
    if num_quarters > 0:
            print(num_quarters,  end=" ")
            if num_quarters == 1:
                print("Quarter")
            else:
                print("Quarters")

    if num_dimes > 0:
            print(num_dimes,  end=" ")
            if num_dimes == 1:
                print("Dime")
            else:
                print("Dimes")

    if num_nickles > 0:
            print(num_nickles,  end=" ")
            if num_nickles == 1:
                print("Nickle")
            else:
                print("Nickles")

    if num_pennies > 0:
            print(num_pennies,  end=" ")
            if num_pennies == 1:
                print("Penny")
            else:
                print("Pennies")


def show_avail_items(dictionary):
    print(f"{'Grocery Item':<25}{'Price'}")
    print("-------------------------")
    for key, value in dictionary.items():
        print(f"{key:<25}${value:.2f}")
    print("------------------------")

def add_items(dictionary):
    cart = []
    item = input("Enter an item to add to the cart or type 'end' to stop adding items: ")
    while item != "end":
        if item in dictionary.keys():
            cart.append(item)
        else:
            print(f"{item} is not in stock")
        item = input("Enter an item to add to the cart or type 'end' to stop adding items: ")

    return cart

def get_total(cart,dictionary):
    print("Grocery Checkout Receipt")
    print("-----------------------")
    total = 0
    for item in cart:
        print(f"{item:<20}{dictionary[item]:.2f}")
        total += dictionary[item]

    #Display totals
    print()
    print(f"SUBTOTAL:           ${total:.2f}")
    tax = total * .07
    final_total = total + tax
    print(f"TAX:                ${tax:.2f}")
    print(f"TOTAL               ${final_total:.2f}")
    return final_total
            
    

#Main logic starts here

#Call function

def main():

    #Create dictionary with items and prices
    items = {"apples":3.69, "berries":4.00, "chocolate":2.89, "turkey":6.99, "cheese":4.00, "pepsi":7.89, "eggs":3.50, "bread":3.00}

    #Call the show_avail_items function
    
    show_avail_items(items)

    #Call the add_item function
    
    cart = add_items(items)
    print(cart)
    print()

    #Display items in cart
    
    print("The items currently in your cart are: ")
    for item in cart:
        print(item)
             
    #Call the get total function
        
    cart_total = get_total(cart, items)

    #Find out how much money the customer is presenting
    print()
    
    pay_owed = float(input('Enter the total amount of currency you are paying: $'))

    change_owed =  pay_owed - cart_total
    
    print(f"The change owed to you is ${change_owed:.2f}")

        #disperse_change(83)
    change_owed = round(change_owed * 100)
    disperse_change (change_owed)
#Call the main
main()

