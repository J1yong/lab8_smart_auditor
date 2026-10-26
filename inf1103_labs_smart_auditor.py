inventory = []

class product:
    def __init__(self, id, name, stock, price):
        self.__product_id = id
        self.__name = name
        self.__stock  = stock
        self. __price = price


    def update_stock(self, newstock):
        self.__stock = newstock


    def display_information(self):
        return (f" ID:{self.__product_id} | Name:{self.__name} | Stock:{self.__stock} | price:{self.__price}")

    def get_product_id(self):
        return self.__product_id



def load_latest_id():
    if len(inventory) == 0:
        return 1000

    return max(item.get_product_id() for item in inventory)


def display_all_product():
     
    print("----------------------------------------------------")
    
    for product in inventory:
        print(product.display_information())

    print("---------------------------------------------------")



def update_stock():
    while True:

        try:
            print("Update Stock")
            product = int(input(" Enter Product ID: "))

            for item in inventory:
                    if product == item.get_product_id():
                        print(item.display_information())

                        newstock = int(input("New Stock Quantity: "))
                        item.update_stock(newstock)
                        print("Stock updated successfully")

                        return False



        except ValueError:
            print("please key in a valid product id! try agn.")
            continue


def search_product():
    while True:
        try:
            product = int(input("Enter Product ID: "))
            for item in inventory:
                if product == item.get_product_id():
                    print("Product Found")
                    print("---------------------------------------------------------")
                    print(item.display_information())
                    print("----------------------------------------------------------")

                    return False
                else:
                    print("invalid product id! try agn.")
                    continue
        
        except ValueError:
            print("Please key a interger!")
            continue

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

    product_id = load_latest_id()
    product_id += 1


    main_print()

    while True:

        try:
            print("-----------------------------------------------------")
            choice = int(input("Enter option:  "))

        except ValueError:
            print("invalid input! try again")
            continue

        if choice == 1:
            display_all_product()

        elif choice == 2:
            product_id = input_values(product_id)

        elif choice == 3:
            update_stock()

        elif choice == 4:
            search_product()

        elif choice == 5:
            print("inventory saved")
            print("inventory saved!")

        elif choice == 6:
            print("you have quited the program!")
            return False

main()
        