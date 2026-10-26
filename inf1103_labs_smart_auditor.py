inventory = []


class product:
    def __init__(self, id, name, stock, price):
        self.__product_id = id
        self.__name = name
        self.__stock  = stock
        self. __price = price


def input_values(product_id):

    while True:
        try:

            new_product = str(input("Product Name: "))
            quantity = int(input("Quantity: "))
            price = float(input("Price: "))
            product1 = product(product_id, new_product, quantity, price)
         
            inventory.append(product1)
            product_id += 1

            print("Product add successfully!")

            break

        except ValueError:
            print("invalid input, please try again")
            continue

    return product_id

def main_print():
    print("----------------Menu------------------")
    print("1. Display all products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit program")



def main():

    print("======================================")
    print("Welcome to INVENTORY MANAGEMENT SYSTEM")
    print("======================================")
    

    main_print()

    while True:

        try:
            print("-----------------------------------------------------")
            choice = int(input("Enter option:  "))

        except ValueError:
            print("invalid input! try again")
            continue

        if choice == 1:
            print("display_all_product()")

        elif choice == 2:
            product_id = input_values(product_id)

        elif choice == 3:
            print("update_stock()")

        elif choice == 4:
            print("search_product()")

        elif choice == 5:
            print("inventory saved")
            print("inventory saved!")

        elif choice == 6:
            print("you have quited the program!")
            return False

main()
        