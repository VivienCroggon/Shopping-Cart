items = {"CAT FOOD" : 5, 
         "DOG FOOD" : 6, 
         "HAMSTER FOOD" : 3.50, 
         "RABBIT FOOD": 3}

customer_list = []


border = "-"*80
cart_str = "Items currently in shopping cart:"
options = """What would you like to do?

1. Add item to your cart
2. Remove an item from your cart
3. View total cost of cart
4. Checkout
"""
pet_products = "\t".join(list(items.keys()))

print(f"{border}\n\nHello and welcome to Paws n Cart!\n")

while True:
    for i in customer_list:
        if i in items:
            print_list = f"{i}\t\t£ {items[i]}"
    if len(customer_list)<1:
        greeting = f"{border}\n{cart_str}\nC A R T  E M P T Y\n{border}"
    elif len(customer_list) == 1:
        greeting = f"{border}\n{cart_str}\n{print_list}\n{border}"
    elif len(customer_list)>1:
        print_list = ""
        for i in customer_list:
            if i in items:
                print_list += (f"{i}\t\t£ {items[i]}\n")
        greeting = f"{border}\n{cart_str}\n{print_list}\n{border}"

    print(f"{greeting}\n{options}\n{border}")

    choice = input("Please enter the number of which option you would like to select: \n")
    if choice.isnumeric():
        choice = int(choice)
        if choice == 1:
            while True:
                add_item = input(f"""{border}\nPlease type name of item you wish to add, or type BACK to return to menu:\n{pet_products}\n\n{border}\n""")
                add_item = add_item.upper()
                if add_item == "BACK":
                    break
                elif add_item in items:
                    customer_list.append(add_item)
                    print(f"{border}\n\n{add_item} added to cart!\n")
                else:
                    print(f"{border}\n\nSorry, we don't stock that item!\n")
                
        elif choice == 2:
            while True:
                if len(customer_list) > 0:
                    remove_item = input(f"{border}\nPlease type name of item you wish to remove, or type BACK to return to menu:\n")
                    remove_item = remove_item.upper()
                    if remove_item == "BACK":
                        break
                    elif remove_item in customer_list:
                        customer_list.remove(remove_item)
                        print(f"\n{border}\n\n{remove_item} removed from cart!\n")
                    else:
                        print(f"{border}\n\nSorry, no such item in cart!\n")
                else:
                    print(f"{border}\n\nNo items to remove!\n")
                    break

        elif choice == 3:
            cost = 0
            for i in customer_list:
                if i in items.keys():
                    cost += items[i]
            print(f"\n{border}\n\nTotal of items in cart: £{cost}\n")

        elif choice == 4:
            print(f"{border}\nProceeding to Checkout!\n{border}")
            break
        elif choice > 4:
            print(f"{border}\n\nSorry, your input was invalid!\n")
    else:
        print(f"{border}\n\nSorry, your input was invalid!\n")
